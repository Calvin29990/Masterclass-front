# Cours rédigés — un fichier par jour

Chaque cours est autoportant : démonstrations complètes, TD corrigé et vérifié
en Python, oraux FR/EN, pièges, flashcards, ticket de sortie. On avance
**cours par cours**, jamais en avance : le fichier du jour J n'est écrit que le
jour J.

| Jour | Date | Fichier | Livrable Python | État |
|---|---|---|---|---|
| **M0** | **06/09** | [**`M0-rappels-maths.md`**](M0-rappels-maths.md) — **à lire en premier si les maths sont rouillées** | — | ✅ 8 modules + exos |
| — | 06/09 | [`PLAN-rattrapage-06-09.md`](PLAN-rattrapage-06-09.md) | — | ✅ planning révisé |
| J1 | 05/09 | [`J01-parite-forward-black-scholes.md`](J01-parite-forward-black-scholes.md) | `livrables/j01_bs_closed_form.py` | ✅ écrit, tests OK |
| J2 | 07/09 | `J02-grecs.md` | `livrables/j02_greeks.py` | à écrire |
| J3 | 08/09 | `J03-structures.md` | `livrables/j03_payoffs.py` | à écrire |
| … | … | (voir `01-programme-elite-05-30-septembre-2026.md`) | | |

## Par où commencer

1. **Maths rouillées ?** → [`M0-rappels-maths.md`](M0-rappels-maths.md)
   (1 h 30). Huit modules courts, micro-exercices corrigés, uniquement ce qui
   sert au J1. Aucune honte : c'est un problème d'outillage, pas de niveau.
2. **Sinon** → directement [`J01`](J01-parite-forward-black-scholes.md).
3. Les blocs 🧮 dans le J1 renvoient au module M0 correspondant.

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

- [`PLAN-10-au-16-09.md`](PLAN-10-au-16-09.md) — plan allégé de la semaine event (1 h/jour : 20 min anglais + 40 min cours). Reprise du programme J2 le 16/09.
- [`COURS-URGENCE-2H.md`](COURS-URGENCE-2H.md) — **cours d'urgence FIC en 2 h** : 6 blocs (taux, obligations, dérivés fermes, options, vol, crédit/FX), images mentales + chiffres, 12 questions de contrôle. [PDF](COURS-URGENCE-2H.pdf)
- [`HULL-francais-comment-y-acceder.md`](HULL-francais-comment-y-acceder.md) — le Hull en français (Pearson 11e éd.) : accès ScholarVox SKEMA gratuit, chapitre 1 offert, lexique EN→FR de 40 termes, plan de lecture 4 jours avec pages exactes.
- [`FX-le-trou-a-boucher.md`](FX-le-trou-a-boucher.md) — le FX en 40 min : lire une paire, pips, forward FX (CIP) avec le calcul mental, report/deport, carry trade, cross, 8 mots de vocabulaire et les 5 questions d'entretien. Comble le trou que les 14 premiers chapitres du Hull ne couvrent pas.
