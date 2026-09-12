# Les 3 trous de la simulation — et comment les boucher

> Gemini a nommé trois choses : **les corrélations macro**, **le skew et le
> carry**, et **le positionnement** (eFX ou exotiques, tu as hésité).
>
> Cette fiche ne traite que ça. Rien d'autre. Elle se lit en 30 minutes.

---

# TROU 1 — Pétrole et devises émergentes

Tu as buté dessus parce qu'**il n'y a pas de réponse unique**, et que tu
cherchais la bonne. Voilà la vraie structure.

## La règle de base : ça dépend de qui exporte

| Type de pays | Exemples | Pétrole ↑ |
|---|---|---|
| **Exportateurs nets** | 🇧🇷 Brésil, 🇲🇽 Mexique, 🇨🇴 Colombie, 🇷🇺 Russie, 🇳🇴 Norvège | Devise **soutenue** |
| **Importateurs nets** | 🇮🇳 Inde, 🇹🇷 Turquie, 🇨🇱 Chili, 🇯🇵 Japon | Devise **sous pression** |

C'est le canal des **termes de l'échange** : un exportateur vend plus cher ce
qu'il produit, ses recettes en dollars montent, sa devise se renforce.

## Mais il y a un second canal, qui joue en sens inverse

> **Pétrole cher → inflation mondiale → banques centrales hawkish → dollar fort
> et taux longs US en hausse → sortie de capitaux des émergents.**

C'est **exactement la situation d'aujourd'hui** : le Brent au-dessus de 100 a
poussé la Fed vers une hausse le 16 septembre, avec le 10 ans US à 4,96 %.

## 🔑 La réponse à donner, en deux temps

> *« Il y a deux canaux qui s'opposent. Le canal des termes de l'échange
> favorise les exportateurs — le Brésil est exportateur net depuis le pré-sal,
> donc un Brent à 105 soutient le réal. Mais le canal financier joue contre :
> un pétrole cher fait remonter l'inflation mondiale, la Fed devient hawkish,
> le dollar se renforce et les capitaux quittent l'EM.
>
> Aujourd'hui le premier canal gagne sur le réal — il est à 5,16, en hausse de
> 5 % sur un an. Mais si la Fed monte mercredi, le second canal reprend le
> dessus. »*

**Pourquoi cette réponse est parfaite :** tu ne donnes pas *une* réponse, tu
donnes **le cadre**, puis tu tranches sur le cas d'espèce. C'est exactement
comme ça qu'un desk raisonne. Dire « le pétrole monte donc le réal monte » est
une réponse d'étudiant.

## Le tableau à mémoriser

| Choc | Canal réel | Canal financier | Qui gagne |
|---|---|---|---|
| Pétrole ↑, Fed **dovish** | BRL ↑ | neutre | **BRL fort** |
| Pétrole ↑, Fed **hawkish** | BRL ↑ | BRL ↓ | **Ça dépend — dis-le** |
| Pétrole ↓, Fed dovish | BRL ↓ | BRL ↑ | ambigu |
| **Risk-off généralisé** | — | BRL ↓↓ | **BRL faible, toujours** |

> ⚠️ **La règle qui prime sur tout.** En **risk-off violent**, toutes les
> devises émergentes baissent, exportatrices ou non. Le carry se déboucle,
> personne ne regarde les fondamentaux. **Si tu ne dois retenir qu'une ligne,
> c'est celle-là.**

---

# TROU 2 — Le carry trade, chiffré

Tu connaissais le mot. Il te manquait **les chiffres et le risque**.

## Où on en est aujourd'hui

$$\text{Carry} = \text{Selic} - \text{Fed} = 14{,}00 - 3{,}625 = \mathbf{10{,}4 \text{ points}}$$

## Ce qui se passe cette semaine — le point que personne ne relève

Le **Copom** et le **FOMC** décident **les mêmes jours**, les 15 et 16
septembre, **en sens opposés** :

