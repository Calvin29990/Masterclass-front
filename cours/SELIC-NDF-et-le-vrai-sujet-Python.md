# Selic, NDF, et ce que je t'ai mal dit sur Python

> Trois choses courtes. La première est une faute de ma part : j'ai écrit
> « Selic » 32 fois dans tes fiches sans jamais te dire ce que c'est.

---

# 1. La Selic — en 60 secondes

> **La Selic, c'est le taux directeur du Brésil. Point.**
>
> C'est l'équivalent exact du taux de la Fed aux États-Unis, ou du taux de
> dépôt de la BCE en zone euro. Le taux auquel la banque centrale prête aux
> banques, et donc le taux qui commande tous les autres taux du pays.

| Pays | Banque centrale | Nom du taux | Niveau aujourd'hui |
|---|---|---|---|
| 🇺🇸 États-Unis | Fed | *Fed funds rate* | 3,50-3,75 % |
| 🇪🇺 Zone euro | BCE | Taux de dépôt | 2,50 % |
| 🇧🇷 **Brésil** | **Banco Central do Brasil** | **Selic** | **14,00 %** |

**Le comité qui la décide s'appelle le Copom** — l'équivalent du FOMC américain.
Il se réunit toutes les 6 semaines. Prochaine réunion : **15-16 septembre**,
baisse attendue à 13,75 %.

## Pourquoi 14 %, c'est énorme

Parce que le Brésil a une **histoire d'hyperinflation** (des taux à plus de
40 % dans les années 90) et que la banque centrale y est, depuis, très
agressive. L'inflation tourne autour de 5 %, donc le **taux réel** — ce que tu
gagnes vraiment après inflation — est d'environ **9 %**.

> C'est le taux réel le plus élevé des grandes économies mondiales. **C'est
> toute la raison pour laquelle le carry trade brésilien existe.**

**À l'oral, dis simplement :** *« la Selic, le taux directeur brésilien »*.
Personne ne te demandera l'étymologie.

🇬🇧 *« The Selic is Brazil's policy rate — their equivalent of fed funds. »*

---

# 2. Le NDF — en 90 secondes

## Le problème qu'il résout

Tu es un fonds à Londres. Tu veux te couvrir contre une baisse du réal.
Tu voudrais faire un forward classique : dans 3 mois, j'échange des dollars
contre des réaux à un cours fixé aujourd'hui.

**Impossible.** Le réal n'est **pas librement convertible** : le Brésil contrôle
les mouvements de sa devise. Tu ne peux pas te faire livrer des réaux à
Londres, et tu n'as de toute façon pas de compte en réaux au Brésil.

## La solution

> **Le NDF — *non-deliverable forward*, forward non livrable.**
>
> C'est un forward où **personne ne livre la devise**. À l'échéance, on compare
> le cours convenu au cours officiel du jour, et **on se règle la différence en
> dollars**.

## L'exemple concret

Tu achètes 10 M USD/BRL à 3 mois, à **5,29**.

| À l'échéance, le fixing officiel est… | Ce qui se passe |
|---|---|
| **5,40** (le réal s'est affaibli) | Tu avais raison → **on te verse la différence en dollars** |
| **5,20** (le réal s'est renforcé) | Tu avais tort → **tu paies la différence en dollars** |

**Dans les deux cas : aucun réal ne change de main.** Tout se règle en dollars,
hors du Brésil.

## Le fixing — le mot qui compte

Le cours de référence n'est pas un prix de marché quelconque. C'est un **taux
officiel publié chaque jour par la banque centrale brésilienne : le PTAX**.

> **PTAX = le fixing officiel du réal.** C'est le chiffre contre lequel tous les
> NDF brésiliens se règlent.

Chaque devise non convertible a le sien : PTAX pour le réal, et il existe des
équivalents pour la roupie indienne, le won coréen, le peso chilien, le
renminbi offshore.

## Pourquoi c'est LE sujet de ton appel

**Les NDF, c'est comme ça que se traite tout le FX émergent depuis l'étranger.**
Et **CACIB a été élu meilleure maison de NDF en Asie**, avec des volumes en
hausse de 200 % après avoir refondu son offre électronique.

> Autrement dit : **le NDF électronique sur devises émergentes, c'est
> littéralement leur franchise.** Et c'est le croisement exact entre ton Brésil
> et leur métier.

🇬🇧 *« An NDF is a forward with no delivery — you cash-settle the difference in
dollars against an official fixing, the PTAX for the real. It's how EM
currencies trade offshore. »*

---

# 3. Python — j'ai eu tort, et voilà le vrai sujet

## Ce que j'ai mal formulé

J'ai écrit « arrête de parler comme un quant » et « ne dis jamais
scikit-learn ». **C'était trop brutal et ça t'a fait douter de quelque chose
qui est un vrai atout.**

> **Tes compétences Python ne sont pas un problème. Elles sont un
> différenciateur rare.** La plupart des candidats sales n'ont jamais écrit une
> ligne de code. Toi tu as automatisé des flux en production chez BPCE. Ça,
> c'est défendable, et tu dois le défendre.

## Le vrai sujet : ce n'est pas la compétence, c'est le signal

Le problème n'est pas que tu codes. C'est **ce que l'interlocuteur en conclut
sur le poste que tu vises**.

| Ce que tu dis | Ce qu'un sales entend |
|---|---|
| « scikit-learn, BigQuery, prédiction de vol » | *« Il veut aller en quant research. Ce n'est pas mon desk. »* |
| « j'automatise des flux, je sors un prix en 2 secondes » | *« Il coderait des outils pour mon desk. Je le veux. »* |

**Même compétence. Signal opposé.** Romain ne recrute pas pour la recherche
quantitative — il ne te recommandera pas pour un poste qu'il n'a pas.

## Donc : tu gardes tout, tu changes l'angle

> *« J'ai des bases solides en Python — chez BPCE j'ai automatisé des flux
> multi-actifs avec Bloomberg BQL, et j'ai codé mon propre terminal de marché
> et un pricer Black-Scholes.
>
> Sur un desk, je vois ça comme un avantage pratique : pouvoir sortir moi-même
> un carry, un point mort ou un forward en quelques secondes, sans dépendre de
> quelqu'un. Ce qui m'intéresse ce n'est pas le modèle pour le modèle, c'est de
> pouvoir répondre à une question de marché avant qu'elle ne soit périmée. »*

**Ce que fait cette version :**
1. Tu **revendiques** la compétence, tu ne la caches pas
2. Tu cites des **réalisations concrètes** (BQL en production, un terminal, un pricer)
3. Tu la relies à **un usage de desk**, pas à de la recherche
4. La dernière phrase dit que tu as compris que l'information a une durée de vie

🇬🇧 *« I'm solid in Python — I automated multi-asset flows at BPCE with
Bloomberg BQL and built my own market terminal. On a desk I see it as being
able to answer a market question before it goes stale, rather than modelling
for its own sake. »*

> 🔑 **La règle, reformulée proprement :** ne cache jamais ton code. **Dis
> toujours à quoi il sert sur un desk.** La compétence est un atout ; c'est
> seulement le vocabulaire de laboratoire qui égare ton interlocuteur.

---

# Récapitulatif

| | En une phrase |
|---|---|
| **Selic** | Le taux directeur du Brésil, 14 % — leur Fed funds |
| **Copom** | Le comité qui la décide, leur FOMC |
| **NDF** | Un forward sans livraison, réglé en dollars contre un fixing |
| **PTAX** | Le fixing officiel du réal, publié par la banque centrale |
| **Python** | Un atout à revendiquer — en disant ce qu'il décide, pas quelle librairie |
