# M0 — Rappels maths pour le J1
### Annexe à lire *avant* (ou pendant) le cours J1 · dimanche 06/09/2026

> **À qui ça s'adresse.** À toi ce matin : les maths sont rouillées, et une
> ligne comme
> $\lim_{m\to\infty}(1+\frac{r}{m})^{mT}=e^{rT}$
> passe pour de la magie. Ce n'est pas de la magie, et ce n'est pas grave.
> **Être rouillé n'est pas être nul** : les outils reviennent en quelques
> heures si on les reprend dans le bon ordre.

**Ce que cette annexe n'est pas :** un cours de maths. Il n'y a **que** ce qui
sert au J1, rien de plus. Huit modules courts, chacun sur le même patron :

> **① À quoi ça sert dans J1** → **② Le rappel** → **③ Un exemple traité** →
> **④ 2 ou 3 micro-exercices** (corrigés en fin de module)

**Durée visée : 1 h 30**, crayon en main. Tu fais les exercices, tu ne les lis
pas. Un module = 10 min. Si un module passe tout seul, saute à l'exercice et
va au suivant.

**Règle du jour :** on ne cherche pas la rigueur d'un cours de licence. On
cherche à **savoir manipuler**. Un trader n'a jamais démontré le théorème
central limite ; il sait quand s'en servir.

| Module | Sujet | Débloque dans J1 |
|---|---|---|
| M1 | Exponentielle et logarithme | forwards, actualisation, §1 entier |
| M2 | Dérivées : les 6 qui servent | grecs, §6 |
| M3 | **Approximations locales (DL)** | la formule de ta capture, l'approx ATM |
| M4 | **La limite $(1+r/m)^{mT}\to e^{rT}$, lentement** | §0.1 |
| M5 | Loi normale : $\phi$ et $N$ | $N(d_1)$, $N(d_2)$, §4–5 |
| M6 | Somme d'exponentielles / complétion du carré | la démo de BS, §4.4 |
| M7 | Log-normale et le fameux $-\sigma^2/2$ | §4.2 |
| M8 | Dérivées partielles et règle de la chaîne | Itô, l'EDP, §4.3 |

---

## M1 — Exponentielle et logarithme

### ① À quoi ça sert
**Partout.** $F=Se^{(r-q)T}$, l'actualisation $e^{-rT}$, le $\ln(S/K)$ de
$d_1$. Si ce module est solide, la moitié du J1 devient mécanique.

### ② Le rappel

$e\approx2{,}718$. L'exponentielle transforme **les additions en
multiplications**, le log fait l'inverse. C'est tout.

| Règle | Formule | En clair |
|---|---|---|
| Produit | $e^a\cdot e^b=e^{a+b}$ | on **additionne** les exposants |
| Quotient | $e^a/e^b=e^{a-b}$ | on soustrait |
| Inverse | $e^{-a}=1/e^{a}$ | le signe moins = diviser |
| Neutre | $e^0=1$ | taux nul ou durée nulle ⇒ rien ne bouge |
| Log du produit | $\ln(ab)=\ln a+\ln b$ | |
| Log du quotient | $\ln(a/b)=\ln a-\ln b$ | c'est le $\ln(S/K)$ de $d_1$ |
| Puissance | $\ln(a^n)=n\ln a$ | |
| Réciproques | $\ln(e^x)=x$ et $e^{\ln x}=x$ | l'un défait l'autre |

**Les trois seuls repères numériques à retenir :**
$$\ln 2\approx0{,}69\qquad e\approx2{,}72\qquad e^{0{,}05}\approx1{,}051$$

**Le réflexe finance :** pour de **petits** taux, $e^x\approx1+x$.
Donc $e^{0{,}03}\approx1{,}03$ : capitaliser à 3 % ≈ multiplier par 1,03.
C'est faux à 0,05 % près, et **ça suffit pour un ordre de grandeur en oral**.

### ③ Exemple traité
*Actualiser 100 sur 6 mois à 4 % continu.*
$$100\,e^{-0{,}04\times0{,}5}=100\,e^{-0{,}02}\approx100\times(1-0{,}02)=98$$
Valeur exacte : $\mathbf{98{,}0199}$. L'approximation donne 98 : **erreur de 2
centimes**, obtenue de tête. C'est exactement le nombre du TD, exercice 1.

### ④ Micro-exercices

