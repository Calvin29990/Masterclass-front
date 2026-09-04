# Reprise Masterclass Front — contexte pour l'IA (Arena / Gemini)

> À coller en tête d'une **nouvelle conversation** pour reprendre sans perdre le fil.

---

## 1. Qui, quoi, pourquoi

- **Candidat :** Calvin (SKEMA). Objectif : passer un **Superday Front Office**
  (S&T / dérivés / structurés / junior trader dérivés).
- **Ce dépôt** (`Calvin29990/Masterclass-front`) = le **cerveau du mois** : le
  programme, les livrables Python quotidiens, la fiche de suivi, la mémoire de
  recherche. Ce n'est **pas** ShockDesk.
- **Lab séparé :** `Calvin29990/shockdesk` (le simulateur backtest/options) +
  `Calvin29990/calvin-exotic-desk`. ShockDesk a ses **onglets réels** ; ne pas
  inventer d'onglets ALM / Risk / galerie d'autocalls.
- **Drive source (61/61 fichiers) :**
  https://drive.google.com/drive/folders/1NdzR22hAIUB3o-92rcAsyRItUtse6eBz
  (aucun livre dans le repo — droits ; le catalogue `02-catalogue-drive.md`
  porte tous les liens).

## 2. Le sprint

- **Période :** 5 → 30 septembre 2026 (22 jours, 6 h/jour). Aujourd'hui de
  référence du pack = **J1 samedi 05/09** ; fin = **mercredi 30/09**.
- **Desk visé (un seul) :** n°1 Equity derivatives / produits structurés ;
  n°2 rates/ALM/repo ; n°3 commo pétrole + coton.
- **Périmètre :** 100 % du Drive, zéro notion hors Drive. **Stage en pause**
  jusqu'au 30/09 (une candidature = faute `F`).
- **4 blocs :** A vanilles (5–11) · B exotiques (12–18) · C taux/ALM/repo/commo
  (19–25) · D quant/risque/synthèse (26–30).
- **3 trade ideas :** 11/09 Oil timing · 18/09 Structuré Phoenix/collar ·
  25/09 Rates 2s10s **ou** coton WASDE.
- **Vendredis :** mini-Superday 45 min enregistrées (11, 18, 25, 30).

## 3. Règles non négociables

1. **Livrable Python absent → jour non clos.** Chaque script imprime sa
   **provenance** en docstring (Drive fichier + page, ou run ShockDesk). Un
   nombre sans source = script refusé.
2. **Dimanche off annulé** si un ticket de sortie de la semaine est rouge.
3. **Jamais les chiffres synthétiques.** Uniquement les chiffres **yfinance**
   (voir §5). Un recruteur qui clone et lance sous Yahoo ne retrouve pas les
   chiffres du générateur synthétique — c'est disqualifiant.
4. **Pas d'onglet inventé** dans ShockDesk/exotic-desk. On dit « je ne l'ai
   pas », jamais on le promet.
5. **Bilingue FR/EN** sur chaque oral (90 s + 90 s, debout, minuterie).

## 4. Structure du dépôt

```
README.md                    ← page d'accueil du repo
REPRISE-CONTEXTE.md          ← ce fichier
00-programme-elite-2026.md   ← programme amélioré (source du PDF)
programme-elite-2026.pdf     ← PDF à mettre dans le Drive
01-programme-elite-05-30-septembre-2026.md   ← programme original (gelé)
02-catalogue-drive.md        ← les 61/61 fichiers Drive, jour d'emploi
03-octobre-base-recherche.md ← ce qu'on ne fait PAS en septembre (vivant)
04-fiche-suivi.md            ← cases à cocher + bloc du jour à recoller
05-nettoyage-github.md       ← audit des 4 dépôts
06-ecarts-vs-ebauche.md      ← pourquoi l'ébauche 4 h ne tient pas
livrables/                   ← 21 scripts (un par jour, à partir de J1)
recherche/                   ← mémoire ShockDesk (journal, carnet, roadmap)
suivi/                       ← suivi daté
tools/md2pdf.py              ← générateur Markdown → PDF (fpdf2)
```

## 5. Chiffres d'or (à recoller si on te dit que tes refs sont fausses)

```
yfinance · shock-lab-oil · 25,5 M$ · 2026-07-01 → 2026-08-29 · 42 barres
pic J+7 = +337 887 $ · stop J+21 = −279 633 $ · timing = 617 520 $
or = +53,0 k$ (PAS un miss) · misses = HYG, TLT · Brent ×3,68
```

Détail (sortie pic J+7 / stop J+21) : Brent +187,1 k$ / −117,5 k$ · S&P short
+82,0 k$ / −213,4 k$ · Or +53,0 k$ / +107,2 k$ · signe net 4/6 · Brent
réalisé +18,4 % vs prévu +5 % → **×3,68**.

Repères options ShockDesk (Atelier 5/7, mesurés 30/08) : straddle vs strangle
prime ×2,3 (24,40 vs 10,69) · choc IV +10 pts → prime 10,69 → 23,91, vega
1,242 → 1,374, theta −0,344 → −0,608 · à +18,4 % le straddle gagne *par
structure*, le strangle *par dollar* (×2,13) · `MIN_EDGE` 0,52 < 1,00 → 0 trade.

## 6. Reprendre une journée

Dans le chat, coller le bloc de `04-fiche-suivi.md` :

```
JOUR : J__  DATE : __/09  MODE : E / C / F
FAIT : cours[ ] td[ ] lab[ ] oral[ ] brain[ ] py[ ]
TICKET : oui / non — détail :
REDTES :
CHIFFRE DU JOUR (provenance) :
QUESTION POUR LA SESSION :
```

Le détail de chaque jour (Drive P/S, consignes par bloc, ticket de sortie) est
dans `00-programme-elite-2026.md` (ou le PDF).

## 7. Régénérer le PDF

```bash
python3 -m venv .venv
.venv/bin/pip install fpdf2 matplotlib
.venv/bin/python tools/md2pdf.py 00-programme-elite-2026.md programme-elite-2026.pdf
```

`tools/md2pdf.py` rend **gras**, *italique*, `code`, tableaux, listes,
citations et blocs de code ; la couverture se pilote par des commentaires
`<!-- subtitle / date / meta -->` en tête du `.md`.

## 8. Bloc de reprise (prêt à coller)

```
Reprise masterclass FO. Lis REPRISE-CONTEXTE.md puis 00-programme-elite-2026.md.
Aujourd'hui = J__ (date __/09). Drive = 100 %, zéro notion hors Drive.
Stage en pause. ShockDesk = lab, pas ce repo.
Chiffres : yfinance · shock-lab-oil · 25,5 M$ · 42 barres · +337 887 / −279 633 ·
timing 617 520 · or +53,0 k$ · misses HYG/TLT · Brent ×3,68.
```
