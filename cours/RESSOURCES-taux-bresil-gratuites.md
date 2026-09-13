# Taux et Bresil — les sources gratuites, et dans quel ordre

> **Pourquoi ce document existe.** Tu reponds sans probleme jusqu'a la question
> 78 : le FX est acquis. A partir de la, ca coince, et ce n'est pas un hasard —
> **les questions 101 a 125 ne sont pas du change, ce sont des taux**. Selic,
> courbe, dette, cupom cambial : c'est du fixed income habille en FX.
>
> **Ce n'est pas un cours.** Ce sont des liens, tous **gratuits et legaux**, avec
> pour chacun ce qu'il faut y prendre et ce qu'il faut ignorer. Tu as constate
> qu'il n'existe pas de livre sur les derives bresiliens : c'est exact. **Le
> sujet ne vit pas dans les livres, il vit dans la documentation officielle.**
> C'est une bonne nouvelle : ces sources sont plus a jour qu'un manuel, et
> personne parmi tes concurrents ne les ouvre.

---

## 0. Le diagnostic, en une ligne

Le trou n'est pas bresilien, il est **obligataire**. Tu sais ce qu'est un
forward ; tu ne sais pas encore lire une courbe. Or au Bresil, **le change ne se
comprend pas sans les taux** : le forward USD/BRL est construit sur l'ecart de
taux, le cupom cambial est un taux, le carry est un ecart de taux, et la prime
de risque du real est une prime budgetaire lisible sur la courbe locale.

**Donc l'ordre est : les taux d'abord, le Bresil ensuite.** Pas l'inverse.

---

## 1. 🥇 La priorite absolue : le cours du Tesouro Nacional

**Gratuit, officiel, en portugais, avec certificat.** C'est la meilleure
ressource existante sur les taux bresiliens, et elle est publique.

**Page du cours :**
`tesourodireto.com.br/educacional/curso-tesouro-direto.htm`