**M1.1** Simplifier $e^{rT}\cdot e^{-qT}$.
**M1.2** Calculer de tête $e^{-0{,}01}$ puis comparer à la vraie valeur $0{,}990050$.
**M1.3** Écrire $\ln\left(\frac{100}{105}\right)$ comme une différence de logs. Le signe est‑il positif ou négatif ? Pourquoi ?
**M1.4** Si $F=Se^{(r-q)T}$, isoler $r-q$.

<details><summary><b>Corrigés M1</b></summary>

**M1.1** $e^{rT}e^{-qT}=e^{rT-qT}=e^{(r-q)T}$. **C'est littéralement la formule
du forward** : capitaliser au taux $r$ et « décapitaliser » du dividende $q$.

**M1.2** $e^{-0{,}01}\approx1-0{,}01=0{,}99$. Vraie valeur $0{,}990050$.
Erreur : $5\times10^{-5}$.

**M1.3** $\ln 100-\ln 105$. **Négatif**, car $100<105$ : le log d'un nombre
inférieur à 1 est négatif. Dans $d_1$, ça traduit « je suis **sous** le
strike », donc l'option est OTM. Valeur : $-0{,}0488$ (le premier chiffre de
l'exercice 5 du TD).

**M1.4** $\frac{F}{S}=e^{(r-q)T}$, donc $\ln\frac{F}{S}=(r-q)T$, donc
$$r-q=\frac{1}{T}\ln\frac{F}{S}.$$
**Tu viens de retrouver seul la formule du convenience yield implicite**
(exercice 4 du TD) : on lit un taux dans une courbe en prenant un log.
</details>

---

## M2 — Dérivées : les six qui servent

### ① À quoi ça sert
Un grec **est** une dérivée. Delta = dérivée du prix par rapport au spot,
gamma = dérivée du delta. Pas de dérivées ⇒ pas de grecs.

### ② Le rappel

**L'idée en une phrase :** la dérivée $f'(x)$, c'est **de combien $f$ bouge
quand $x$ bouge d'une toute petite unité**. C'est une *sensibilité*. Un desk
ne dit jamais « dérivée », il dit « sensi ». Même chose.

| Fonction | Dérivée | Note |
|---|---|---|
| $x^n$ | $nx^{n-1}$ | |
| $e^{x}$ | $e^{x}$ | elle est sa propre dérivée |
| $e^{ax}$ | $a\,e^{ax}$ | le **$a$ descend** |
| $\ln x$ | $1/x$ | |
| $\sqrt x=x^{1/2}$ | $\frac{1}{2\sqrt x}$ | sert pour $\sqrt T$ |
| $f(g(x))$ | $f'(g(x))\cdot g'(x)$ | **règle de la chaîne** |

**Produit :** $(uv)'=u'v+uv'$.

**La règle de la chaîne, en français :** « je dérive l'extérieur, **puis** je
multiplie par la dérivée de l'intérieur ». C'est l'outil qu'on utilise le plus
en §6.

### ③ Exemple traité
*Dériver $f(T)=e^{-rT}$ par rapport à $T$.*
Extérieur : $e^{u}$, dérivée $e^{u}$. Intérieur : $u=-rT$, dérivée $-r$.
$$f'(T)=e^{-rT}\times(-r)=-r\,e^{-rT}$$
**Lecture :** le facteur d'actualisation **décroît** quand la maturité
s'allonge (signe négatif), et d'autant plus vite que le taux est élevé.

### ④ Micro-exercices

**M2.1** Dériver $g(S)=\ln(S/K)$ par rapport à $S$ ($K$ constant).
**M2.2** Dériver $h(T)=\sigma\sqrt T$ par rapport à $T$.
**M2.3** Dériver $\phi(x)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2}$ par rapport à $x$.

<details><summary><b>Corrigés M2</b></summary>

**M2.1** $\ln(S/K)=\ln S-\ln K$ (M1) ; $\ln K$ est une constante, dérivée nulle.
Donc $g'(S)=\boxed{1/S}$.

**M2.2** $h(T)=\sigma T^{1/2}$, donc
$h'(T)=\sigma\cdot\frac12T^{-1/2}=\boxed{\frac{\sigma}{2\sqrt T}}$.
**Reconnais ce terme :** c'est exactement celui qui apparaît dans le **theta**
(§6.5). Le theta vient de la dérivée de $\sqrt T$ — voilà pourquoi la valeur
temps s'effondre en accéléré près de l'échéance : la dérivée $\frac{1}{2\sqrt T}$
**explose** quand $T\to0$.

