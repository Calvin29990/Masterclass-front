# Cours rédigés — un fichier par jour

Chaque cours est autoportant : démonstrations complètes, TD corrigé et vérifié
en Python, oraux FR/EN, pièges, flashcards, ticket de sortie. On avance
**cours par cours**, jamais en avance : le fichier du jour J n'est écrit que le
jour J.

| Jour | Date | Fichier | Livrable Python | État |
|---|---|---|---|---|
| J1 | 05/09 | [`J01-parite-forward-black-scholes.md`](J01-parite-forward-black-scholes.md) | `livrables/j01_bs_closed_form.py` | ✅ écrit, tests OK |
| J2 | 07/09 | `J02-grecs.md` | `livrables/j02_greeks.py` | à écrire |
| J3 | 08/09 | `J03-structures.md` | `livrables/j03_payoffs.py` | à écrire |
| … | … | (voir `01-programme-elite-05-30-septembre-2026.md`) | | |

## Convention de rédaction

1. **Provenance obligatoire.** Chaque cours cite les fichiers Drive (P et S) du
   jour, et chaque script imprime sa provenance en docstring.
   *Un chiffre sans provenance n'est pas un chiffre.*
2. **Démonstrations complètes.** Pas de « on montre que » : les étapes sont
   écrites, numérotées, refaisables au crayon.
3. **Trois marqueurs** dans le texte :
   - 🎤 **Oral** → la phrase exacte à sortir en entretien (FR et EN) ;
   - ⚠️ **Piège** → l'erreur qui coûte le Superday ;
   - tableaux de signes / flashcards → mémorisation.
4. **Tous les chiffres du TD sont recalculés** par le livrable Python du jour.
   Si le script échoue, le cours est faux, pas l'inverse.

## Rendu des formules

Les fichiers utilisent LaTeX (`$...$` et `$$...$$`). Pour un rendu correct :
GitHub (natif), VS Code + *Markdown Preview Enhanced*, Obsidian, ou :

```bash
pandoc cours/J01-parite-forward-black-scholes.md -o J01.pdf --pdf-engine=xelatex
```
