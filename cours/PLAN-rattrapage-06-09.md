# Rattrapage — dimanche 06/09/2026

## D'abord : ce n'est pas grave

Tu as pris du retard sur J1 parce que les maths sont rouillées. **C'est un
problème d'outillage, pas de niveau.** Un mois de préparation qui ne rencontre
aucun mur, c'est un mois mal calibré.

Le programme prévoyait « dimanche off ». On l'utilise pour **remettre les
outils en place**, ce qui est un bien meilleur usage qu'un jour de repos que tu
passerais à ruminer J1.

**Ce qui change dans le pack :**
- ajout de [`M0-rappels-maths.md`](M0-rappels-maths.md) — 8 modules, **~110 exercices corrigés** en séries A/B/C, plus un exercice de synthèse qui reconstruit $d_1$ et $d_2$ ;
- le §0.1 du J1 (ta capture) commence maintenant par **un tableau de chiffres
  sans aucune formule**, la formule ne vient qu'après ;
- six renvois 🧮 dans le J1 pointent vers le module M0 correspondant.

**Ce qui ne change pas :** le contenu du J1. Tu ne perds pas une ligne de
programme, tu ajoutes une rampe d'accès.

---

## Le planning d'aujourd'hui (3 h 30, pas 6 h)

| Bloc | Durée | Quoi | Pourquoi |
|---|---|---|---|
| 1 | **1 h 45** | [`M0`](M0-rappels-maths.md) modules **M1 → M4** + **toutes** leurs séries d'exercices | exp, log, dérivées, DL, la limite $e^{rT}$ |
| 2 | **0 h 20** | pause réelle, sans écran | consolidation |
| 3 | **1 h 00** | J1 **§0 et §1** (briques + forwards) | maintenant lisible |
| 4 | **0 h 40** | TD **exercices 1 à 4** au papier | forwards uniquement |

**Tu t'arrêtes là.** Tu ne touches ni à Black-Scholes, ni aux grecs
aujourd'hui.

> **Pourquoi couper J1 en deux ?** Parce que le §1 (forwards) ne demande que
> M1, et que le §4 (Black-Scholes) demande M5, M6, M7. Les enchaîner le même
> jour quand les maths sont froides, c'est se garantir un mur. Séparés, chaque
> moitié est faisable.

---

## Demain lundi 07/09 (5 h 30)

| Bloc | Durée | Quoi |
|---|---|---|
| 0 | 0 h 15 | Mental math (Optiver) — **dès demain, pas le 26** |
| 1 | 0 h 45 | M0 modules **M5 → M8** |
| 2 | 1 h 30 | J1 **§2, §3, §4** (parité, bornes, les 3 démos de BS) |
| 3 | 0 h 45 | J1 **§5, §6** (lecture du modèle, grecs) |
| 4 | 0 h 45 | TD **exercices 5 à 7** + `python3 livrables/j01_bs_closed_form.py --td` |
| 5 | 0 h 45 | Oral WORDS §8.3 + ticket de sortie J1 |
| 6 | 0 h 30 | Lab ShockDesk §8.1 |

**J1 est clos lundi soir.** J2 (grecs) glisse à mardi 08/09.

---

## Impact sur le mois : aucun, si on absorbe ici

Le programme a **22 jours pour 22 sessions**, avec 4 dimanches off. En
consommant le dimanche 06 et en décalant d'un jour, on absorbe le retard
**sans toucher aux blocs B, C, D**.

| | Prévu | Révisé |
|---|---|---|
| J1 parité/BS | 05/09 | **05 → 07/09** (étalé) |
| J2 grecs | 07/09 | **08/09** |
| J3 structures | 08/09 | **09/09** |
| … | | glissement de 1 jour |
| Fin bloc A | 11/09 | **12/09** |

Le bloc B commençait le 12/09 (samedi) : on récupère le décalage sur le
dimanche 13, qui devient une demi-journée. **À partir du 14/09, on est
recalé.**

> **Règle à ne pas violer :** on ne rattrape jamais en sautant les
> démonstrations. On rattrape en réduisant les blocs C (lab) et D (marché),
> qui sont importants mais pas éliminatoires en Superday. Le cours et le TD ne
> se compriment pas.

---

## Comment lire un passage qui bloque (méthode, 4 étapes)

À appliquer chaque fois qu'une ligne te résiste — c'est une compétence, pas un
réflexe naturel :

1. **Identifie le type de blocage.** Notation inconnue ? étape de calcul
   sautée ? ou concept ? Les trois se soignent différemment. Le plus souvent
   c'est la **notation** — et ça se règle en 30 secondes avec M0.
2. **Cherche le chiffre.** Presque tout le J1 a un exemple numérique. Fais
   tourner l'exemple : le sens vient souvent **avant** la démonstration.
3. **Lis la conclusion d'abord**, la preuve ensuite. Savoir *où on va* rend une
   démonstration deux fois plus facile.
4. **Time-box : 10 minutes.** Passé ce délai, tu notes la ligne dans le bloc
   ci-dessous et tu **continues**. Rester bloqué 40 min sur une ligne, c'est
   perdre une session.

```
LIGNES BLOQUANTES (à me transmettre)
- § ____ ligne « ____________________ »  → type : notation / calcul / concept
- § ____ ligne « ____________________ »  → type :
```

Envoie-moi ce bloc : je réécris **le passage exact**, pas tout le cours.

---

## Ce que je veux comme retour ce soir

Trois lignes suffisent :

```
M0 : modules faits ___  / exercices ratés (numéros) : ___
     auto-test ___/10
J1 : §0 [ ]  §1 [ ]  TD ex.1-4 [ ]
BLOQUÉ SUR :
```

**Donne-moi les numéros d'exercices ratés**, pas seulement « j'ai eu du mal ».
Un exercice raté est une information précise : je réécris le rappel
correspondant.

Et honnêtement : **si M0 seul te prend les 3 h 30, c'est un bon dimanche.**
Le J1 tiendra lundi. Ce qui compte au 30/09 n'est pas d'avoir coché 22 cases,
c'est de savoir dériver la parité et l'EDP sans notes — et ça se construit
exactement comme tu es en train de le faire.