**M2.3** Chaîne : extérieur $e^u$ (dérivée $e^u$), intérieur $u=-x^2/2$
(dérivée $-x$) :
$$\phi'(x)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2}\times(-x)=\boxed{-x\,\phi(x)}$$
Jolie propriété : la dérivée de la densité normale, c'est elle‑même fois $-x$.
</details>

---

## M3 — Approximations locales (développements limités)

> **C'est le module de ta capture d'écran.** Prends‑le lentement, tout le
> reste en découle.

### ① À quoi ça sert
À remplacer une fonction compliquée par une **droite** (ou une parabole) quand
on regarde de très près. C'est ce qui permet : la limite $e^{rT}$, l'approx du
call ATM $0{,}4\sigma\sqrt T S$, et le lemme d'Itô lui‑même.

### ② Le rappel — l'idée avant les formules

Zoome sur une courbe lisse, très fort, autour d'un point. **Elle ressemble à
une droite.** C'est tout ce qu'est un développement limité : *près de zéro,
je remplace la courbe par sa tangente*. Si je veux plus de précision,
j'ajoute un terme en $x^2$ (une parabole).

**Les trois DL du J1** (valables quand $x$ est **petit**, disons $|x|<0{,}1$) :

$$e^{x}\approx1+x\qquad \ln(1+x)\approx x\qquad \sqrt{1+x}\approx1+\frac{x}{2}$$

Et avec le terme suivant, si on veut être plus précis :
$$e^{x}\approx1+x+\frac{x^2}{2}\qquad\ln(1+x)\approx x-\frac{x^2}{2}$$

**Vérifions que ce n'est pas du bluff** — $x=0{,}1$ (déjà « grand ») :

| | valeur exacte | $1+x$ | $1+x+\frac{x^2}{2}$ |
|---|---|---|---|
| $e^{0,1}$ | $1{,}105171$ | $1{,}1$ | $1{,}105$ |
| $\ln(1{,}1)$ | $0{,}095310$ | $0{,}1$ | $0{,}095$ |

Et pour $x=0{,}01$ :

| | exact | $1+x$ |
|---|---|---|
| $e^{0,01}$ | $1{,}0100502$ | $1{,}01$ |
| $\ln(1{,}01)$ | $0{,}0099503$ | $0{,}01$ |

**Conclusion :** plus $x$ est petit, plus l'approximation est bonne — et
l'erreur diminue **beaucoup** plus vite que $x$ (elle est en $x^2$). Quand tu
divises $x$ par 10, l'erreur est divisée par 100.

### ③ Que veut dire $O(1/m)$ ?

C'est **la seule notation intimidante de ta capture**, et elle ne dit rien de
plus que :

> « il reste des bricoles, et ces bricoles sont au plus de la taille de
> $1/m$ ; donc quand $m$ devient énorme, elles tendent vers zéro et je les
> jette. »

$O(\cdot)$ = « **un reste de l'ordre de** ». Rien à calculer. C'est une
façon d'écrire « et du menu fretin qui disparaît ». Quand tu lis
$O(1/m)$ dans une preuve, tu peux littéralement lire **« + poussière »**.

### ④ Micro-exercices

**M3.1** Approcher $e^{0{,}02}$ avec $1+x$. Exact : $1{,}020201$. Erreur ?
**M3.2** Approcher $\ln(1{,}05)$. Exact : $0{,}048790$. Commentaire ?
**M3.3** Une action baisse de 2 % puis remonte de 2 %. Est‑on revenu au départ ? Justifier avec un DL à l'ordre 2.

<details><summary><b>Corrigés M3</b></summary>

**M3.1** $1+0{,}02=1{,}02$ contre $1{,}020201$ : erreur $2\times10^{-4}$,
soit **2 points de base**. Négligeable pour un ordre de grandeur oral.

**M3.2** $\ln(1{,}05)\approx0{,}05$, exact $0{,}048790$.
**C'est le fameux « 5 % annuel = 4,88 % en continu ».** Un taux continu est
toujours **un peu plus petit** que le taux simple équivalent, parce que le
continu capitalise plus souvent.

**M3.3** Non. Le facteur total est
$$(1-0{,}02)(1+0{,}02)=1-0{,}02^2=0{,}9996$$
On a **perdu 0,04 %**. C'est le *volatility drag* : les allers‑retours coûtent,
et le coût est en **carré** de l'amplitude. **Tu viens de toucher du doigt
pourquoi la moyenne dépasse la médiane** en log‑normale — c'est le $-\sigma^2/2$
du module M7.
</details>

---

## M4 — La limite $(1+r/m)^{mT}\to e^{rT}$, refaite lentement

