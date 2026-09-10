# Cours d'urgence FIC — 2 h

**Objectif : pouvoir dire « je connais » sur toutes les notions du périmètre.**
Pas de démonstration longue. Des images mentales, des exemples concrets, des
chiffres que tu peux ressortir.

> 🎯 **Comment lire.** Chaque notion suit le même schéma : **l'image mentale**
> d'abord, puis **le chiffre**, puis **la phrase à dire**. Si tu retiens l'image,
> le reste revient. Si tu ne retiens que la formule, tu bloqueras.

**Les 6 blocs :** taux · obligations · dérivés fermes · options · vol · crédit &
FX.

---

# BLOC 1 — Les taux (15 min)

## 1.1 L'actualisation

**L'image :** 100 € dans un an ne valent pas 100 € aujourd'hui. Parce qu'avec
96 € aujourd'hui placés à 4 %, tu as 100 € dans un an. **Donc 100 € dans un an
= 96 € aujourd'hui.**

C'est tout. Toute la finance de taux, c'est ça, répété.

| Recevoir 100 € | À 4 %, ça vaut aujourd'hui |
|---|---|
| dans 1 an | **96,15 €** |
| dans 10 ans | **67,56 €** |

> **À retenir :** plus c'est loin, moins ça vaut. Et **plus le taux monte, moins
> ça vaut**. Cette phrase explique 80 % du marché obligataire.

## 1.2 La courbe des taux

**L'image :** c'est le prix du temps. Sur l'axe horizontal, la durée du prêt
(1 an, 2 ans… 30 ans). Sur l'axe vertical, le taux exigé.

| Forme | Nom | Ce que ça raconte |
|---|---|---|
| Monte | **normale** | Prêter longtemps est plus risqué, on exige plus |
| Plate | **flat** | Incertitude, transition |
| Descend | **inversée** | Le marché anticipe des baisses de taux — souvent une récession |

**Les mouvements — le vocabulaire de desk :**

| Mouvement | Nom |
|---|---|
| L'écart court-long **augmente** | **steepening** (la courbe se pentifie) |
| L'écart **diminue** | **flattening** (elle s'aplatit) |
| Toute la courbe monte/descend | **parallel shift** |

> **Bull ou bear ?** *Bull* = les prix montent = **les taux baissent**.
> **Bull steepener** = le court baisse plus que le long. **Bear flattener** = le
> court monte plus que le long (typique d'une banque centrale qui resserre).

## 1.3 Taux directeurs et marché

**Aujourd'hui (10/09/2026) :** la BCE a monté de **25 bp**, dépôt à **2,50 %**.
Le marché price **~40 %** de proba d'une hausse de plus en décembre.

**Un point de base (bp) = 0,01 %.** On dit **« un bip »**. Sur 10 M€, 1 bp =
1 000 € par an. Ce n'est jamais négligeable.

---

# BLOC 2 — Les obligations (25 min)

## 2.1 Le mécanisme

**L'image :** tu prêtes 100 € à un État pour 5 ans. Il te verse **3 € par an**
(le coupon), et te rend **100 € à la fin** (le nominal).

## 2.2 LA relation à comprendre : prix ↔ taux

**L'image terre à terre.** Tu as acheté une obligation qui paie **3 %**. Le
lendemain, l'État émet la même à **4 %**.

Ton titre à 3 % n'intéresse plus personne au prix de 100. Pour le vendre, tu
dois **baisser ton prix** jusqu'à ce que l'acheteur obtienne l'équivalent de
4 %.

> 🔑 **Le prix d'une obligation et son rendement bougent en sens inverse.
> Toujours.** C'est la question numéro 1 en entretien FIC. Si tu ne retiens
> qu'une chose de ce cours, c'est celle-là.

**Le chiffre :** obligation 5 ans, coupon 3 %

| Rendement du marché | Prix |
|---|---|
| 3 % | **100,00** (au pair) |
| 4 % | **95,55** |
| 5 % | **91,34** |

## 2.3 La duration

**L'image :** c'est le **bras de levier** de l'obligation face aux taux.
Duration 5 → si les taux montent de 1 %, tu perds environ 5 %.

Techniquement c'est la maturité moyenne pondérée des flux — mais **en entretien,
dis « la sensibilité aux taux »**. C'est ce qu'on attend.

$$\Delta P / P \approx -MD \times \Delta y$$

**Le chiffre :** l'obligation ci-dessus a une **duration modifiée de 4,53**.
Pour +100 bp, l'approximation prédit **−4,53 %**. Le vrai calcul donne
**−4,40 %**.

## 2.4 La convexité

**L'écart entre −4,53 % et −4,40 %, c'est elle.**

**L'image :** la relation prix/taux n'est pas une droite, c'est une **courbe**.
Résultat, c'est **asymétrique en ta faveur** quand tu détiens l'obligation :

| Mouvement | Effet réel |
|---|---|
| Taux **+100 bp** | **−4,40 %** |
| Taux **−100 bp** | **+4,66 %** |

> **Tu gagnes plus quand ça baisse que tu ne perds quand ça monte.** C'est la
> convexité, et **c'est pour ça qu'elle se paie**. Retiens l'asymétrie, pas la
> formule.

## 2.5 Le repo

**L'image :** tu as besoin de cash pour la nuit. Tu **vends** ton obligation en
t'engageant à la racheter demain un peu plus cher. C'est un **prêt garanti par
un titre** — c'est comme ça que se finance un desk.

Si tout le monde veut le même titre, il devient **special** : tu te finances
moins cher parce que ton collatéral est recherché.
*"That bond is trading special."*

---

# BLOC 3 — Forwards, futures, swaps (20 min)

## 3.1 Le forward

**L'image :** tu fixes aujourd'hui le prix d'une transaction future. Pas de cash
maintenant, tout à l'échéance.

> ⚠️ **L'erreur que font tous les étudiants :** le prix forward n'est **PAS une
> prévision**. C'est le spot **plus le coût de portage** : ce que ça coûte de
> détenir l'actif jusqu'à l'échéance (le financement, moins ce que l'actif
> rapporte).

