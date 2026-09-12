# Cours eFX bilingue — 1 heure avant la simulation

> **À lire d'une traite, à voix haute pour les passages en anglais.**
> On part de zéro sur le carry. Chaque section finit par ce qu'il faut savoir
> dire. Les chiffres sont ceux du 11 septembre 2026 — **revérifie-les le jour J**.
>
> **Plan :** 1. Le métier · 2. Les bases FX · 3. Le carry expliqué de zéro ·
> 4. Le Brésil · 5. CACIB · 6. Ton profil · 7. Les pièges · 8. Q/R

---

# 1. Le métier d'eFX Sales — ce que fait Romain

## L'idée en une phrase

> Avant, un client qui voulait acheter 50 M EUR/USD **appelait** un sales.
> Aujourd'hui il clique sur un écran, et **un algorithme répond en 20
> millisecondes**. L'eFX, c'est ce basculement.

## Ce que le desk gagne

Le desk **cote un prix à l'achat et à la vente**, et gagne l'écart.

> 0,5 pip sur 10 M EUR/USD = **500 USD**. Ça paraît peu. Multiplié par des
> milliers de tickets par jour, c'est le modèle.

**Le point crucial, et c'est le cœur du métier :**

| Modèle | Ce que fait le desk | Marge |
|---|---|---|
| **Externalisation** | Le client achète, le desk va racheter sur le marché interbancaire | Faible — il paye lui-même un spread |
| **🔑 Internalisation** | Le client A achète, le client B vend. Le desk **matche les deux en interne** | Forte — il encaisse les deux spreads sans rien payer |

> **L'internalisation est LE sujet d'un desk eFX.** Plus tu internalises, plus
> tu gagnes. C'est pour ça que les banques veulent du **volume** et du **flux
> diversifié**.

## Le vocabulaire du desk — à connaître absolument

| EN | FR | Ce que ça veut dire vraiment |
|---|---|---|
| **RFQ** *(request for quote)* | demande de cotation | Le client demande un prix ferme |
| **streaming** | prix en continu | Le desk diffuse un prix permanent, sans qu'on demande |
| **hit ratio** | taux de réussite | Part des RFQ gagnées face aux banques concurrentes |
| **to internalise flow** | internaliser le flux | Matcher les clients entre eux |
| **franchise flow** | flux de franchise | Le flux client récurrent, par opposition au risque pris |
| **to skew a price** | décaler un prix | Coter plus agressif d'un côté pour attirer le flux qu'on veut |
| **last look** | last look | Droit de refuser un ordre après l'avoir affiché |
| **spread capture** | captation de spread | Ce que le desk garde sur le bid-ask |
| **a fixing** | un fixing | Cours de référence officiel (**PTAX** au Brésil) |
| **market impact** | impact de marché | De combien le marché bouge contre toi quand tu exécutes |

## Les plateformes à citer

**Multi-dealer :** FXall (LSEG) · 360T (Deutsche Börse) · Bloomberg FXGO
**Algos d'exécution :** TWAP · VWAP · POV
**Connexion directe :** API en protocole **FIX**

> 🎯 **La question de pro à poser à Romain :**
> *« Quelle part de votre flux vous arrivez à internaliser ? »*
>
> Tu touches directement au modèle économique. Personne d'autre ne pose ça.

---

# 2. Les bases FX — le strict nécessaire

## Lire une paire

`EUR/USD = 1,1610` → **1 euro s'achète 1,1610 dollar.** EUR = base, USD =
contrepartie.

> ⚠️ **Le piège où tombe la moitié des candidats.** EUR/USD baisse de 1,1610 à
> 1,1550 : **le dollar se renforce**. Moins de dollars pour un euro.

## Le pip

| Paire | 1 pip | Valeur sur 1 M |
|---|---|---|
| EUR/USD | 0,0001 | 100 USD |
| USD/JPY | **0,01** ⚠️ | 64 USD |
| USD/BRL | 0,0001 | 100 BRL ≈ 19 USD |

## Le forward — la formule unique

$$F = S \times \frac{1 + r_{\text{contrepartie}} \times T}{1 + r_{\text{base}} \times T}$$

**Le calcul mental :** points ≈ spot × écart de taux × durée × 10 000.

> **La devise au taux le plus élevé cote en déport (*at a discount*).**
> Mnémotechnique : *déport* comme *décote*. Qui paye plus aujourd'hui vaut
> moins demain — sinon on encaisserait le taux **et** la devise.

## 🔑 Le point le plus rentable de tout ce cours

> **Le forward n'est PAS une prévision.** C'est du **cost of carry**.
>
> 🇬🇧 *« The forward isn't a forecast — it's just the interest rate
> differential. It's where you can transact today, not where the market thinks
> spot will be. »*