> C'est **exactement** la formule de ta capture. On la reprend en 5 étapes, et
> on commence par la comprendre **sans aucun calcul**.

### ① D'abord, le sens — zéro maths

Je place 100 € à 5 % pendant 1 an.

- Versé **1 fois** en fin d'année : $100\times1{,}05=105{,}000$
- Versé **2 fois** (2,5 % par semestre) : $100\times1{,}025^2=105{,}0625$ — un
  peu plus, car les intérêts du 1er semestre produisent eux‑mêmes des intérêts
- **12 fois** (mensuel) : $105{,}116$
- **365 fois** (quotidien) : $105{,}1267$
- **8 760 fois** (horaire) : $105{,}12710$
- **En continu** : $100\,e^{0{,}05}=105{,}12711$

**Regarde la colonne : ça converge.** Découper toujours plus finement ne fait
pas exploser le résultat, ça **plafonne**. Cette limite s'appelle $e^{0,05}$.
Voilà tout ce que dit la formule. Le reste, c'est de la plomberie.

### ② La plomberie, étape par étape

On veut $\lim_{m\to\infty}\left(1+\frac{r}{m}\right)^{mT}$.

**Étape 1 — passer au log.** Une puissance est pénible à manipuler ; un log la
transforme en produit (M1). On pose $A_m=\left(1+\frac{r}{m}\right)^{mT}$ :
$$\ln A_m=mT\cdot\ln\left(1+\frac{r}{m}\right)$$

**Étape 2 — l'ingrédient clé.** $m$ devient énorme, donc $\frac{r}{m}$ devient
**minuscule**. Or pour $x$ petit, $\ln(1+x)\approx x$ (M3) ! Ici $x=\frac{r}{m}$ :
$$\ln\left(1+\frac{r}{m}\right)\approx\frac{r}{m}$$

**Étape 3 — remplacer.**
$$\ln A_m\approx mT\times\frac{r}{m}=rT$$
**Le $m$ se simplifie.** C'est tout le tour de passe‑passe : le $m$ qui
multiplie annule le $m$ qui divise.

**Étape 4 — le reste.** L'approximation de l'étape 2 n'est pas exacte : il
reste des poussières, notées $O(1/m)$. Multipliées par $mT$, elles restent de
taille $\sim T/m\to0$. **Donc elles disparaissent.**

**Étape 5 — revenir de l'autre côté du log.** Si $\ln A_m\to rT$, alors
$$A_m\to e^{rT}.\qquad\blacksquare$$

### ③ Contrôle numérique
Avec $r=5\%$, $T=1$ : l'écart entre le mensuel ($1{,}051162$) et le continu
($1{,}051271$) vaut $1{,}1\times10^{-4}$. La théorie prédit un reste de l'ordre
de $\frac{r^2T}{2m}=\frac{0{,}0025}{24}=1{,}04\times10^{-4}$. **Ça colle.**

### ④ Micro-exercices

**M4.1** Sans calculatrice, ordonner : $\left(1+\frac{0{,}06}{2}\right)^2$, $e^{0{,}06}$, $1{,}06$.
**M4.2** Dans l'étape 3, pourquoi est‑ce important que le $m$ se simplifie ?
**M4.3** Convertir 6 % semestriel en taux continu. *(Formule : $r_c=m\ln(1+r_m/m)$.)*

<details><summary><b>Corrigés M4</b></summary>

**M4.1** $1{,}06<1{,}0609<1{,}061837$, soit
$$1{,}06\;<\;\left(1+\tfrac{0{,}06}{2}\right)^2\;<\;e^{0{,}06}$$
**Règle générale :** plus on capitalise souvent, plus on finit haut. Le continu
est la **borne supérieure**.

**M4.2** Parce que sinon la limite serait soit $0$, soit $+\infty$. C'est
l'équilibre exact entre « le taux par période tend vers 0 » et « le nombre de
périodes tend vers l'infini » qui produit un résultat **fini**. Deux effets
opposés qui se compensent : c'est ça, une forme indéterminée $1^\infty$.

**M4.3** $r_c=2\ln(1+0{,}03)=2\times0{,}029559=0{,}0591$, soit **5,91 %**.
Bien **inférieur** à 6 %, cohérent avec M3.2.
</details>

---

## M5 — La loi normale : $\phi$ et $N$

### ① À quoi ça sert
$N(d_1)$ et $N(d_2)$ **sont** la formule de Black-Scholes. Si tu sais lire ces
deux symboles, la formule cesse d'être un hiéroglyphe.