$$F = S_0 e^{(r-q)T}$$

**L'exemple terre à terre :** or à 2 000 €, taux 4 %. Le forward 1 an vaut
~2 082 €. Pas parce que l'or va monter — **parce que tu empruntes 2 000 € pendant
un an pour le détenir**.

| Cas | q représente |
|---|---|
| Action / indice | le dividende |
| **FX** | le **taux étranger** |
| Commodité | le rendement de convenance − le stockage |

**Les chiffres :** indice S=3500, r=3,5 %, q=1,8 %, T=0,75 → **F = 3544,91**
EURUSD 1,0850, r_d=4,25 %, r_f=2,25 %, T=0,25 → **F = 1,090439** (+54,4 pips)

> **Contango** = forward au-dessus du spot (r > q). **Backwardation** = en
> dessous.

## 3.2 Futures vs forwards

| | Forward | Future |
|---|---|---|
| Où | gré à gré (OTC) | en bourse |
| Sur-mesure | oui | non, standardisé |
| Risque de contrepartie | oui | non (chambre de compensation) |
| Flux | tout à la fin | **appels de marge quotidiens** |

## 3.3 Le swap de taux

**L'image :** deux parties échangent des flux d'intérêts sur un montant
notionnel. L'un paie **fixe**, l'autre paie **variable**.

**L'exemple concret :** une entreprise a emprunté à taux variable et craint une
hausse. Elle **paie fixe / reçoit variable** : elle a transformé sa dette
variable en dette fixe. Elle a acheté de la **tranquillité**.

> **Le notionnel ne s'échange jamais.** Seuls les intérêts circulent. C'est
> pour ça qu'on parle de milliards de notionnel sans mouvement de capitaux.

**Payer fixe = être short duration** : tu gagnes si les taux montent.

---

# BLOC 4 — Les options (35 min)

## 4.1 Le mécanisme

**L'image :** l'option est une **assurance**. Tu paies une **prime** pour avoir
le **droit** — pas l'obligation — d'acheter (call) ou de vendre (put) à un prix
fixé (**strike**).

| | Tu es acheteur | Tu es vendeur |
|---|---|---|
| **Perte max** | la prime | **illimitée** |
| **Gain max** | illimité | la prime |

> **L'asymétrie est tout.** L'acheteur d'option paie pour dormir. Le vendeur
> encaisse pour prendre le risque. Un desk fait surtout… **vendeur**.

**Vocabulaire :** *in the money* (exercer est rentable) · *at the money*
(strike = spot) · *out of the money*.

## 4.2 La parité call-put

**L'image :** acheter un call et vendre un put au même strike, c'est
**exactement** détenir l'actif à crédit. Donc les prix sont liés — pas par une
théorie, par un **arbitrage** : sinon on encaisse la différence sans risque.

$$C - P = S_0 e^{-qT} - K e^{-rT}$$

**Le chiffre :** S=100, K=100, r=4 %, q=2 %, T=0,5, C=6,20 → **P = 5,2149**

## 4.3 Black-Scholes