Si un intervieweur affirme le contraire et que tu le reprends **poliment**, tu
gagnes l'entretien. C'est le test classique.

---

# 3. Le carry trade — de zéro

## L'idée, avec des mots simples

> Tu empruntes dans une devise où l'argent **coûte peu**. Tu places dans une
> devise où l'argent **rapporte beaucoup**. Tu encaisses la différence.

Aujourd'hui : emprunter en dollar à **3,625 %**, placer en réal à **14,00 %**.

$$\text{Carry} = 14{,}00 - 3{,}625 = \mathbf{10{,}4 \text{ points par an}}$$

**Sur 1 M USD pendant 3 mois : environ 25 900 USD encaissés.**

## Le piège n°1 : couvert, ça ne rapporte RIEN

C'est **la** chose à comprendre, et c'est contre-intuitif.

Si tu te couvres avec un forward, tu vends tes réaux à terme à **5,2926** au
lieu de 5,16. Tu perds **1 326 pips** — qui valent **exactement le carry**.

> **Le marché reprend en forward ce que le taux d'intérêt donne.** Sinon ce
> serait de l'argent gratuit, et l'arbitrage le ferait disparaître.
>
> 🇬🇧 *« Covered, the carry is zero by construction. The whole trade is the
> uncovered bet. »*

**Donc : le carry trade n'existe que NON COUVERT.** Tu prends tout le risque de
change.

## Le piège n°2 : le point mort

Carry 3 mois = **2,5 %**. Spot à 5,16. Ton point mort :

$$5{,}16 \times 1{,}025 = \mathbf{5{,}29}$$

> **Si l'USD/BRL monte de plus de 2,5 % en trois mois, tu perds — malgré
> 10 points de carry.**

Et la vol du réal est de **13 % annualisé**, soit **0,82 % par jour**.

> 🎯 **La phrase à dire, elle vaut de l'or :**
> *« Trois séances à un écart-type effacent un trimestre de portage. »*
>
> 🇬🇧 *« Three months of Brazilian carry is two and a half percent. Daily vol
> on the real is eighty basis points. So three standard-deviation days wipe out
> a full quarter of carry. That's why people say carry trades pick up pennies
> in front of a steamroller. »*

## Le piège n°3 : tout le monde est du même côté

Un carry trade rentable attire **tout le monde**. Quand ça se retourne, tout le
monde sort **en même temps** — d'où des mouvements violents et non linéaires.

> **Le carry ne meurt pas lentement. Il meurt d'un coup.** Souviens-toi du
> débouclage du carry sur le yen.

## Ce qu'il faut retenir en 4 lignes

1. Emprunter bas, placer haut, encaisser l'écart
2. **Couvert = zéro.** Le forward mange exactement le carry
3. Le point mort est proche : 3 jours de vol = 1 trimestre de carry
4. Ça se déboucle **violemment**, parce que le positionnement est unanime

---

# 4. 🇧🇷 Le Brésil — ton angle

## Les chiffres

| | Niveau |
|---|---|
| **USD/BRL** | **5,16** |
| EUR/BRL | 5,95 |
| **Selic** | **14,00 %** |
| Taux réel | **~9 %** |
| Ibovespa | ~172 500 (**+26 % sur 1 an**) |
| Brent | ~105 USD |

## Le NDF — le concept qui te distingue

Le réal **n'est pas librement convertible**. On ne peut pas livrer des réaux à
Londres. Donc tout se traite en **NDF** :

> Un **non-deliverable forward** est un forward où **personne ne livre**. À
> l'échéance on compare le taux convenu au **fixing PTAX** de la Banque
> centrale du Brésil, et **on règle la différence en dollars**.

> 🇬🇧 *« The real isn't freely deliverable offshore, so everything trades as
> NDFs — cash-settled in dollars against the PTAX fixing. »*

## Cette semaine : le point que personne ne relève

**Copom et FOMC décident les mêmes jours (15-16 septembre), en sens opposés.**

| | Avant | Attendu |
|---|---|---|
| Selic | 14,00 % | **13,75 %** (−25 bp, ~95 % probable) |
| Fed | 3,625 % | **3,875 %** (+25 bp, ~85 % probable) |
| **Carry** | **10,4 pts** | **9,9 pts** |

> 🎯 *« Le carry perd 50 bp en deux séances. Mais à presque 10 points, il reste
> de loin le plus large des grandes devises — c'est pour ça que les analystes
> n'attendent qu'une pression modérée sur le réal. »*

## Pétrole et réal — la question à deux canaux

Tu as buté dessus. Il n'y a **pas** de réponse unique :

| Canal | Effet du Brent à 105 |
|---|---|
| **Termes de l'échange** — le Brésil est exportateur net (pré-sal) | BRL **soutenu** |
| **Financier** — pétrole cher → inflation → Fed hawkish → USD fort | BRL **sous pression** |