| | Avant | Après (attendu) |
|---|---|---|
| Selic | 14,00 % | **13,75 %** (−25 bp) |
| Fed | 3,625 % | **3,875 %** (+25 bp) |
| **Carry** | **10,4 pts** | **9,9 pts** |

**Le carry perd 50 bp en deux jours.** Mais à presque 10 points, il reste de
très loin le plus large des grandes devises.

## Le chiffre qui fait la différence : le point mort

Sur 3 mois, un carry de 9,9 % annualisé rapporte **2,47 %**. Avec un spot à
5,16, ton point mort est à :

$$5{,}16 \times (1 + 0{,}0247) = \mathbf{5{,}2874}$$

> **Autrement dit : si l'USD/BRL monte de plus de 1 274 pips en trois mois, tu
> perds de l'argent malgré 10 points de carry.**

Et la volatilité du réal tourne autour de **13 % annualisé**, soit **0,82 % par
jour**. Donc :

> 🎯 **La phrase qui va faire mouche.**
> *« Trois mois de carry brésilien, c'est 2,5 %. La vol quotidienne du réal est
> à 0,8 %. Ça veut dire que trois séances à un écart-type effacent un trimestre
> entier de portage. C'est pour ça qu'on dit que le carry, c'est ramasser des
> pièces devant un rouleau compresseur. »*

**Pourquoi cette réponse est parfaite :** tu transformes une notion en **ratio
risque/rendement chiffré**. C'est le réflexe qu'on cherche sur un desk.

## Et le lien avec le forward, qu'on va te tendre

> Le forward USD/BRL 3M est à **5,2910**, soit **+1 310 pips** au-dessus du
> spot. **Ces points, c'est exactement le carry.** Si tu te couvres, tu les
> paies et tu ne gagnes rien. **Le carry trade n'existe que non couvert.**

---

# TROU 3 — Le skew

Tu as hésité. C'est normal : personne ne l'explique clairement. Voilà.

## Le smile, puis le skew

Black-Scholes suppose **une seule volatilité** pour tous les strikes. Le marché
dit l'inverse : chaque strike a **sa propre volatilité implicite**.

- **Smile** : les options loin de la monnaie, des deux côtés, cotent une vol
  plus élevée. La courbe ressemble à un sourire.
- **Skew** : le sourire est **asymétrique**. Un côté cote plus cher que l'autre.

## Le sens du skew selon le marché

| Marché | Qui cote le plus cher | Pourquoi |
|---|---|---|
| **Actions / indices** | Les **puts** (strikes bas) | Tout le monde veut se protéger d'un krach. Les marchés actions chutent plus vite qu'ils ne montent. |
| **FX développé** (EUR/USD) | À peu près **symétrique** | Une hausse de l'euro est une baisse du dollar. Il n'y a pas de « krach » naturel. |
| **FX émergent** (USD/BRL) | Les **calls USD** | Le risque est la **fuite vers le dollar**. On se protège contre un effondrement du réal, pas contre sa hausse. |

## 🔑 La réponse à donner

> *« Le skew, c'est le fait que la volatilité implicite dépend du strike.
> Sur actions, les puts cotent plus cher parce que la demande de protection est
> structurelle et que les marchés tombent plus vite qu'ils ne montent.
>
> Sur les émergents c'est le même mécanisme mais inversé côté paire : sur
> USD/BRL, ce sont les calls dollar qui cotent le plus cher, parce que le
> scénario de stress c'est la fuite vers le dollar. Le skew, c'est le prix de
> l'assurance contre le scénario qui fait mal. »*

**Pourquoi cette réponse est parfaite :** la dernière phrase — *« le prix de
l'assurance contre le scénario qui fait mal »* — est une définition qu'un
trader valide immédiatement.

## Le mot à placer : *risk reversal*

> Un **risk reversal**, c'est acheter un call et vendre un put de même delta
> (typiquement 25 delta). **C'est la mesure directe du skew.** Quand un sales FX
> dit *« le 25 delta risk reversal s'est écarté »*, il dit que le marché paye
> plus cher la protection d'un côté.

