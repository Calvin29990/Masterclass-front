# FX — boucher le trou en 40 minutes

> Tu t'es fait avoir sur une question FX. Normal : **le FX n'est presque pas
> dans les 14 premiers chapitres du Hull.** Il y est traité en une section
> (5.10) et un bout du chapitre 17. Un ex-stagiaire sales qui te dit « connais
> les 14 premiers chapitres » et qui t'interroge sur le FX te teste sur quelque
> chose que ces 14 chapitres **ne couvrent pas**.
>
> Ce document contient ce qu'il te manquait. C'est court parce que le FX de
> base **est** court.

---

## 1. Lire une paire — le réflexe qui manque à 90 % des candidats

`EUR/USD = 1,0850`

- **EUR = la base.** USD = la contrepartie (*quote currency*).
- Ça veut dire : **1 euro s'achète 1,0850 dollar.**
- Le prix est **toujours** exprimé en unités de contrepartie pour une unité de base.

**« Acheter EUR/USD »** = acheter des euros, vendre des dollars. Si le chiffre
monte, tu gagnes.

> 🔑 **Le piège classique en entretien.** « EUR/USD baisse de 1,0850 à 1,0800 :
> le dollar est-il plus fort ou plus faible ? »
> → **Plus fort.** Il faut moins de dollars pour un euro, donc le dollar s'est
> apprécié. Le chiffre baisse, la devise de **contrepartie** se renforce.
> La moitié des candidats se trompe ici.

### Le pip

Un **pip** = la dernière décimale de la cotation standard.

| Paire | Cotation | 1 pip | Valeur d'1 pip sur 1 M de base |
|---|---|---|---|
| EUR/USD | 1,0850 | 0,0001 | **100 USD** |
| USD/JPY | 155,20 | 0,01 | **64,43 USD** |

> ⚠️ **Le JPY est l'exception** : 2 décimales, pas 4. Et la valeur du pip d'une
> paire en `USD/xxx` dépend du niveau du taux — d'où les 64,43 et pas 100.

---

## 2. Le forward FX — LA formule qu'on te demandera

C'est **la** question FX d'entretien. Elle a un nom : **la parité des taux
d'intérêt couverte** (*covered interest rate parity*, CIP).

$$F = S \times \frac{1 + r_{\text{contrepartie}} \times T}{1 + r_{\text{base}} \times T}$$

**En version continue** (celle du Hull, chapitre 5.10) :

$$F = S e^{(r_{\text{contrepartie}} - r_{\text{base}})T}$$

### L'exemple à savoir refaire

`EUR/USD spot = 1,0850` · taux USD 4,25 % · taux EUR 2,25 % · **3 mois**

$$F = 1{,}0850 \times \frac{1 + 0{,}0425 \times 0{,}25}{1 + 0{,}0225 \times 0{,}25} = 1{,}090395$$

**Soit +53,9 pips.** (En continu : 1,090439, soit +54,4 pips. L'écart est du
bruit, personne ne te chicanera là-dessus.)

### 🧠 Le calcul mental que tu dois savoir faire en 5 secondes

> **Points de forward ≈ spot × (écart de taux) × (durée en années) × 10 000**
>
> Ici : 1,0850 × 2 % × 0,25 = 0,00543 → **+54 pips**. Fait de tête.

**Dis-le comme ça en entretien :** *« The rate differential is two percent,
over three months that's fifty basis points, on a spot of one oh eight fifty
that's about fifty-four pips. So EUR/USD three-month forward trades around one
oh nine oh. »*

### Pourquoi c'est comme ça — la seule justification à donner

**Parce que sinon il y a un arbitrage sans risque.** Tu empruntes des euros à
2,25 %, tu les changes au comptant, tu places les dollars à 4,25 %, et tu
verrouilles le taux de reconversion aujourd'hui. Si le forward n'est pas
exactement à ce niveau, tu encaisses la différence sans prendre de risque.

> 🎯 **Le focus qui fait la différence.** Comme pour le forward action :
> **le forward FX n'est pas une prévision du taux futur.** C'est du **cost of
> carry**, point. Si un intervieweur te dit « le forward est à 1,0904, donc le
> marché anticipe une hausse de l'euro » — **c'est faux**, et le lui dire
> proprement te fait gagner l'entretien.
>
> *« That's not a forecast, that's just the interest rate differential. The
> forward is where you can transact today, not where the market thinks spot
> will be. »*

---

## 3. La règle de la devise forte — à connaître par cœur

> **La devise au taux d'intérêt le plus élevé cote en déport (*at a discount*)
> à terme. La devise au taux le plus bas cote en report (*at a premium*).**

Ici le USD paye plus que l'EUR → le dollar est **en déport**, donc plus faible
en forward : il faut 1,0904 USD pour un euro à trois mois, contre 1,0850
aujourd'hui. Symétriquement, l'euro cote **en report** contre dollar.

