#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
md2pdf — convertit un sous-ensemble de Markdown en PDF A4 propre (fpdf2 + DejaVu).

Rend **gras**, *italique*, `code inline`, tableaux, listes, citations, blocs de
code et règles horizontales. Tout en Unicode (DejaVu couvre le grec Δ Γ ν Θ ρ,
les flèches →, les signes × ≥ ≠ ≈, les accents FR).

Installation (une fois) :
    python3 -m venv .venv
    .venv/bin/pip install fpdf2 matplotlib

    fpdf2  : moteur PDF.
    matplotlib : fournit les variantes DejaVu oblique/italique (sinon l'italique
                 est rendu en romain — dégradation acceptable).

Usage :
    .venv/bin/python tools/md2pdf.py PROGRAMME.md PROGRAMME.pdf

Métadonnées (commentaires HTML en tête du .md, ignorés ailleurs) :
    <!-- subtitle: … -->   sous-titre de couverture (1re occurrence)
    <!-- date: … -->       ligne de date de couverture
    <!-- meta: … -->       puce de couverture (répétable)
    <!-- pagebreak -->     saut de page forcé dans le corps
La couverture est construite à partir du premier titre `# ` + ces métadonnées.
"""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

from fpdf import FPDF

# --------------------------------------------------------------------------- #
# Mise en page & palette
# --------------------------------------------------------------------------- #
PAGE_W, PAGE_H = 210.0, 297.0  # A4 portrait (mm)
MARGIN = 16.0
TOP = 20.0                     # laisse la place au bandeau d'en-tête
BODY_W = PAGE_W - 2 * MARGIN   # 178 mm
BODY_FONT = 9.8
BODY_LH = 4.5                  # hauteur de ligne du corps
CELL_PAD = 1.7                 # marge intérieure des cellules de tableau
CODE_FONT = 8.2

ACCENT = (17, 42, 91)          # bleu nuit
ACCENT_2 = (36, 84, 155)
INK = (34, 37, 42)
MUTED = (108, 114, 124)
LIGHT = (236, 241, 249)
CODE_BG = (243, 244, 247)
QUOTE_BG = (242, 245, 250)
RULE = (208, 213, 222)
ZEBRA = (247, 248, 250)
WHITE = (255, 255, 255)
COVER_BAND = 72.0

# --------------------------------------------------------------------------- #
# Polices
# --------------------------------------------------------------------------- #
_SYSTEM_DIR = Path("/usr/share/fonts/truetype/dejavu")
_MATPLOTLIB_DIR = None
try:
    import matplotlib  # noqa: WPS433

    _MATPLOTLIB_DIR = (
        Path(matplotlib.__file__).parent / "mpl-data" / "fonts" / "ttf"
    )
except Exception:  # noqa: BLE001
    _MATPLOTLIB_DIR = None


def _find_font(*names: str) -> Path:
    for d in (_SYSTEM_DIR, _MATPLOTLIB_DIR):
        if d is None:
            continue
        for n in names:
            p = d / n
            if p.exists():
                return p
    raise FileNotFoundError(
        f"Police DejaVu introuvable ({names[0]}). "
        "Installez fonts-dejavu-core ou pip install matplotlib."
    )


REGULAR = _find_font("DejaVuSans.ttf")
BOLD = _find_font("DejaVuSans-Bold.ttf")
OBLIQUE = _find_font("DejaVuSans-Oblique.ttf", "DejaVuSans.ttf")
BOLD_OBLIQUE = _find_font("DejaVuSans-BoldOblique.ttf", "DejaVuSans-Bold.ttf")
MONO = _find_font("DejaVuSansMono.ttf")
MONO_BOLD = _find_font("DejaVuSansMono-Bold.ttf", "DejaVuSansMono.ttf")

_HAS_TRUE_ITALIC = OBLIQUE.name.endswith("Oblique.ttf")


def _strip_md(s: str) -> str:
    """Retire la syntaxe inline pour mesurer la largeur réelle."""
    return re.sub(r"[*_`]", "", s)


# --------------------------------------------------------------------------- #
# Parseur markdown inline
# --------------------------------------------------------------------------- #
def tokenize(text: str):
    """Découpe une chaîne en segments (style, texte).

    Styles : '' = romain, 'B' = gras, 'I' = italique, 'C' = code.
    Les marqueurs non appariés sont rendus littéralement.
    """
    tokens = []
    i = 0
    n = len(text)
    buf = []

    def flush():
        if buf:
            tokens.append(("", "".join(buf)))
            buf.clear()

    while i < n:
        c = text[i]
        if c == "`":
            j = text.find("`", i + 1)
            if j != -1:
                flush()
                tokens.append(("C", text[i + 1 : j]))
                i = j + 1
                continue
        elif c == "*":
            if i + 1 < n and text[i + 1] == "*":
                j = text.find("**", i + 2)
                if j != -1:
                    flush()
                    tokens.append(("B", text[i + 2 : j]))
                    i = j + 2
                    continue
            else:
                j = text.find("*", i + 1)
                if j != -1:
                    flush()
                    tokens.append(("I", text[i + 1 : j]))
                    i = j + 1
                    continue
        buf.append(c)
        i += 1
    flush()
    return tokens


def strip_inline(text: str) -> str:
    return "".join(seg for _, seg in tokenize(text))


# --------------------------------------------------------------------------- #
# Blocs
# --------------------------------------------------------------------------- #
def _parse_blocks(text: str):
    """Découpe le Markdown en blocs typés."""
    meta = {"subtitle": "", "date": "", "metas": []}
    lines = text.splitlines()
    blocks = []
    i = 0
    n = len(lines)

    def flush_para(buf):
        if buf:
            blocks.append({"t": "p", "text": " ".join(buf)})

    para = []
    while i < n:
        raw = lines[i]
        s = raw.rstrip()
        st = s.strip()

        # métadonnées / saut de page
        if st.startswith("<!--"):
            m = re.match(r"<!--\s*subtitle:\s*(.*?)\s*-->", st)
            if m:
                meta["subtitle"] = m.group(1)
            m = re.match(r"<!--\s*date:\s*(.*?)\s*-->", st)
            if m:
                meta["date"] = m.group(1)
            m = re.match(r"<!--\s*meta:\s*(.*?)\s*-->", st)
            if m:
                meta["metas"].append(m.group(1))
            if "pagebreak" in st:
                flush_para(para)
                para = []
                blocks.append({"t": "pagebreak"})
            i += 1
            continue

        if st == "":
            flush_para(para)
            para = []
            i += 1
            continue

        # clôture de code
        if st.startswith("```"):
            flush_para(para)
            para = []
            code = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1  # ligne de fermeture
            blocks.append({"t": "code", "lines": code})
            continue

        # titres
        m = re.match(r"^(#{1,4})\s+(.*)$", st)
        if m:
            flush_para(para)
            para = []
            blocks.append(
                {"t": "h", "level": len(m.group(1)), "text": m.group(2).strip()}
            )
            i += 1
            continue

        # règle horizontale
        if re.fullmatch(r"-{3,}|\*{3,}|_{3,}", st):
            flush_para(para)
            para = []
            blocks.append({"t": "rule"})
            i += 1
            continue

        # tableau
        if st.startswith("|"):
            flush_para(para)
            para = []
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                rows.append(cells)
                i += 1
            if len(rows) > 1 and all(
                re.fullmatch(r":?-{2,}:?", c) for c in rows[1]
            ):
                body = rows[2:]  # header + séparateur
            else:
                body = rows[1:]  # uniquement le header
            blocks.append({"t": "table", "header": rows[0], "rows": body})
            continue

        # citation
        if st.startswith(">"):
            flush_para(para)
            para = []
            q = []
            while i < n and lines[i].strip().startswith(">"):
                q.append(lines[i].strip()[1:].strip())
                i += 1
            blocks.append({"t": "quote", "text": " ".join(q)})
            continue

        # listes
        m = re.match(r"^(\s*)([-*+]|\d+\.)\s+(.*)$", raw)
        if m:
            flush_para(para)
            para = []
            indent = len(m.group(1)) // 2
            blocks.append(
                {"t": "ul", "indent": indent, "text": m.group(3).strip()}
            )
            i += 1
            continue

        # paragraphe
        para.append(st)
        i += 1

    flush_para(para)
    return meta, blocks


# --------------------------------------------------------------------------- #
# PDF
# --------------------------------------------------------------------------- #
class Pdf(FPDF):
    def __init__(self, short_title: str):
        super().__init__("P", "mm", "A4")
        self.short_title = short_title
        self.set_margins(MARGIN, TOP, MARGIN)
        self.set_auto_page_break(True, margin=18.0)
        self.add_font("DejaVu", "", str(REGULAR))
        self.add_font("DejaVu", "B", str(BOLD))
        self.add_font("DejaVu", "I", str(OBLIQUE))
        self.add_font("DejaVu", "BI", str(BOLD_OBLIQUE))
        self.add_font("mono", "", str(MONO))
        self.add_font("mono", "B", str(MONO_BOLD))
        self.alias_nb_pages("{nb}")

    # -- styles ------------------------------------------------------------- #
    def _style(self, style: str, size: float):
        if style == "B":
            self.set_font("DejaVu", "B", size)
        elif style == "I":
            self.set_font("DejaVu", "I", size)
        elif style == "BI":
            self.set_font("DejaVu", "BI", size)
        elif style == "C":
            self.set_font("mono", "", size - 0.6)
        else:
            self.set_font("DejaVu", "", size)

    # -- texte riche -------------------------------------------------------- #
    def wrap_md(self, text: str, width: float, size: float = BODY_FONT):
        """Retourne une liste de lignes ; chaque ligne = [(style, mot), …]."""
        words = []
        for style, seg in tokenize(text):
            for w in seg.split(" "):
                if w != "":
                    words.append((style, w))
        self._style("", size)
        space_w = self.get_string_width(" ")
        lines = []
        cur = []
        cur_w = 0.0
        for style, w in words:
            self._style(style, size)
            ww = self.get_string_width(w)
            if ww > width:
                # mot trop long (nom de fichier, commande) : césure caractère
                for chunk in self._chunk_word(style, w, size, width):
                    add = self.get_string_width(chunk) + (space_w if cur else 0.0)
                    if cur and cur_w + add > width:
                        lines.append(cur)
                        cur = [(style, chunk)]
                        cur_w = self.get_string_width(chunk)
                    else:
                        cur.append((style, chunk))
                        cur_w += add
                continue
            add = ww + (space_w if cur else 0.0)
            if cur and cur_w + add > width:
                lines.append(cur)
                cur = []
                cur_w = 0.0
                cur.append((style, w))
                cur_w = ww
            else:
                cur.append((style, w))
                cur_w += add
        if cur:
            lines.append(cur)
        return lines

    def _chunk_word(self, style: str, word: str, size: float, width: float):
        self._style(style, size)
        chunks = []
        cur = ""
        for ch in word:
            if cur and self.get_string_width(cur + ch) > width:
                chunks.append(cur)
                cur = ch
            else:
                cur += ch
        if cur:
            chunks.append(cur)
        return chunks

    def _draw_line(self, x: float, y: float, line, h: float, size: float):
        self.set_xy(x, y)
        for idx, (style, w) in enumerate(line):
            self._style(style, size)
            self.write(h, w + (" " if idx < len(line) - 1 else ""))

    def _write_block(self, x: float, y: float, width: float, text: str,
                     h: float, size: float):
        """Écrit un bloc de texte riche (retourne la nouvelle position y)."""
        self.set_left_margin(x)
        self.set_right_margin(PAGE_W - x - width)
        self.set_xy(x, y)
        for style, seg in tokenize(text):
            self._style(style, size)
            self.write(h, seg)
        self.set_left_margin(MARGIN)
        self.set_right_margin(MARGIN)
        return self.get_y()

    # -- en-tête / pied de page --------------------------------------------- #
    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("DejaVu", "", 8.0)
        self.set_text_color(*MUTED)
        self.set_y(8)
        self.set_x(MARGIN)
        self.cell(BODY_W / 2, 5, self.short_title, align="L")
        self.set_x(MARGIN + BODY_W / 2)
        self.cell(BODY_W / 2, 5, "Calvin · Septembre 2026", align="R")
        self.set_draw_color(*RULE)
        self.set_line_width(0.3)
        self.line(MARGIN, 14.5, PAGE_W - MARGIN, 14.5)

    def footer(self):
        if self.page_no() == 1:
            return
        self.set_y(-13)
        self.set_font("DejaVu", "", 8.0)
        self.set_text_color(*MUTED)
        self.cell(0, 8, f"{self.page_no()} / {{nb}}", align="C")

    # -- primitives --------------------------------------------------------- #
    def heading(self, level: int, text: str):
        text = strip_inline(text)
        if level == 2:
            if self.get_y() > PAGE_H - 46:
                self.add_page()
            self.ln(3)
            self.set_font("DejaVu", "B", 13.0)
            self.set_text_color(*ACCENT)
            self.multi_cell(BODY_W, 6.4, text)
            y = self.get_y() + 1.2
            self.set_draw_color(*ACCENT_2)
            self.set_line_width(0.7)
            self.line(MARGIN, y, MARGIN + 34, y)
            self.set_y(y + 2.4)
        elif level == 3:
            if self.get_y() > PAGE_H - 34:
                self.add_page()
            self.ln(2.6)
            self.set_font("DejaVu", "B", 11.2)
            self.set_text_color(*ACCENT_2)
            self.multi_cell(BODY_W, 5.6, text)
            self.ln(0.8)
        else:  # niveau 4
            if self.get_y() > PAGE_H - 30:
                self.add_page()
            self.ln(1.8)
            self.set_font("DejaVu", "B", 10.0)
            self.set_text_color(*INK)
            self.multi_cell(BODY_W, 5.0, text)
            self.ln(0.6)

    def para(self, text: str):
        self.set_text_color(*INK)
        self._write_block(MARGIN, self.get_y(), BODY_W, text, BODY_LH, BODY_FONT)
        self.ln(1.4)

    def bullet(self, level: int, text: str):
        if self.get_y() > PAGE_H - 24:
            self.add_page()
        indent = MARGIN + 4.5 * level
        width = PAGE_W - MARGIN - indent
        markers = ["•", "–", "·"]
        mk = markers[min(level, 2)]
        y0 = self.get_y()
        self.set_text_color(*ACCENT_2)
        self.set_font("DejaVu", "B", BODY_FONT)
        self.set_xy(indent, y0)
        self.cell(5.0, BODY_LH, mk)
        self.set_text_color(*INK)
        self._write_block(indent + 5.0, y0, width - 5.0, text, BODY_LH, BODY_FONT)
        self.ln(0.7)

    def quote(self, text: str):
        self.ln(0.8)
        w = BODY_W
        inner_w = w - 10
        lines = self.wrap_md(text, inner_w, BODY_FONT)
        h = max(len(lines), 1) * BODY_LH + 3.4
        if self.get_y() + h > PAGE_H - 18:
            self.add_page()
        y0 = self.get_y()
        self.set_fill_color(*QUOTE_BG)
        self.rect(MARGIN, y0, w, h, "F")
        self.set_fill_color(*ACCENT_2)
        self.rect(MARGIN, y0, 1.6, h, "F")
        self.set_text_color(*INK)
        y = y0 + 1.7
        for ln in lines:
            self._draw_line(MARGIN + 6, y, ln, BODY_LH, BODY_FONT)
            y += BODY_LH
        self.set_y(y0 + h + 1.2)

    def code_block(self, lines):
        self.ln(1.2)
        if self.get_y() > PAGE_H - 40:
            self.add_page()
        x0 = MARGIN
        w = BODY_W
        self.set_font("mono", "", CODE_FONT)
        disp = lines if lines else [""]
        h = len(disp) * 3.9 + 3.4
        if self.get_y() + h > PAGE_H - 18:
            self.add_page()
        y0 = self.get_y()
        self.set_fill_color(*CODE_BG)
        self.rect(x0, y0, w, h, "F")
        self.set_text_color(*INK)
        self.set_xy(x0 + 4, y0 + 2.2)
        for ln_ in disp:
            self.set_x(x0 + 4)
            self.multi_cell(w - 8, 3.9, ln_)
        self.set_y(y0 + h + 1.2)

    def table(self, header, rows):
        ncol = len(header)
        if ncol == 0:
            return

        def norm(row):
            r = list(row)
            while len(r) < ncol:
                r.append("")
            return r[:ncol]

        header = norm(header)
        rows = [norm(r) for r in rows]
        pad = CELL_PAD
        hdr_h = 6.0

        # largeurs proportionnelles au contenu (mesure sur texte "aplati")
        self.set_font("DejaVu", "", BODY_FONT)
        natural = [0.0] * ncol
        for r in [header] + rows:
            for i, c in enumerate(r):
                natural[i] = max(natural[i], self.get_string_width(_strip_md(c)) + 8)
        s = sum(natural) or 1.0
        raw = [max(14.0, (n / s) * BODY_W) for n in natural]
        ratio = BODY_W / sum(raw)
        widths = [r * ratio for r in raw]

        def row_lines(cells):
            return [self.wrap_md(c, w - 2 * pad, BODY_FONT) for c, w in zip(cells, widths)]

        def draw_header(y):
            x = MARGIN
            self.set_fill_color(*ACCENT)
            for w in widths:
                self.rect(x, y, w, hdr_h, "F")
                x += w
            x = MARGIN
            self.set_text_color(*WHITE)
            self.set_font("DejaVu", "B", BODY_FONT)
            for c, w in zip(header, widths):
                self.set_xy(x + pad, y + pad)
                self.multi_cell(w - 2 * pad, BODY_LH, strip_inline(c))
                x += w

        if self.get_y() > PAGE_H - 30:
            self.add_page()
        self.ln(1.0)
        y = self.get_y()
        draw_header(y)
        self.set_y(y + hdr_h)

        for ri, r in enumerate(rows):
            rl = row_lines(r)
            h = max((len(l) for l in rl), default=1) * BODY_LH + 2 * pad
            if h < 5.6:
                h = 5.6
            if self.get_y() + h > PAGE_H - 18:
                self.add_page()
                y = self.get_y()
                draw_header(y)
                self.set_y(y + hdr_h)
            y = self.get_y()
            fill = ZEBRA if ri % 2 == 1 else WHITE
            self.set_fill_color(*fill)
            self.rect(MARGIN, y, BODY_W, h, "F")
            x = MARGIN
            self.set_text_color(*INK)
            for ci, (c, w) in enumerate(zip(r, widths)):
                yy = y + pad
                for ln in rl[ci]:
                    self._draw_line(x + pad, yy, ln, BODY_LH, BODY_FONT)
                    yy += BODY_LH
                x += w
            self.set_y(y + h)
        # filet de séparation fin
        self.set_draw_color(*RULE)
        self.set_line_width(0.2)
        self.line(MARGIN, self.get_y(), MARGIN + BODY_W, self.get_y())
        self.ln(2.0)

    def rule(self):
        y = self.get_y() + 1.6
        self.set_draw_color(*RULE)
        self.set_line_width(0.4)
        self.line(MARGIN, y, PAGE_W - MARGIN, y)
        self.set_y(y + 3.0)


# --------------------------------------------------------------------------- #
# Couverture
# --------------------------------------------------------------------------- #
def _cover(pdf: Pdf, title: str, meta):
    pdf.add_page()
    pdf.set_fill_color(*ACCENT)
    pdf.rect(0, 0, PAGE_W, COVER_BAND, "F")
    pdf.set_text_color(*WHITE)
    pdf.set_font("DejaVu", "B", 24.0)
    pdf.set_xy(MARGIN, 24)
    pdf.multi_cell(BODY_W, 11, strip_inline(title))
    if meta["subtitle"]:
        pdf.set_font("DejaVu", "", 11.5)
        pdf.set_text_color(198, 212, 236)
        pdf.set_xy(MARGIN, 52)
        pdf.multi_cell(BODY_W, 5.8, strip_inline(meta["subtitle"]))

    y = COVER_BAND + 14
    pdf.set_text_color(*ACCENT)
    pdf.set_font("DejaVu", "B", 12.0)
    pdf.set_xy(MARGIN, y)
    pdf.multi_cell(BODY_W, 6, strip_inline(meta["date"] or ""))
    y = pdf.get_y() + 4

    pdf.set_font("DejaVu", "", 11.0)
    pdf.set_text_color(*INK)
    for m in meta["metas"]:
        pdf.set_xy(MARGIN, y)
        pdf.set_fill_color(*ACCENT_2)
        pdf.rect(MARGIN, y + 1.6, 2.8, 2.8, "F")
        pdf.set_xy(MARGIN + 6, y)
        pdf.multi_cell(BODY_W - 6, 5.6, strip_inline(m))
        y = pdf.get_y() + 2.4

    pdf.set_font("DejaVu", "", 8.5)
    pdf.set_text_color(*MUTED)
    pdf.set_xy(MARGIN, PAGE_H - 30)
    pdf.multi_cell(
        BODY_W,
        4.4,
        f"Programme officiel · généré le {date.today().isoformat()} · "
        "source : github.com/Calvin29990/Masterclass-front",
    )


# --------------------------------------------------------------------------- #
# Rendu principal
# --------------------------------------------------------------------------- #
def render(text: str, pdf_path: Path):
    meta, blocks = _parse_blocks(text)

    title = "Programme"
    for b in blocks:
        if b["t"] == "h" and b["level"] == 1:
            title = strip_inline(b["text"])
            break

    short_title = " ".join(title.split())[:48]
    pdf = Pdf(short_title)

    _cover(pdf, title, meta)
    first = True
    for b in blocks:
        if first and b["t"] == "h" and b["level"] == 1:
            first = False
            continue
        first = False
        if b["t"] == "h":
            pdf.heading(b["level"], b["text"])
        elif b["t"] == "p":
            pdf.para(b["text"])
        elif b["t"] == "ul":
            pdf.bullet(b["indent"], b["text"])
        elif b["t"] == "table":
            pdf.table(b["header"], b["rows"])
        elif b["t"] == "code":
            pdf.code_block(b["lines"])
        elif b["t"] == "quote":
            pdf.quote(b["text"])
        elif b["t"] == "rule":
            pdf.rule()
        elif b["t"] == "pagebreak":
            pdf.add_page()

    pdf.output(str(pdf_path))
    return pdf.page_no()


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        sys.exit(2)
    src = Path(argv[1])
    out = Path(argv[2])
    if not src.exists():
        print(f"Introuvable : {src}", file=sys.stderr)
        sys.exit(1)
    pages = render(src.read_text(encoding="utf-8"), out)
    print(f"OK → {out} ({pages} pages)")


if __name__ == "__main__":
    main(sys.argv)