Sur USD/BRL, le risk reversal est **structurellement en faveur des calls
dollar**. Si tu places ça, tu ne ressembles plus à un étudiant.

---

# TROU 4 — Le positionnement (celui qui coûte le plus cher)

Gemini a relevé que tu as hésité entre eFX et exotiques. **C'est le point le
plus grave des trois, et le plus facile à corriger.**

> Hésiter sur ce qu'on veut, c'est le seul défaut qui ne se rattrape pas par du
> travail. Un candidat qui ne sait pas ce qu'il veut, on ne le recommande pas —
> parce qu'on ne sait pas à qui l'envoyer.

## Ta réponse, à apprendre par cœur

> *« L'eFX, clairement. Et je peux dire pourquoi précisément.
>
> Chez BPCE j'ai automatisé des flux avec BQL et Python. Ce qui m'a intéressé,
> ce n'était pas le produit, c'était le fait que la valeur vienne de
> l'infrastructure — de la vitesse et de la qualité d'exécution. L'eFX, c'est
> exactement ça à l'échelle d'un desk.
>
> Et je suis particulièrement attiré par les émergents, parce que c'est le
> segment où l'électronification n'est pas terminée. Les NDF brésiliens se
> traitent encore beaucoup à la voix. C'est là qu'il reste quelque chose à
> construire. »*

**Pourquoi cette réponse est parfaite :**
1. Tu réponds **en trois mots** avant de justifier. Pas d'hésitation.
2. Tu relies à **ton vécu réel** (BPCE), pas à une envie abstraite.
3. Tu montres que tu as compris **l'économie du métier** — la valeur vient de
   l'infrastructure.
4. Tu termines sur **les émergents**, qui est ton angle différenciant.

> ⚠️ **Ne dis jamais « les deux m'intéressent ».** Même si c'est vrai. Choisis,
> assume, et garde l'ouverture pour la fin : *« cela dit, je suis là pour
> apprendre, pas pour arriver avec des exigences »*.

---

# Le vocabulaire anglais du desk eFX

| EN | FR | À dire quand |
|---|---|---|
| **hit ratio** | taux de réussite | Part des RFQ que le desk remporte |
| **RFQ** (*request for quote*) | demande de cotation | Le client demande un prix |
| **the skew** | le skew | Asymétrie de la vol implicite |
| **a risk reversal** | un risk reversal | Call moins put, la mesure du skew |
| **to internalise flow** | internaliser le flux | Matcher les clients entre eux sans aller au marché |
| **franchise flow** | flux de franchise | Le flux client récurrent, par opposition au risque pris |
| **to skew a price** | décaler un prix | Coter plus agressif d'un côté pour attirer le flux qui t'intéresse |
| **spread capture** | captation de spread | Ce que le desk gagne sur l'écart bid-ask |
| **last look** | last look | Droit de refuser un ordre après l'avoir coté |
| **a fixing** | un fixing | Cours de référence officiel (PTAX pour le BRL) |

> 🔑 **Le mot le plus rentable de cette liste : *internalisation*.** C'est le
> cœur du modèle économique d'un desk eFX. Si tu demandes à Romain *« quelle
> part de votre flux vous arrivez à internaliser ? »*, tu poses **la** question
> que pose un professionnel.

---

# Ce que tu fais maintenant

1. ☐ **Relis les 4 réponses en 🔑** — elles se disent à voix haute, pas en lecture
2. ☐ **Apprends 3 chiffres** : carry **10,4 pts** → **9,9** après cette semaine ·
   point mort **5,2874** · vol quotidienne **0,82 %**
3. ☐ **Apprends la réponse eFX par cœur.** Celle-là, mot pour mot.
4. ☐ **Refais la simulation** — `anglais/SIMULATION-call-CACIB.pdf`

> Tu as trois trous nommés et bouchés. C'est très différent d'un « niveau
> insuffisant ». **La deuxième simulation ne ressemblera pas à la première.**