> 🇬🇧 *« Two channels pull in opposite directions. Terms of trade help Brazil —
> it's a net oil exporter. But the financial channel hurts: expensive oil means
> global inflation, a hawkish Fed, a stronger dollar and EM outflows. Right now
> the first channel is winning. If the Fed hikes on Wednesday, the second takes
> over. »*

⚠️ **La règle qui prime :** en **risk-off violent**, toutes les devises EM
baissent, exportatrices ou non.

## Le troisième moteur : l'élection d'octobre

Lula et Flávio Bolsonaro sont **à égalité technique**. Le marché voit Bolsonaro
comme plus restrictif budgétairement → **chaque sondage favorable à Bolsonaro
fait monter le réal**.

## Le skew sur USD/BRL

> **Le skew, c'est le prix de l'assurance contre le scénario qui fait mal.**

| Marché | Le plus cher | Pourquoi |
|---|---|---|
| Actions | Les **puts** | Protection contre le krach |
| EUR/USD | ~symétrique | Pas de krach naturel |
| **USD/BRL** | Les **calls USD** | Le stress = fuite vers le dollar |

Le mot à placer : **risk reversal** (acheter un call, vendre un put de même
delta) = la mesure directe du skew.

---

# 5. CACIB — l'actualité à connaître

> ⚠️ Deux ou trois faits suffisent. Réciter un rapport annuel est contre-productif.

## Le fait qui compte pour ton appel

> **Crédit Agricole CIB a été élu *Best Asia FX Non-Deliverable Forward House*
> par FX Markets.** Après avoir refondu son offre électronique, la banque a vu
> ses **volumes NDF croître de 200 %**, et figure dans le **top 3 des
> plateformes de streaming NDF multi-bancaires**. Elle a aussi été la
> **première banque étrangère à exécuter des NDF via le CFETS** en Chine.

**Lis bien ce paragraphe.** Le NDF électronique n'est pas un détail chez CACIB
— **c'est leur franchise reconnue**. Et c'est exactement ce dont on parle
depuis le début avec le Brésil.

## Autres repères

- **FX House of the Year — Hong Kong** (FX Markets Asia Awards 2026)
- CACIB est la banque de financement et d'investissement du groupe Crédit
  Agricole ; le pôle Grandes Clientèles a fait **2 358 M€ de revenus au T1 2026**
- Groupe CA : RoTE 11,4 %, CET1 phasé 17,1 % au T1 2026

## 🎯 La phrase qui va marquer

> *« Ce qui m'a marqué en préparant cet appel, c'est que CACIB a été élu
> meilleure maison de NDF en Asie, avec des volumes en hausse de 200 % après la
> refonte de l'offre électronique. C'est exactement ce qui m'intéresse : le NDF
> est le segment où l'électronification n'est pas terminée, et c'est là qu'il
> reste quelque chose à construire. »*

🇬🇧 *« You were named best NDF house in Asia after a two hundred percent volume
increase — that's exactly the space I find interesting, because NDF
electronification isn't finished yet. »*

**Pourquoi c'est parfait :** tu montres que tu t'es renseigné **sur son métier
précis**, pas sur la banque en général. Et ça relie naturellement au Brésil.

---

# 6. Ton profil — les 3 points à placer

## a) BPCE — ton vrai argument eFX

> *« Chez BPCE Assurances j'ai automatisé des flux avec Bloomberg BQL, Python
> et VBA. Ce qui m'a intéressé, ce n'était pas le produit — c'était que la
> valeur vienne de l'infrastructure, de la vitesse et de la qualité
> d'exécution. L'eFX, c'est exactement ça à l'échelle d'un desk. »*

## b) ShockDesk — comment en parler sans se faire piéger

**Les chiffres :** 25,5 M USD · **+337 883 USD (+1,32 %)** · **Sharpe 1,67** ·
**drawdown max 8 bp** · 21 trades.

> *« C'est un backtest de stratégie macro, pas de l'argent réel — je le précise
> tout de suite. Ce que j'en retiens n'est pas le P&L : c'est que sur mes
> positions, avoir raison sur la direction comptait moins qu'avoir raison sur
> le timing. Environ 600 000 d'écart entre le pic et le stop, sur la même vue. »*

> ⚠️ **Dis « backtest » AVANT qu'on te le demande.** Si on te l'arrache, tu
> passes pour quelqu'un qui gonfle. Si tu le dis d'emblée, tu passes pour
> quelqu'un d'honnête.

🇬🇧 *« It's a backtest, point-in-time data, no look-ahead. What I took from it
is that timing mattered more than direction. »*

## c) Ton positionnement — à dire SANS hésiter

> *« L'eFX, clairement. »* — puis tu justifies avec BPCE et les émergents.