### ② Le rappel

Deux objets, à ne jamais confondre.

**$\phi(x)$ — la densité** (« la cloche ») :
$$\phi(x)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2}$$
C'est la **hauteur** de la courbe en cloche au point $x$. Maximale en $0$ où
elle vaut $\phi(0)=\frac{1}{\sqrt{2\pi}}\approx\mathbf{0{,}3989}$ — retiens
**« 0,4 »**, c'est le $0{,}4$ de l'approximation du call ATM (§5.2 du cours !).

**$N(x)$ — la fonction de répartition** (« l'aire cumulée ») :
$$N(x)=\mathbb P(Z\le x)=\text{aire sous la cloche à gauche de }x$$
C'est une **probabilité** : toujours entre 0 et 1, toujours croissante.

**Le lien :** $N$ est la primitive de $\phi$ ; autrement dit $N'(x)=\phi(x)$.
*Accumuler la hauteur donne l'aire.*

**Les valeurs à connaître :**

| $x$ | $-2$ | $-1$ | $0$ | $1$ | $1{,}645$ | $1{,}96$ | $2$ |
|---|---|---|---|---|---|---|---|
| $N(x)$ | $0{,}023$ | $0{,}159$ | $\mathbf{0{,}5}$ | $0{,}841$ | $0{,}95$ | $0{,}975$ | $0{,}977$ |

**La symétrie, indispensable :**
$$\boxed{N(-x)=1-N(x)}$$
*Preuve visuelle :* la cloche est symétrique, donc l'aire à gauche de $-x$
égale l'aire à droite de $+x$, qui vaut $1-N(x)$. C'est **exactement** ce qui
transforme la formule du call en celle du put (§4.4 du cours).

**Approximation près de zéro** (utile en mental math) :
$$N(x)\approx0{,}5+0{,}4\,x\quad\text{pour }|x|<0{,}3$$

### ③ Exemple traité
*Dans l'exercice 5 du TD : $d_2=-0{,}2795$. Que vaut $N(d_2)$ et que signifie‑t‑il ?*
$N(-0{,}2795)=\mathbf{0{,}3899}$.
Approximation : $0{,}5-0{,}4\times0{,}2795=0{,}388$ — à un millième près, de tête.
**Sens :** il y a environ **39 % de probabilité (risque-neutre) que l'option
finisse dans la monnaie.** Cohérent : le strike 105 est au-dessus du spot 100,
donc moins d'une chance sur deux.

### ④ Micro-exercices

**M5.1** Que vaut $N(0)$ ? Pourquoi, sans calcul ?
**M5.2** Sachant $N(1)=0{,}841$, calculer $N(-1)$.
**M5.3** $\phi$ peut-elle dépasser 1 ? $N$ peut-elle dépasser 1 ?
**M5.4** Estimer $N(0{,}2)$ de tête, puis comparer à $0{,}579260$.

<details><summary><b>Corrigés M5</b></summary>

**M5.1** $N(0)=\mathbf{0{,}5}$. La cloche est symétrique autour de 0 : la moitié
de l'aire est à gauche. Concrètement : une option **au strike forward** a ~50 %
de finir ITM — c'est le §2.4 du cours ($C=P$ à l'ATM forward).

**M5.2** $N(-1)=1-N(1)=1-0{,}841=\mathbf{0{,}159}$.

**M5.3** $\phi$ **oui** (c'est une hauteur, pas une probabilité — pour une
normale très resserrée elle dépasse largement 1). $N$ **non, jamais** : c'est
une probabilité, plafonnée à 1.

**M5.4** $0{,}5+0{,}4\times0{,}2=\mathbf{0{,}58}$. Exact : $0{,}5793$.
Erreur : 7 dix-millièmes, de tête.
</details>

---

## M6 — Somme d'exponentielles et complétion du carré

### ① À quoi ça sert
**Uniquement** à comprendre l'étape 5 de la démonstration de Black-Scholes
(§4.4), celle où $N(d_1)$ apparaît « par magie ». C'est le seul passage
calculatoire dur du J1 — et c'est un simple exercice de collège déguisé.

### ② Le rappel

**Compléter le carré**, c'est réécrire $z^2+bz$ sous la forme
$(z+\tfrac{b}{2})^2-\tfrac{b^2}{4}$. Rien de plus. Tu l'as fait au lycée pour
résoudre les équations du second degré.

