# 🧹 MÉNAGE DU 14 SEPTEMBRE 2026 — RETRAIT INTÉGRAL DU DOSSIER ALDRIN

## Contexte
Demande de Calvin : « voici les relations d'Aldrin (ne mélange pas avec les miennes), supprime Aldrin de ma stratégie ».
Le réseau LinkedIn d'Aldrin (671 relations) est un réseau **distinct** de celui de Calvin et ne doit
**jamais** alimenter les fichiers de Calvin, Cléanne ou Yasmine.

## ⛔ Règle permanente encodée
**Le réseau d'Aldrin est HORS PÉRIMÈTRE de cette stratégie. Ne jamais le mélanger avec les relations de Calvin.**
Cette règle est désormais écrite dans : `AUDIT_MASTER_RESEAU_GLOBAL_CALVIN.md` (en-tête),
`DOSSIER_DE_REPRISE_AGENT_ARENA.md` (bloc ⛔ en tête) et `GUIDE_FILTRES_RECHERCHE_RESEAU_2_POLES.md` (note).

## Ce qui a été retiré
| Élément | Action |
|---|---|
| `dossier-aldrin-minang/` (7 fichiers : packs mails, recruteurs, guide mobilité Europe, sponsors visa) | **Dossier supprimé intégralement** |
| `AUDIT_MASTER_RESEAU_GLOBAL_CALVIN.md` — section « 4. OPÉRATION VIANNEY-ALDRIN MINANG » (11 contacts : Martin Meurin, Robin Gervais, Simon Gotthardt, Noemie Caron, Daoud Sylla, Etienne Vial, Thomas Le Roy, Gabriel Soumbo, Mathieu Guilleminot, Alida Dembélé, Hugues Duron) | **Section supprimée** (l'audit passe de 4 à 3 opérations) |
| `GUIDE_FILTRES_RECHERCHE_RESEAU_3_POLES.md` — pôle 3 « Ingénieur / Génie Industriel / Supply Chain » | **Pôle supprimé**, fichier renommé `GUIDE_FILTRES_RECHERCHE_RESEAU_2_POLES.md` |
| `DOSSIER_DE_REPRISE_AGENT_ARENA.md` — section « 3. DOSSIER VIANNEY-ALDRIN MINANG » + arborescence | **Section supprimée**, arborescence mise à jour |
| `generate_handover_pdf.py` — footer, sous-titre « Opérations actives », section 5 du PDF | **Nettoyés** |
| `DOSSIER_DE_REPRISE_CHASSE_FO_CALVIN_MINANG.pdf` | **Régénéré sans Aldrin** (14/09/2026, vérifié : 0 mention) |

## Vérifications effectuées (14/09/2026)
1. **Cross-référence** : les 413 noms de la liste de relations d'Aldrin fournie ont été comparés à TOUS les
   fichiers restants → aucun contact Aldrin ne subsiste dans les sections Calvin / Cléanne / Yasmine.
   Seuls deux cas, tous deux documentés et volontaires :
   - **Calvin MINANG** : présent dans la liste d'Aldrin (connexion du 04/12/2022) — normal, c'est le candidat lui-même.
   - **Mehdi Saoud** : **homonymes ≠ même personne**. Celui de la stratégie Cléanne est
     « DAF @ LiveMentor & Co-fondateur @ startDAF » (`/in/mehdi-saoud/`) ; celui de la liste d'Aldrin est
     « Ingénieur industriel d'État / supply chain » (`/in/mehdi-saoud-652494203/fr/`). Profils LinkedIn distincts → **conservé**.
2. **Intégrité Calvin** : §1 FO de l'audit, CSV, campagnes, emails — intouchés (1 428+ relations conservées).
3. **Dossiers Cléanne et Yasmine** : intacts et toujours actifs.
4. **PDF** : régénéré via `generate_handover_pdf.py` nettoyé — 0 mention Aldrin/Vianney/« Génie Industriel » (vérifié par extraction de texte pypdf).

## ⚠️ Note sur le dépôt d'origine
Cette copie nettoyée vit dans le dépôt `Masterclass-front` (branche `arena/01a09ea2-masterclass-front`).
L'original dans `shockdesk` (branche `arena/01a05d5c`) **contient encore le dossier Aldrin** et n'est pas
modifiable depuis cette session. Voir les instructions de purge dans la conversation de passation.
