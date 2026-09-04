# Masterclass Front — Septembre 2026

Préparation **élite Front Office** de Calvin : 22 jours (5 → 30 septembre
2026), 6 h/jour, objectif Superday S&T / dérivés / structurés.

Ce dépôt est le **cerveau du mois**. Le simulateur reste le lab séparé
[`Calvin29990/shockdesk`](https://github.com/Calvin29990/shockdesk).

## 🎯 Le programme (PDF)

➡️ **Télécharger le PDF :** [`programme-elite-2026.pdf`](./programme-elite-2026.pdf)

Source Markdown : [`00-programme-elite-2026.md`](./00-programme-elite-2026.md).

## 📚 Contenu

| Fichier | Rôle |
|---|---|
| `00-programme-elite-2026.md` | Programme amélioré (source du PDF) — 22 jours, ticket de sortie par jour |
| `programme-elite-2026.pdf` | PDF à mettre dans le Drive |
| `REPRISE-CONTEXTE.md` | Contexte complet pour reprendre avec une IA (Arena / Gemini) |
| `01-programme-elite-05-30-septembre-2026.md` | Programme original (gelé) |
| `02-catalogue-drive.md` | 61/61 fichiers Drive, rôle et jour d'emploi |
| `03-octobre-base-recherche.md` | Ce qu'on ne fait pas en septembre (octobre) |
| `04-fiche-suivi.md` | Cases à cocher + bloc du jour à recoller |
| `05-nettoyage-github.md` | Audit des 4 dépôts |
| `06-ecarts-vs-ebauche.md` | Pourquoi l'ébauche 4 h ne tient pas |
| `livrables/` | 21 scripts Python (un par jour, à partir de J1) |
| `recherche/` | Mémoire ShockDesk (journal, carnet, roadmap) |
| `suivi/` | Suivi daté |
| `tools/md2pdf.py` | Générateur Markdown → PDF (fpdf2 + DejaVu) |

## 🔗 Liens

- **Drive source (61/61 fichiers) :**
  https://drive.google.com/drive/folders/1NdzR22hAIUB3o-92rcAsyRItUtse6eBz
- **Lab ShockDesk :** https://github.com/Calvin29990/shockdesk
- **Lab exotiques :** https://github.com/Calvin29990/calvin-exotic-desk

## 🔑 Chiffres d'or (provenance yfinance — jamais le synthétique)

```
yfinance · shock-lab-oil · 25,5 M$ · 2026-07-01 → 2026-08-29 · 42 barres
pic J+7 = +337 887 $ · stop J+21 = −279 633 $ · timing = 617 520 $
or = +53,0 k$ (PAS un miss) · misses = HYG, TLT · Brent ×3,68
```

## 🛠️ Régénérer le PDF

```bash
python3 -m venv .venv
.venv/bin/pip install fpdf2 matplotlib
.venv/bin/python tools/md2pdf.py 00-programme-elite-2026.md programme-elite-2026.pdf
```
