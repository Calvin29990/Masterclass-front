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
- [`URGENCE-marche-du-jour-12-09.md`](URGENCE-marche-du-jour-12-09.md) — le marche au 11/09/2026 pour l'appel CACIB eFX : regime de hausse des taux, CPI US, indices, et un bloc Bresil complet (Selic 14 %, carry de 10,4 points, NDF/PTAX, forward USD/BRL). 6 questions avec reponses.
- [`APRES-SIMULATION-les-3-trous.md`](APRES-SIMULATION-les-3-trous.md) — correctif cible apres le debrief Gemini : correlation petrole/devises EM en deux canaux, carry brésilien chiffre avec point mort et vol, skew et risk reversal, et la reponse eFX a apprendre par coeur. Plus le lexique du desk eFX.
- [`COURS-eFX-bilingue-1h.md`](COURS-eFX-bilingue-1h.md) — **le cours a lire avant la prochaine simulation**. 1 h, bilingue FR/EN : metier eFX et internalisation, bases FX, le carry explique de zero avec ses trois pieges, focus Bresil (NDF, PTAX, Copom, skew), actualite CACIB (Best Asia NDF House, +200 % de volumes), les 3 points de profil a placer, les 7 pieges et 10 questions avec reponses.
- [`POSTURE-sales-le-dernier-cran.md`](POSTURE-sales-le-dernier-cran.md) — apres la 2e simulation, ou les trous techniques ont disparu : refonte de la presentation avec le Bresil en ouverture, comment parler de Python sans sonner quant, la bonne reponse sur les RFQ chiffree, 5 reflexes de langage et la question de fin creusee.
- [`SELIC-NDF-et-le-vrai-sujet-Python.md`](SELIC-NDF-et-le-vrai-sujet-Python.md) — les deux definitions manquantes : la Selic (taux directeur bresilien, leur Fed funds) et le NDF (forward sans livraison regle en dollars contre le fixing PTAX), plus la correction du conseil sur Python, qui est un atout a revendiquer et non a cacher.
- [`POSITIONNEMENT-ce-quon-raconte.md`](POSITIONNEMENT-ce-quon-raconte.md) — **a lire avant tout entretien** : pourquoi aucune attache personnelle a une region n'entre dans le recit (risque d'assignation a un desk regional), l'asymetrie entre un oral d'ecole et un entretien bancaire, l'interdiction definitive de l'echange au Bresil invente, et quoi repondre si on pose la question directement.
- [`FX-LATAM-cours-complet.md`](FX-LATAM-cours-complet.md) — **LE cours, six heures, autonome et sans prerequis**. Vocabulaire de zero, douze dates de Bretton Woods au CNH, tous les produits dont le NDF et les options, les strategies carry et couverture corporate, le LatAm pays par pays, le Bresil en profondeur avec Selic PTAX B3 cupom cambial dette et courbe des taux, le langage du metier et huit exercices corriges.
- [`BIBLIOTHEQUE-scholarvox-plan-de-lecture.md`](BIBLIOTHEQUE-scholarvox-plan-de-lecture.md) - quels livres lire sur ScholarVox SKEMA, dans quel ordre, et lesquels eviter. Planning 5 jours.
- [`PIVOT-FX-sales-France.md`](PIVOT-FX-sales-France.md) — **la decision de recentrage, a lire en premier**. Pourquoi le right to work sort les stages londoniens du jeu, la carte des desks FX en France, ce qui change entre l'eFX londonien et le FX Sales corporate parisien, ce qui ne change pas dans le socle technique, le discours ferme avec la reponse si on demande pourquoi pas Londres, le message a Ali, la reformulation de ShockDesk en langage risque et trois sujets d'articles.
- [`ACTU-banque-par-banque-2026.md`](ACTU-banque-par-banque-2026.md) — **le dossier d'actualite, environ deux heures de lecture**. Comment lire les resultats d'une banque de marche, tableau comparatif des cinq maisons au deuxieme trimestre 2026, une section detaillee par banque avec plateforme et algorithmes, la lecture transversale sur la fracture du FICC europeen, les cinq pieges a eviter, huit exercices corriges et une fiche de revision de dix minutes.
- [`LATAM-ta-specialisation.md`](LATAM-ta-specialisation.md) — **le recit officiel** : le FX latino-americain electronique. Livrable contre non livrable (MXN / BRL, COP, CLP), carry compare, calcul des points de terme USD/MXN, pourquoi le desk LatAm est a Londres, pourquoi Suzhou reste dehors, et 5 exercices corriges.