**Les PDF en telechargement direct** (depot officiel de l'ENAP, l'ecole
nationale d'administration publique bresilienne) :
`repositorio.enap.gov.br/handle/1/6248`

Tu y trouves le *Guia do Investidor*, les modules 1 a 4, et surtout **cinq
chapitres « Topicos Avancados »** — c'est la que se trouve la matiere utile.

### Ce que tu y prends, module par module

| Module | Contenu | Utile pour |
|---|---|---|
| 1-2 | Bases, orientation vers le particulier | **Survoler**, c'est de l'education financiere grand public |
| 3-4 | Les titres en detail, fiscalite, liquidite | **Lire** : c'est la typologie de la dette bresilienne |
| **Topicos Avancados 1-5** | 🔴 **Marcacao a mercado, formation des prix, courbe** | **Le cœur. C'est pour ca qu'on ouvre ce cours.** |

### Les cinq titres a savoir distinguer

C'est la premiere chose qu'on te demandera si on parle de dette bresilienne.

| Nom de marche | Nom technique | Nature | Ce que ca signifie |
|---|---|---|---|
| Tesouro Prefixado | **LTN** | Taux fixe, zero coupon | Le taux est fige a l'achat, tout est verse a l'echeance |
| Tesouro Prefixado c/ juros | **NTN-F** | Taux fixe, coupons semestriels | Meme chose, mais avec flux intermediaires |
| Tesouro Selic | **LFT** | Post-fixe sur la Selic | Suit le taux directeur au jour le jour : **tres faible volatilite de prix** |
| Tesouro IPCA+ | **NTN-B Principal** | Inflation + taux reel | Protege le pouvoir d'achat, sans coupon |
| Tesouro IPCA+ c/ juros | **NTN-B** | Inflation + taux reel, coupons | La reference du marche long bresilien |

> 🔑 **Le point qui vaut de l'or en entretien.** La **LFT** est la clef de voute
> du systeme. Comme elle se reevalue chaque jour sur la Selic, **son prix ne
> bouge quasiment pas quand les taux montent** : sa duration est proche de zero.
> C'est pour ca que l'Etat bresilien peut placer une dette enorme malgre une
> Selic a 14 % — il vend a ses banques un titre sans risque de taux.
>
> **La consequence, et c'est la vraie analyse :** cela rend la politique
> monetaire moins efficace. Une hausse de la Selic ne fait pas perdre d'argent
> aux detenteurs de LFT, elle les enrichit immediatement. **Le canal de
> transmission par les effets de richesse est casse.** Aucun candidat
> generaliste ne sait dire ca.

**Temps a y passer :** trois heures sur les Topicos Avancados. Le reste se
survole.

---

## 2. La Selic, le CDI et le DI futur — la trilogie a ne pas confondre

Il n'existe pas de livre la-dessus en francais. Il existe des pages officielles.

**Le BCB explique la Selic :** `bcb.gov.br/controleinflacao/taxaselic`

### Les trois notions, et pourquoi on les confond

**La Selic meta** est la cible fixee par le Copom — l'equivalent du taux
directeur de la Fed. **La Selic over** est le taux effectivement constate au
jour le jour sur les operations garanties par titres publics. **Le CDI** est le
taux des depots interbancaires, fixe par le marche, et il colle a la Selic sans
etre identique.

> **Pourquoi ca compte.** Le CDI est **le benchmark de toute la finance
> bresilienne**. Un fonds se mesure en « pourcentage du CDI », une dette
> d'entreprise se cote « CDI + spread ». Dire « la Selic » quand on parle d'un
> produit de marche est une approximation de touriste : **le marche parle en
> CDI.**

### Le contrat DI1 — l'instrument le plus important du Bresil

Specifications reelles de la B3 : `b3.com.br`, section Produits, Taux d'interet.

- **Sous-jacent** : le taux moyen des depots interbancaires d'un jour, capitalise
  jusqu'a l'echeance.
- **Nominal** : **100 000 points a l'echeance**, chaque point valant 1 real.
- **Cotation** : en **taux annuel, base 252 jours ouvres** — pas en jours
  calendaires. C'est une specificite bresilienne.
- **Prix** : PU = 100 000 / (1 + taux)^(jours ouvres / 252).
- **Reglement** : financier, tous les mois d'echeance.

**Le piege de vocabulaire qui trahit un debutant :** acheter un contrat DI1,
c'est acheter du **PU**, donc **vendre du taux**. La position s'appelle
*aplicada*. Qui parie sur une baisse des taux est acheteur du contrat. **L'ordre
parait inverse a quelqu'un qui vient du future classique** — c'est
exactement pour ca que le savoir impressionne.

> **La phrase d'entretien :** *« La courbe bresilienne ne se lit pas sur les
> obligations, elle se lit sur les DI futurs. C'est la que se forme le prix, et
> c'est en base 252 jours ouvres, pas en jours calendaires. »*

---

## 3. La source la plus rentable de toutes : le RPM

**Le *Relatorio de Politica Monetaria* du Banco Central do Brasil.** Trimestriel,
gratuit, environ 110 pages, PDF direct :

`bcb.gov.br/publicacoes/relatorioinflacao`

Le fichier suit un format previsible :
`bcb.gov.br/content/ri/relatorioinflacao/AAAAMM/rpmAAAAMMp.pdf`
— par exemple `202606` pour juin 2026.

**Pourquoi c'est la meilleure source du lot.** C'est le document que **lisent
reellement les strategists** que tu suis sur LinkedIn. Il contient l'inflation,
l'activite, les comptes exterieurs, la situation budgetaire, et les projections
de la banque centrale elle-meme.

**Comment le lire sans y passer la semaine :** uniquement le **resume executif**
et la section **contas externas**. Vingt pages, une heure.

> 🔑 **Le detail que personne ne connait : le QPC.** Le *Questionario
> Pre-Copom* est une enquete que le BCB mene aupres des analystes **avant chaque
> reunion**, et dont il publie les resultats dans le RPM. Une des questions
> porte sur l'evaluation de la situation budgetaire.
>
> **Pouvoir dire *« au dernier QPC, la majorite des analystes ne voyait pas de
> degradation budgetaire malgre le deficit »* est un marqueur de lecture reelle.**
> On ne peut pas inventer ca, et ca ne s'apprend dans aucun livre.

**A cote, deux autres sources du BCB :**

- **Le rapport Focus**, hebdomadaire, publie chaque lundi : les anticipations de
  marche pour la Selic, l'inflation, le change et le PIB. **Une page, deux
  minutes.** C'est le document le plus lu du Bresil chaque semaine.
- **Le SGS**, *Sistema Gerenciador de Series Temporais* :
  `bcb.gov.br/estatisticas/sgs`. Toutes les series historiques, exportables, avec
  une **API publique**. C'est la que ton Python sert vraiment — et le dire en
  entretien montre l'outil au service de la decision.

---

## 4. Le Tresor : la dette, mois par mois

**Le *Relatorio Mensal da Divida Publica Federal*** du Tesouro Nacional :
`tesourotransparente.gov.br`

Gratuit, mensuel. C'est de la que viennent les chiffres que tu cites deja :
l'encours de **8 635 milliards de reais**, la part de **96,2 % en monnaie
locale**, le cout moyen de **13,92 %**.

**Ce qu'il faut y regarder, et c'est trois choses :**

1. **La composition par indexation** — quelle part en prefixado, en Selic, en
   IPCA, en devises. **C'est le vrai indicateur de vulnerabilite.**
2. **La duration moyenne et le profil d'echeances** — combien de dette arrive a
   maturite dans les douze mois. Un mur de refinancement est un risque.
3. **La part detenue par les non-residents** — c'est le lien direct avec le FX :
   quand les etrangers sortent de la dette locale, ils vendent des reals.

> **L'analyse a une phrase :** *« La vulnerabilite bresilienne n'est pas le
> niveau de dette, c'est sa structure : courte, chere, et massivement indexee
> sur le taux directeur. Une hausse de Selic se transmet au service de la dette
> en quelques mois, pas en quelques annees. »*

---

## 5. Pour l'Amerique latine hors Bresil

Tous gratuits, tous en espagnol — et c'est la que ton espagnol devient
verifiable.

| Institution | Publication | Rythme |
|---|---|---|
| **Banxico** (Mexique) | *Informe Trimestral* + comunicados | Trimestriel |
| **BanRep** (Colombie) | *Informe de Politica Monetaria* + **minutas** | Trimestriel |
| **BCCh** (Chili) | **IPoM** — *Informe de Politica Monetaria* | Trimestriel |
| **CEPAL** | *Estudio Economico de America Latina* | Annuel, gratuit en PDF |
| **BID** | Rapports macro regionaux | Variable |

**Le plus utile des cinq : les *minutas* du BanRep.** Elles detaillent les
**desaccords internes du comite**, vote par vote. C'est de la matiere brute qu'on
ne trouve nulle part ailleurs, et citer un desaccord de comite en entretien est
un signal de lecture de source primaire.

---

## 6. L'histoire des banques bresiliennes — les faits, sans livre

Tu cherchais une ressource la-dessus : voici l'essentiel, verifie. C'est de la
culture generale de candidat, pas de la technique.

**Le Banco do Brasil (1808).** Cree a l'arrivee de la famille royale portugaise
en fuite devant Napoleon. **Il a longtemps fait office de banque centrale** :
depots, escompte, emission de monnaie.

**La SUMOC (1945).** *Superintendencia da Moeda e do Credito*, creee par Getulio
Vargas comme etape transitoire vers une vraie banque centrale.

**Le Banco Central do Brasil (31 decembre 1964, loi 4.595).** Il commence ses
activites en mars 1965. **Le Bresil n'a donc de banque centrale que depuis
soixante ans** — c'est tres recent, et ca explique beaucoup de la fragilite
institutionnelle.

**1994 : le Plano Real.** La stabilisation qui met fin a l'hyperinflation.

**1999 : le ciblage d'inflation**, adopte juste apres le passage au flottement.

**Fevrier 2021 : la loi complementaire 179**, qui donne au BCB son **autonomie
formelle** : mandats fixes pour le president et les directeurs, decales du
calendrier politique. **Nuance a connaitre : autonomie n'est pas independance.**
La cible d'inflation reste fixee par le **CMN**, le Conseil monetaire national,
ou siege le ministre des Finances.

### Le paysage bancaire actuel

| Banque | Fondation | Nature |
|---|---|---|
| **Itau Unibanco** | Fusion **2008** | La plus grande banque privee d'Amerique latine |
| **Banco do Brasil** | **1808** | Publique, la plus ancienne du pays |
| **Bradesco** | 1943 | Privee |
| **BTG Pactual** | 1983 | La banque d'investissement de reference de la region |
| **Caixa Economica Federal** | 1861 | Publique, logement et social |
| **BNDES** | 1952 | Banque publique de developpement |

> **Le fait a retenir, un seul :** la **fusion Itau-Unibanco de novembre 2008**,
> en pleine crise financiere mondiale, a cree un groupe pesant environ **18 % du
> reseau bancaire bresilien**. C'est l'evenement structurant du secteur, et il
> montre que la crise de 2008 a **concentre** le systeme bresilien au lieu de le
> fragiliser.

---

## 7. Le plan des trois prochaines semaines

Tu as deja le socle FX. Il s'agit d'ajouter une couche, pas de tout reprendre.

| Semaine | Quoi | Duree |
|---|---|---|
| **1** | Topicos Avancados du Tesouro Direto (ch. 1 a 5) + les cinq titres | 3 h |
| **1** | La page Selic du BCB + specifications DI1 sur la B3 | 1 h |
| **2** | Le dernier RPM : resume executif et comptes exterieurs | 1 h 30 |
| **2** | Le dernier rapport mensuel de la dette : les trois points de la section 4 | 1 h |
| **3** | Un IPoM chilien **ou** une minuta du BanRep, en espagnol | 1 h 30 |
| **3** | Le Focus du lundi, toutes les semaines — a prendre comme habitude | 2 min/sem |

**Neuf heures au total.** C'est le complement exact des questions 101 a 125.

> **La routine a installer des maintenant, et elle coute deux minutes :** le
> **Focus du lundi matin**. Au bout d'un mois, tu sauras dire *« le consensus a
> revise la Selic de fin d'annee a la hausse depuis trois semaines »*. C'est
> exactement le genre de phrase qui fait dire a un recruteur que tu suis le
> marche pour de vrai.

---

## 8. Ce qu'il faut retenir de cette page

- **Ton trou n'est pas bresilien, il est obligataire.** Les questions 101-125
  sont des questions de taux deguisees en questions de change.
- **🥇 La ressource numero un est le cours gratuit du Tesouro Nacional**, et
  specifiquement ses cinq chapitres avances.
- **La LFT est le point de rupture a comprendre** : duration proche de zero,
  donc transmission monetaire amoindrie.
- **Le marche bresilien parle en CDI, pas en Selic**, et la courbe se lit sur
  les **DI futurs, en base 252 jours ouvres**.
- **Le RPM trimestriel et le Focus hebdomadaire** sont les deux documents que
  lisent les professionnels. Le **QPC** cache dedans est ton marqueur de lecture
  reelle.
- **Aucun livre n'existe sur les derives bresiliens : c'est un avantage.** La
  documentation officielle est gratuite, a jour, et personne ne l'ouvre.