**L'idée en une phrase :** on peut **fabriquer** une option en détenant une
quantité d'actif qu'on ajuste en continu. Si la copie est parfaite, l'option n'a
qu'**un seul prix possible** — celui de la copie.

$$C = S_0 e^{-qT} N(d_1) - K e^{-rT} N(d_2)$$

**Comment la lire, sans la démontrer :**

| Terme | Ce que c'est |
|---|---|
| $N(d_2)$ | la probabilité de finir **dans la monnaie** |
| $N(d_1)$ | le **delta** — combien d'actif détenir pour couvrir |
| $Ke^{-rT}$ | le strike, actualisé |

**Le chiffre :** S=100, K=105, r=3 %, σ=25 %, T=0,5 → **C = 5,5760**,
**P = 9,0127**

**L'approximation de tête** (call ATM, r=0) :
$$C \approx 0{,}4 \times \sigma\sqrt{T} \times S$$
σ=20 %, T=1, S=100 → **8,00** vs vrai prix **7,9656**. Impressionnant en
entretien.

### Les 6 hypothèses — à réciter

1. Mouvement brownien géométrique (rendements log-normaux)
2. **Volatilité constante**
3. Taux constant
4. Pas de coûts de transaction ni de taxes
5. Divisibilité parfaite, vente à découvert possible
6. Pas d'arbitrage, option **européenne**

> **La question qui tombe : « laquelle casse en premier ? »**
> **La vol constante.** Et la preuve est publique : le **smile de volatilité**.
> Le marché lui-même contredit l'hypothèse du modèle qu'il utilise.

## 4.4 Les grecs

**L'image globale :** ce sont les **cadrans du tableau de bord**. Chacun répond
à « si CE paramètre bouge, je perds combien ? ».

| Grec | Répond à | L'image |
|---|---|---|
| **Delta** Δ | le spot bouge | ta **vitesse** |
| **Gamma** Γ | le delta bouge | ton **accélération** |
| **Vega** | la vol bouge | ta sensibilité à la **peur** |
| **Theta** Θ | un jour passe | le **loyer** que tu paies |
| **Rho** ρ | les taux bougent | le plus petit, souvent ignoré |