> 🧠 **Le moyen mnémotechnique.** *Déport* contient *dé*, comme *décote*. La
> devise qui paye le plus cher aujourd'hui vaut moins cher demain — sinon on
> encaisserait le taux ET la devise, ce qui serait de l'argent gratuit.

**Le raccourci mental :** le marché te reprend en forward ce que le taux
d'intérêt te donne. Sinon, argent gratuit.

---

## 4. Le carry trade — la question qui suit toujours

**Question type :** *« Si le dollar paye 4,25 % et l'euro 2,25 %, pourquoi ne
pas juste emprunter en euro et placer en dollar ? »*

**Réponse :** Parce que **couvert**, ça ne rapporte rien — le forward mange
exactement l'écart (c'est la CIP ci-dessus). Le carry trade n'est rentable que
**non couvert**, et là tu portes le risque de change en entier.

$$\text{PnL carry} = \underbrace{(r_{USD} - r_{EUR}) \times T}_{\text{le carry, certain}} + \underbrace{\Delta S}_{\text{le change, incertain}}$$

Sur 3 mois : le carry te rapporte 0,50 %, soit **54 pips**. Une variation de
spot de 54 pips (0,5 %) suffit à tout effacer.

> 🎯 **La phrase qui montre que tu comprends le métier :**
> *« Carry trades pick up pennies in front of a steamroller. You collect fifty
> basis points a quarter and you can lose three percent in a morning. That's why
> they unwind violently — everyone is on the same side. »*

---

## 5. Le cross — le calcul qu'on fait au tableau

Tu n'as pas EUR/JPY coté ? Tu le reconstruis.

`EUR/USD = 1,0850` · `USD/JPY = 155,20`

$$EUR/JPY = 1{,}0850 \times 155{,}20 = \mathbf{168{,}392}$$

**La règle :** quand la devise commune (`USD`) est en **contrepartie** de la
première et en **base** de la seconde, **tu multiplies**. Sinon tu divises.

> 🔑 **Le contrôle de bon sens.** 1 euro vaut ~1,09 dollar, 1 dollar vaut
> ~155 yens, donc 1 euro vaut ~1,09 × 155 ≈ 168 yens. **Si ton résultat n'a pas
> l'ordre de grandeur du bon sens, tu t'es trompé de sens.** Fais ce contrôle à
> voix haute en entretien, ça montre de la rigueur.

---

## 6. Les 8 mots de vocabulaire FX

| EN | FR | Ce que ça veut dire |
|---|---|---|
| **spot** | comptant | Livraison à J+2 |
| **the base currency** | la devise de base | Celle de gauche, celle qu'on achète |
| **a pip** | un pip | Dernière décimale (0,0001 sauf JPY) |
| **forward points** | les points de terme | L'écart forward − spot, en pips |
| **a swap point** | un point de swap | Même chose, langage desk |
| **at a premium** | en report | Le forward est au-dessus du spot |
| **at a discount** | en déport | Le forward est en dessous du spot |
| **a cross** | un cross | Paire sans USD (EUR/JPY, EUR/GBP) |

---

## 7. Les 5 questions qu'on va te poser

**Q1. EUR/USD passe de 1,0850 à 1,0800. Que fait le dollar ?**
→ Il **se renforce**. Moins de dollars pour un euro.

**Q2. Spot 1,0850, USD 4,25 %, EUR 2,25 %, 3 mois. Le forward ?**
→ **≈ 1,0904**, +54 pips. *« Rate differential two percent, quarter of a year,
fifty-four pips. »*

**Q3. Pourquoi le forward est-il au-dessus du spot ?**
→ Parce que le **dollar paye plus**. Le marché reprend en forward ce que le
taux donne, sinon il y a arbitrage. **Ce n'est pas une prévision.**

**Q4. Le forward me dit-il où sera le spot dans 3 mois ?**
→ **Non.** C'est du cost of carry. La meilleure prévision du spot futur reste
le spot d'aujourd'hui (marche aléatoire).

**Q5. EUR/USD 1,0850, USD/JPY 155,20 : EUR/JPY ?**
→ **168,39.** On multiplie, l'USD s'annule.

---

## Ce que tu fais maintenant

1. **Refais l'exemple 1,0850 à la main**, sur papier, sans regarder. Deux fois.
2. **Apprends le raccourci mental** : spot × écart de taux × durée × 10 000.
3. **Retiens la phrase sur le forward qui n'est pas une prévision.** C'est la
   même idée qu'à la question 24 de ta fiche entretien — tu la connais déjà pour
   les actions, elle est **identique** en FX.

> Tu viens de boucher le trou. Ça t'a pris 40 minutes, pas 14 chapitres.