⚠️ **Ne dis jamais « les deux m'intéressent ».** Hésiter sur ce qu'on veut est
le seul défaut que le travail ne rattrape pas : on ne recommande pas quelqu'un
dont on ne sait pas à qui l'envoyer.

---

# 7. Les 7 pièges

| # | Le piège | Ce qu'il faut faire |
|---|---|---|
| 1 | **« Le forward anticipe une baisse du réal »** | Non. C'est le différentiel de taux. |
| 2 | **Hocher la tête sur un mot inconnu** | Demander. *« Sorry, hit ratio — c'est la part de RFQ que vous gagnez ? »* |
| 3 | **Hésiter entre eFX et exotiques** | Trancher en trois mots, puis justifier. |
| 4 | **Inventer un niveau de marché** | *« I don't have that in front of me — where is it trading? »* |
| 5 | **Présenter ShockDesk comme du réel** | Dire « backtest » spontanément. |
| 6 | **Réciter un pitch** | Si ça sonne écrit, il coupera. Parle, ne récite pas. |
| 7 | **Dire « le pétrole monte donc le réal monte »** | Donner les deux canaux, puis trancher. |

> **Le seul vraiment éliminatoire, c'est le n°2.** Personne n'a jamais été
> écarté pour avoir posé une question. Beaucoup l'ont été pour avoir fait
> semblant.

---

# 8. Les 10 questions — FR et EN

**Q1. Parle-moi de ton parcours.** *(90 secondes, chrono)*
> M2 SKEMA, prépa ECE. Stage BPCE : automatisation de flux en BQL/Python/VBA.
> Projets perso : terminal de marché, pricer BS, ShockDesk. Cherche un stage
> 6 mois dès janvier 2027 en eFX.

**Q2. Pourquoi le FX, et pourquoi l'électronique ?**
> Voir section 6a. La valeur vient de l'infrastructure.

**Q3. What are you watching in the markets right now?**
> 🇬🇧 *« Oil, because it drives everything else. Brent above a hundred pushed
> inflation back up, the ECB hiked on Thursday, and the Fed is expected to hike
> on Wednesday — the first since 2023. We've gone from debating when they cut
> to pricing when they hike. »*

**Q4. Le carry trade, tu peux m'expliquer ?**
> Emprunter bas, placer haut. Brésil : 10,4 points. **Mais couvert ça ne
> rapporte rien** — le forward mange le carry. Et trois jours de vol effacent
> un trimestre.

**Q5. What's an NDF?**
> 🇬🇧 *« A forward with no delivery, for non-convertible currencies. You
> cash-settle the difference in dollars against an official fixing — PTAX for
> the real. »*

**Q6. Pourquoi le forward USD/BRL est à 5,29 quand le spot est à 5,16 ?**
> Cost of carry, pas une prévision. 10 points d'écart sur 3 mois ≈ 1 300 pips.
> Sinon il y aurait un arbitrage sans risque.

**Q7. Le pétrole, ça fait quoi aux devises émergentes ?**
> Les deux canaux. Voir section 4.

**Q8. C'est quoi le skew ?**
> Le prix de l'assurance contre le scénario qui fait mal. Sur USD/BRL, les
> calls dollar cotent plus cher. Mesuré par le **risk reversal**.

**Q9. Tu as une idée de trade ?**
> ⚠️ **Ne joue pas au gérant.**
> *« Je n'ai pas la prétention d'avoir une position. J'observe que le carry
> brésilien reste très large même après le Copom, mais que tout le monde est du
> même côté avant une élection serrée. C'est plus une question de
> dimensionnement que de direction. »*

**Q10. Tu as des questions ?**
> ⚠️ **Ne jamais répondre non.** Une seule, précise :
> *« Quelle part de votre flux vous arrivez à internaliser ? »*
> ou *« Sur quels segments de clients vous voyez la croissance électronique la
> plus forte en ce moment ? »*

---

# Les 8 chiffres à avoir en tête

| | |
|---|---|
| USD/BRL | **5,16** · forward 3M **5,29** |
| Selic | **14,00 %** → 13,75 % attendu |
| Fed | **3,50-3,75 %** → hausse attendue le 16 (~85 %) |
| BCE dépôt | **2,50 %** |
| Carry BRL | **10,4 pts** → 9,9 après cette semaine |
| EUR/USD | **1,161** |
| Brent | **~105 USD** |
| CACIB | **Best Asia NDF House**, volumes **+200 %** |

> **Si tu ne retiens que trois choses de cette heure :**
> **1.** Le forward n'est pas une prévision, c'est le cost of carry.
> **2.** Le carry couvert ne rapporte rien — tout le trade est le pari non couvert.
> **3.** Quand tu ne sais pas, tu demandes. Jamais tu ne fais semblant.