Dans la démo de BS, on rencontre l'exposant
$$-\frac{z^2}{2}+sz$$
On factorise par $-\frac12$ :
$$-\frac{z^2}{2}+sz=-\frac12\left(z^2-2sz\right)$$
Puis on complète : $z^2-2sz=(z-s)^2-s^2$. Donc
$$-\frac12\left[(z-s)^2-s^2\right]=\boxed{-\frac{(z-s)^2}{2}+\frac{s^2}{2}}$$

**Pourquoi c'est utile.** À gauche, l'exposant contient un $z$ « en trop ». À
droite, on a **la même cloche, simplement décalée de $s$**, multipliée par une
constante $e^{s^2/2}$ qui sort de l'intégrale.

**En une phrase, ce que fait cette astuce dans BS :**
> Multiplier une gaussienne par $e^{sz}$, c'est **déplacer son centre de $s$**
> (et récupérer un facteur constant au passage).

C'est *toute* la raison pour laquelle la borne d'intégration passe de $-d_2$ à
$-d_2-s$, c'est-à-dire pourquoi le second terme fait apparaître
$$d_1=d_2+\sigma\sqrt T.$$

### ③ Exemple traité
*Vérifier l'identité avec $z=1$ et $s=0{,}3$.*
Gauche : $-\frac{1}{2}+0{,}3=-0{,}2$.
Droite : $-\frac{(1-0{,}3)^2}{2}+\frac{0{,}09}{2}=-0{,}245+0{,}045=-0{,}2$. ✔

### ④ Micro-exercices

**M6.1** Compléter le carré dans $z^2+4z$.
**M6.2** Réécrire $-\frac{z^2}{2}+2z$ sous la forme $-\frac{(z-a)^2}{2}+c$.
**M6.3** Dans la démo BS, on a $s=\sigma\sqrt T$. De combien la cloche est-elle décalée, et quel objet du cours cela fait-il apparaître ?

<details><summary><b>Corrigés M6</b></summary>

**M6.1** $z^2+4z=(z+2)^2-4$.

**M6.2** $-\frac12(z^2-4z)=-\frac12[(z-2)^2-4]=-\frac{(z-2)^2}{2}+2$.
Donc $a=2$, $c=2$.

**M6.3** Décalage de $\sigma\sqrt T$. Cela transforme $d_2$ en
$d_2+\sigma\sqrt T=\mathbf{d_1}$. **C'est l'origine exacte de $N(d_1)$** dans la
formule — et la raison pour laquelle $d_1>d_2$ toujours.
</details>

---

## M7 — La log-normale et le fameux $-\sigma^2/2$

### ① À quoi ça sert
À comprendre pourquoi $S_T$ ne peut pas devenir négatif, et d'où sort ce
$-\frac{\sigma^2}{2}$ qui traîne dans tout le cours (§4.2) et dans $d_1,d_2$.

### ② Le rappel

**Définition.** $X$ est **log-normale** si $\ln X$ est normale. Autrement dit :
la normale décrit les **rendements en log**, la log-normale décrit **le prix**.

**Deux conséquences immédiates :**
1. $X=e^{(\text{quelque chose de normal})}>0$ : **un prix reste positif.** C'est
   la raison n°1 de ce choix de modèle.
2. La distribution est **asymétrique** : queue longue à droite (une action peut
   faire ×10, elle ne peut pas faire −200 %).

**Le résultat central** (celui qui produit le $-\sigma^2/2$) :
$$\boxed{\mathbb E\left[e^{Y}\right]=e^{\;\mathbb E[Y]+\frac12\mathrm{Var}(Y)}}
\qquad\text{pour }Y\text{ normale}$$

**Traduction :** l'espérance d'une exponentielle **n'est pas** l'exponentielle
de l'espérance. Il y a un **bonus** $+\frac12\mathrm{Var}$, dû à la convexité de
$e^x$ (inégalité de Jensen). Plus c'est volatil, plus la moyenne est tirée vers
le haut par les scénarios extrêmes.

**Application au GBM.** On veut que le prix moyen croisse à $\mu$, c'est-à-dire
$\mathbb E[S_T]=S_0e^{\mu T}$. On écrit
$S_T=S_0e^{Y}$ avec $Y$ normale de variance $\sigma^2T$. D'après la formule :
$$\mathbb E[S_T]=S_0\,e^{\mathbb E[Y]+\frac12\sigma^2T}$$
Pour que ça donne $S_0e^{\mu T}$, il faut **obligatoirement**
$$\mathbb E[Y]=\mu T-\frac{\sigma^2}{2}T
\quad\Longrightarrow\quad\boxed{\;\mathbb E[\ln S_T]=\ln S_0+\left(\mu-\frac{\sigma^2}{2}\right)T\;}$$