**Les chiffres (sur l'exemple ci-dessus) :** Δ=0,459 · Γ=0,0224 · vega=0,281 ·
Θ/jour=−0,0225 · ρ=0,202

### Gamma et theta : le couple central

**L'image :** le gamma est une **voiture de sport**, le theta est le **plein
d'essence**.

- **Long gamma** : tu profites des mouvements, mais tu paies du theta chaque
  jour. Tu veux que **ça bouge**.
- **Short gamma** : tu encaisses du theta, mais un mouvement violent te coûte.
  Tu veux que **rien ne se passe**.

$$\Theta + \tfrac{1}{2}\sigma^2 S^2 \Gamma = 0 \quad (r = q = 0)$$

> **Traduction : la convexité se paie en temps.** Toute la vie d'un desk
> d'options est dans cet arbitrage.

### 🚨 La question piège : *short gamma*

**Ce qui se passe concrètement.** Tu es vendeur d'options, tu te couvres en
delta. Le marché monte → ton delta devient négatif → tu dois **acheter** pour
te recouvrir. Le marché baisse → tu dois **vendre**.

**Tu achètes haut, tu vends bas. À chaque ajustement.**

> **En anglais :** *"When you're short gamma, you're hedging into the move — you
> buy the highs and sell the lows. You collect theta, but a fast market costs
> you more than you collect."*
>
> **Et tu l'as vu** sur mars 2020 dans ton pricer Excel. Dis-le : c'est du vécu,
> ça vaut dix réponses théoriques.

---

# BLOC 5 — La volatilité (15 min)

## 5.1 Réalisée vs implicite

| | Ce que c'est |
|---|---|
| **Réalisée** (historique) | ce que le marché **a fait** — un calcul sur le passé |
| **Implicite** | ce que le marché **anticipe** — extraite du prix des options |

> **L'implicite est un prix, pas une prévision.** C'est le niveau de vol qui
> rend la formule cohérente avec le prix coté. Quand un trader dit *« la vol est
> chère »* (*rich*), il dit que l'implicite est au-dessus de ce qu'il pense que
> la réalisée sera.

## 5.2 Le smile

**Le fait :** Black-Scholes suppose une vol unique. Le marché, lui, cote **une
vol différente pour chaque strike**. Tracé, ça fait un **sourire**.

**Pourquoi ?** Parce que les vrais rendements ont des **queues épaisses** : les
krachs sont plus fréquents que ce que suppose la loi normale. Les puts loin de
la monnaie sont donc **plus chers** que le modèle ne le dit — ce sont des
assurances contre le krach.

> **La phrase qui montre que tu comprends :** *"The smile is the market pricing
> in what the model leaves out."*

## 5.3 Les structures à connaître de nom

| Structure | Composition | Pour quoi |
|---|---|---|
| **Straddle** | call + put, **même strike** | tu paries que **ça bouge**, peu importe le sens |
| **Strangle** | call + put, strikes **écartés** | pareil, moins cher, il faut un mouvement plus fort |
| **Call spread** | acheter un call, vendre un plus haut | vue haussière, **moins chère**, gain plafonné |
| **Butterfly** | pari sur la **stabilité** | tu gagnes si ça ne bouge pas |
| **Risk reversal** | acheter un call, vendre un put | vue directionnelle **à coût réduit** |

**Le chiffre :** straddle **24,40** vs strangle **10,69** — le straddle coûte
**2,3×** plus cher. C'est le prix de la zone couverte.

---

# BLOC 6 — Crédit et FX (15 min)

## 6.1 Le spread de crédit

**L'image :** c'est le **supplément** exigé pour prêter à une entreprise plutôt
qu'à un État. C'est le prix du risque de défaut.

**Le chiffre :** un spread de **150 bp** sur 10 M€, c'est **150 000 € par an**.

| Mouvement | Nom | Sens |
|---|---|---|
| Le spread **diminue** | **tightening** | le marché est plus confiant |
| Le spread **augmente** | **widening** | stress, fuite vers la qualité |

**Investment grade** (≥ BBB−) vs **high yield** (en dessous). Le **CDS** est
l'assurance contre le défaut : tu paies une prime annuelle, tu es indemnisé si
l'émetteur fait défaut.

## 6.2 L'OAT-Bund

**L'image :** l'écart entre le taux français et le taux allemand. **La prime de
risque France**, mesurée en direct.

**Le chiffre du jour : ~85 bp** (OAT 10 ans 4,19 %, Bund 3,34 %). La fourchette
sur un an est 59-85 bp → **on est au sommet**. C'est un fait que tu peux citer
mardi.

## 6.3 Le FX

**Une paire est un rapport.** EUR/USD = 1,0850 → 1 € vaut 1,0850 USD.

**Le point clé :** le forward FX ne dit **rien** sur la direction future. Il ne
reflète que **l'écart de taux** entre les deux devises.

> **La parité des taux d'intérêt :** si tu places en dollar à un taux plus élevé
> qu'en euro, le forward EUR/USD sera **plus haut** — exactement de quoi annuler
> ton gain. **Sinon, arbitrage.**

**Un pip** = la 4ᵉ décimale. De 1,0850 à 1,0851 = **1 pip**.

---

# 🎯 Ce que tu dois pouvoir dire mardi

Coche mentalement. Si tu réponds à voix haute sans bloquer, c'est acquis.

| # | Question | La réponse en une ligne |
|---|---|---|
| 1 | Prix et taux d'une obligation ? | **Sens inverse, toujours** |
| 2 | La duration ? | La sensibilité aux taux. Duration 5 → +1 % de taux = −5 % |
| 3 | La convexité ? | La relation est courbe : on gagne plus qu'on ne perd |
| 4 | Le forward est-il une prévision ? | **Non** — spot + coût de portage |
| 5 | Un swap de taux ? | Échange fixe contre variable, **le notionnel ne bouge pas** |
| 6 | La parité call-put ? | Call − put = position forward. Arbitrage |
| 7 | L'idée de Black-Scholes ? | La **réplication** : si on copie l'option, il n'y a qu'un prix |
| 8 | Quelle hypothèse casse ? | **La vol constante** → le smile |
| 9 | Le gamma ? | La vitesse à laquelle mon delta se périme |
| 10 | Short gamma, marché rapide ? | J'achète haut, je vends bas à chaque couverture |
| 11 | Vol implicite ? | Un **prix**, pas une prévision |
| 12 | Un spread de crédit ? | Le prix du risque de défaut. 150 bp sur 10 M = 150 k/an |

---

## Si un recruteur creuse trop

> *"I know the concept and I can use it — I haven't derived it from scratch.
> That's on my list."*

**C'est une bonne réponse.** Elle est honnête, elle montre que tu sais où sont
tes limites, et **personne n'attend d'un M2 qu'il redémontre Black-Scholes**.
Ce qu'on attend, c'est que tu **saches de quoi tu parles** — et après ce cours,
c'est le cas.

> **Ce soir :** lis en entier, sans t'arrêter sur ce qui résiste. Demain, tu
> relis **uniquement les 12 questions** du tableau, à voix haute. Le reste se
> déposera tout seul.
