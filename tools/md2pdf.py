#!/usr/bin/env python3
"""Markdown -> PDF via fpdf2, sans dependance systeme.

Usage: python3 tools/md2pdf.py source.md sortie.pdf "Titre"
Requiert: pip install --break-system-packages fpdf2
"""
import re
import sys

from fpdf import FPDF

MATH = {
    r"\times": "x", r"\approx": "~", r"\sigma": "sigma", r"\sqrt": "sqrt",
    r"\Theta": "Theta", r"\Gamma": "Gamma", r"\ln": "ln", r"\frac": "",
    r"\qquad": "    ", r"\text": "", r"\tfrac": "", r"\cdot": ".",
    r"\Delta": "Delta", r"\Rightarrow": "=>",
    r"_0": "0", r"_1": "1", r"_2": "2", r"_d": "d", r"_f": "f", r"_T": "T",
    "^{-qT}": "^(-qT)", "^{-rT}": "^(-rT)", "^{(r-q)T}": "^((r-q)T)",
    "^{(r_d - r_f)T}": "^((rd-rf)T)", "^2": "2",
}

IPA = {
    "ɒ": "o", "ɪ": "i", "iː": "ee", "uː": "oo", "ˈ": "", "ˌ": "",
    "dʒ": "dj", "ʒ": "j", "ʃ": "sh", "θ": "th", "ə": "e", "ː": "",
    "ɔ": "o", "æ": "a", "ʊ": "u", "ŋ": "ng", "ɛ": "e", "ʌ": "u",
}

REPL = {
    "—": "-", "–": "-", "’": "'", "‘": "'", "“": '"', "”": '"',
    "…": "...", "≈": "~", "×": "x", "≠": "!=", "→": "->", "⚠️": "!",
    "✅": "[x]", "❌": "[ ]", "🔒": "", "⭐": "*", "📄": "", "🗣️": "",
    "🤖": "", "🔑": "", "💡": "", "🥇": "1.", "🥈": "2.", "🥉": "3.",
    "🎯": "", "📎": "", "📘": "", "🚀": "", "☕": "", "🔎": "", "✉️": "",
    "🚨": "!", "€": "EUR", "σ": "sigma", "Δ": "Delta", "Γ": "Gamma",
    "Θ": "Theta", "ρ": "rho", "φ": "phi", "₀": "0", "₁": "1", "₂": "2",
    "π": "pi", "√": "sqrt", "²": "2", "≥": ">=", "≤": "<=", "±": "+/-",
    "\u2022": "-", "\u2191": "^", "\u2193": "v", "\u2714": "ok",
    "\u2718": "x", "\u03b2": "beta",
    "\u2212": "-",   # MOINS UNICODE -> tiret ASCII (critique : sinon le signe
                      # disparait et -4,40 % devient 4,40 %)
    "\u00a0": " ", "\u202f": " ", "\u2009": " ",  # espaces insecables
}


def demath(t: str) -> str:
    t = t.replace("$$", "").replace("$", "")
    for k, v in MATH.items():
        t = t.replace(k, v)
    t = re.sub(r"\{([^{}]*)\}", r"\1", t)
    t = re.sub(r"\{([^{}]*)\}", r"\1", t)
    return re.sub(r"\s+", " ", t).strip()


def clean(t: str) -> str:
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", t)
    t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)
    t = t.replace("**", "").replace("`", "")
    t = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"\1", t)
    t = re.sub(r"~~([^~]+)~~", r"\1", t)
    t = demath(t)
    for k, v in REPL.items():
        t = t.replace(k, v)
    for k, v in IPA.items():
        t = t.replace(k, v)
    out = []
    for c in t:
        try:
            c.encode("latin-1")
            out.append(c)
        except UnicodeEncodeError:
            pass
    return "".join(out)


class PDF(FPDF):
    # fpdf2 laisse par defaut le curseur A DROITE de la cellule (new_x=RIGHT).
    # Deux multi_cell consecutifs derivaient donc de 178 mm vers la droite et
    # le texte sortait de la page. On force le retour a la marge gauche.
    def multi_cell(self, *a, **kw):
        kw.setdefault("new_x", "LMARGIN")
        kw.setdefault("new_y", "NEXT")
        return super().multi_cell(*a, **kw)

    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("Helvetica", "I", 7)
        self.set_text_color(150)
        self.cell(0, 5, self.doc_title[:90], align="R",
                  new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0)

    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", "I", 7)
        self.set_text_color(150)
        self.cell(0, 8, f"{self.page_no()}", align="C")