**Le $-\sigma^2/2$ n'est donc pas un ajustement arbitraire : c'est le prix à
payer pour que la moyenne reste $\mu$.**

**Moyenne vs médiane :**
$$\mathbb E[S_T]=S_0e^{\mu T}\qquad\text{médiane}(S_T)=S_0e^{(\mu-\frac{\sigma^2}{2})T}$$
La moyenne est **au-dessus** de la médiane. C'est le *volatility drag* que tu as
déjà rencontré en **M3.3** (−2 % puis +2 % ⇒ perte de 0,04 %).

### ③ Exemple traité
*$S_0=100$, $\mu=10\%$, $\sigma=30\%$, $T=1$ an.*
- Moyenne : $100e^{0{,}10}=\mathbf{110{,}52}$
- Médiane : $100e^{0{,}10-0{,}045}=100e^{0{,}055}=\mathbf{105{,}65}$

Écart : **4,86**. Plus d'une chance sur deux de finir **sous** la moyenne. Le
« rendement moyen » est trompeur — c'est le genre de remarque qui fait bonne
impression en entretien.

### ④ Micro-exercices

**M7.1** Pourquoi ne modélise-t-on pas $S_T$ directement par une normale ?
**M7.2** Avec $\sigma=20\%$, $T=1$ : de combien la médiane est-elle en dessous (en %) ?
**M7.3** Si $\sigma\to0$, que devient l'écart moyenne/médiane ? Cohérent ?

<details><summary><b>Corrigés M7</b></summary>

**M7.1** Une normale prend des valeurs **négatives** avec probabilité non nulle.
Un prix négatif n'a pas de sens (hors WTI avril 2020, précisément parce que le
**stockage physique** avait saturé — l'exception qui confirme la règle et qui
relie au module commodities, §1.5).

**M7.2** $\frac{\sigma^2}{2}=\frac{0{,}04}{2}=2\%$. La médiane est ~2 % sous la
moyenne.

**M7.3** L'écart tend vers **0**. Cohérent : sans volatilité, il n'y a qu'un
seul scénario, donc moyenne = médiane. **Toute la différence vient du risque.**
</details>

---

## M8 — Dérivées partielles et règle de la chaîne

### ① À quoi ça sert
Le prix d'une option dépend de **plusieurs** variables à la fois ($S$, $t$,
$\sigma$, $r$). Chaque grec est une dérivée **par rapport à une seule**, les
autres gelées. C'est le langage de l'EDP (§4.3).

### ② Le rappel

**Dérivée partielle** $\frac{\partial V}{\partial S}$ : je dérive par rapport à
$S$ **en traitant $t$, $\sigma$, $r$ comme des constantes**. Le symbole rond
$\partial$ ne dit rien d'autre que « il y a d'autres variables, je les gèle ».

**Le dictionnaire grecs ↔ dérivées** — à lire de gauche à droite :

| Grec | Notation | En français |
|---|---|---|
| $\Delta$ | $\frac{\partial V}{\partial S}$ | sensibilité au **spot** |
| $\Gamma$ | $\frac{\partial^2V}{\partial S^2}$ | sensibilité **du delta** au spot |
| $\nu$ (véga) | $\frac{\partial V}{\partial\sigma}$ | sensibilité à la **vol** |
| $\Theta$ | $\frac{\partial V}{\partial t}$ | sensibilité au **temps** |
| $\rho$ | $\frac{\partial V}{\partial r}$ | sensibilité au **taux** |

**Une fois ce tableau lu, l'EDP de Black-Scholes**
$$\frac{\partial V}{\partial t}+(r-q)S\frac{\partial V}{\partial S}
+\frac12\sigma^2S^2\frac{\partial^2V}{\partial S^2}=rV$$
**se lit en français :**
$$\Theta+(r-q)S\Delta+\tfrac12\sigma^2S^2\Gamma=rV$$
> « L'usure du temps, plus le portage de ma position en delta, plus le gain de
> convexité apporté par le gamma, doit rapporter exactement le taux sans
> risque. »

Ce n'est plus une équation aux dérivées partielles : c'est une **phrase de
trader**. Et c'est la ligne la plus rentable du J1.

### ③ Exemple traité
*Soit $V=S^2t$. Calculer les dérivées partielles.*
- $\frac{\partial V}{\partial S}=2St$ ($t$ gelé)
- $\frac{\partial^2V}{\partial S^2}=2t$
- $\frac{\partial V}{\partial t}=S^2$ ($S$ gelé)

### ④ Micro-exercices

**M8.1** $V=e^{-rT}K$. Calculer $\frac{\partial V}{\partial r}$. Signe ? Sens économique ?
**M8.2** Si $\Gamma>0$, que dit le terme $\frac12\sigma^2S^2\Gamma$ sur le signe de $\Theta$ (cas $r=0$, $\Delta=0$) ?
**M8.3** Pourquoi le véga s'écrit-il $\partial V/\partial\sigma$ alors que $\sigma$ est censée être **constante** dans BS ?

<details><summary><b>Corrigés M8</b></summary>

**M8.1** $\frac{\partial V}{\partial r}=-TKe^{-rT}<0$. **Négatif** : si les taux
montent, la valeur actuelle du strike baisse. C'est exactement le $\rho$ négatif
du **put** (§6.6).

**M8.2** L'EDP devient $\Theta+\frac12\sigma^2S^2\Gamma=0$, donc
$$\Theta=-\tfrac12\sigma^2S^2\Gamma<0.$$
**Long gamma ⇒ theta négatif.** Tu viens de redémontrer seul « le theta est le
loyer du gamma » (§4.3, étape 5).

**M8.3** Excellente question, et c'est **une incohérence assumée du modèle**. BS
suppose $\sigma$ constante, donc en toute rigueur le véga devrait être nul.
Mais on s'en sert quand même comme mesure de sensibilité au paramètre qu'on a
choisi. **C'est précisément ce que dit la phrase du cours** : « Black-Scholes
est faux mais universel, on s'en sert comme d'un dictionnaire prix ↔ vol ». Si
un intervieweur te pose cette question, il teste si tu récites ou si tu
comprends.
</details>

---

# Auto-test de sortie M0 (10 questions, 10 minutes)

Réponds sans revenir en arrière. **7/10 = tu peux attaquer le J1 sereinement.**

1. Simplifier $e^{rT}e^{-qT}$.
2. $\ln(a/b)=$ ?
3. Dérivée de $e^{-rT}$ par rapport à $T$ ?
4. $e^{0{,}03}\approx$ ? (de tête)
5. Que vaut $N(0)$ ?
6. $N(-1{,}5)$ en fonction de $N(1{,}5)$ ?
7. $\phi(0)\approx$ ? Où le retrouve-t-on dans le J1 ?
8. Pourquoi $S_T$ est-elle log-normale et non normale ?
9. D'où vient le $-\sigma^2/2$ ?
10. Traduire en français : $\Theta+\frac12\sigma^2S^2\Gamma=0$.

<details><summary><b>Corrigés de l'auto-test</b></summary>

1. $e^{(r-q)T}$ — la formule du forward.
2. $\ln a-\ln b$.
3. $-re^{-rT}$.
4. $\approx1{,}03$ (exact $1{,}0305$).
5. $0{,}5$.
6. $1-N(1{,}5)=0{,}0668$.
7. $0{,}3989\approx0{,}4$ ; c'est le $0{,}4$ de l'approximation du call ATM
   $C\approx0{,}4\,\sigma\sqrt T\,S$.
8. Parce qu'une normale peut être négative, et qu'un prix ne peut pas l'être.
   On modélise donc le **log** du prix par une normale.
9. De $\mathbb E[e^Y]=e^{\mathbb E Y+\frac12\mathrm{Var}Y}$ : c'est la correction
   nécessaire pour que le prix **moyen** croisse bien à $\mu$.
10. « Le theta est le loyer du gamma » : ce que je gagne en convexité, je le
    paie en usure du temps.
</details>

---

## Où retourner maintenant

| Si ce module t'a débloqué… | …va lire dans le cours J1 |
|---|---|
| M1, M3, M4 | **§0.1** (la formule de ta capture) puis **§1** forwards |
| M2, M8 | **§6** les grecs |
| M5 | **§5** lecture de $N(d_1)$, $N(d_2)$ |
| M6, M7 | **§4.2 et §4.4** la démonstration de BS |

**Conseil de rythme pour aujourd'hui (06/09).** Le programme dit « dimanche
off », mais tu as pris du retard sur J1 : fais **M0 (1 h 30) + §0 et §1 du
cours J1 (1 h)**. Tu clôtures J1 demain avec les §2 à §7. Tu ne perds rien :
le J2 « grecs » s'appuie sur §6, que M2 et M8 viennent de préparer.