def render(md_path: str, pdf_path: str, title: str = "") -> None:
    lines = open(md_path, encoding="utf-8").read().split("\n")
    p = PDF()
    # le titre passe en argument traverse header() en cellule brute : il doit
    # subir le meme nettoyage latin-1 que le corps, sinon un tiret cadratin
    # fait echouer tout le rendu au premier saut de page.
    title = clean(title)
    p.doc_title = title
    p.set_title(title)
    p.set_auto_page_break(True, 18)
    p.add_page()
    p.set_margins(16, 14, 16)
    width = p.w - 32

    in_code = False
    table: list[list[str]] = []

    def flush_table() -> None:
        nonlocal table
        if not table:
            return
        rows = [r for r in table if not re.match(r"^[\s|:-]+$", "|".join(r))]
        if not rows:
            table = []
            return
        ncol = max(len(r) for r in rows)
        colw = width / ncol
        for i, row in enumerate(rows):
            row = row + [""] * (ncol - len(row))
            head = i == 0
            p.set_font("Helvetica", "B" if head else "", 7.5)
            hs = [len(p.multi_cell(colw, 4, c, dry_run=True, output="LINES"))
                  for c in row]
            h = max(hs) * 4 + 1
            if p.get_y() + h > p.h - 20:
                p.add_page()
            if head:
                p.set_fill_color(232, 236, 242)
            y0 = p.get_y()
            x = p.l_margin
            for c in row:
                p.set_xy(x, y0)
                p.multi_cell(colw, 4, c, border=1, fill=head, align="L",
                             max_line_height=4)
                x += colw
            p.set_y(y0 + h)
        p.ln(2)
        table = []

    for raw in lines:
        line = raw.rstrip()
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            p.set_font("Courier", "", 7.5)
            p.set_fill_color(245, 245, 245)
            p.multi_cell(width, 3.8, clean(line) or " ", fill=True)
            continue
        if "|" in line and line.strip().startswith("|"):
            table.append([clean(c.strip())
                          for c in line.strip().strip("|").split("|")])
            continue
        flush_table()
        if not line.strip():
            p.ln(2)
            continue
        if line.startswith("---"):
            p.ln(1)
            p.set_draw_color(200)
            p.line(p.l_margin, p.get_y(), p.w - p.r_margin, p.get_y())
            p.ln(3)
            continue
        if line.lstrip().startswith("<"):
            continue
        m = re.match(r"^(#{1,4})\s+(.*)", line)
        if m:
            lvl = len(m.group(1))
            size = {1: 15, 2: 12, 3: 10, 4: 9}[lvl]
            if lvl <= 2 and p.get_y() > 40:
                p.ln(3)
            p.set_font("Helvetica", "B", size)
            p.set_text_color(*((10, 40, 90) if lvl <= 2 else (0, 0, 0)))
            p.multi_cell(width, size * 0.45, clean(m.group(2)))
            p.set_text_color(0)
            p.ln(1)
            continue
        if line.lstrip().startswith(">"):
            txt = clean(re.sub(r"^\s*>\s?", "", line))
            if not txt:
                continue
            p.set_font("Helvetica", "I", 8)
            p.set_fill_color(240, 244, 250)
            p.multi_cell(width, 4, txt, fill=True)
            continue
        m = re.match(r"^\s*[-*]\s+(.*)", line)
        if m:
            p.set_font("Helvetica", "", 8.5)
            p.multi_cell(width, 4.2, "  - " + clean(m.group(1)))
            continue
        m = re.match(r"^\s*(\d+)\.\s+(.*)", line)
        if m:
            p.set_font("Helvetica", "", 8.5)
            p.multi_cell(width, 4.2, f"  {m.group(1)}. " + clean(m.group(2)))
            continue
        p.set_font("Helvetica", "", 8.5)
        p.multi_cell(width, 4.2, clean(line))
    flush_table()
    p.output(pdf_path)
    print("PDF ecrit:", pdf_path, f"{p.page_no()} pages")


if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "")
