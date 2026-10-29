# 05 — Sources de vérité et intégrations

## Ordre

1. Instruction humaine explicite et décision récente.
2. Documents canoniques du projet (`brain/`, registre DEC-006).
3. Registre atomique dans les collections Markdown (entrées JSONL, DEC-009).
4. Index SQLite, pour retrouver une source, pas pour la remplacer.
5. Conversation ou journal, à vérifier avant d'en faire une vérité durable.
6. GitHub, ClickUp, Notion : surfaces spécialisées — **jamais SoT silencieuse** (DEC-007).

ClickUp est une projection du local pour l'humain. Notion est un miroir optionnel. GitHub porte le code.

En cas de contradiction local ↔ distant : montrer les deux, dates et portée ; proposer un patch ; ne pas fusionner sans règle (DEC-007 : local gagne jusqu'à décision contraire explicite).

## Qui configure quoi

| Emplacement | Rôle |
| --- | --- |
| `brain-main/integrations/` | Contrat commun : permissions, limites, sync. |
| `.github/` à la racine | Configuration reconnue par GitHub pour ce dépôt. |
| `templates/project/.github/` | Même rôle, pour un futur projet. |
| `.clickup/` | Mapping listes / IDs ; `source_of_truth: local`. Pas une connexion ClickUp. |
| `.notion/` | Correspondance pages/bases. Pas une connexion Notion. |
| Client MCP | Authentification et secrets. Jamais dans Git. |

## Actions externes

Lecture selon les droits du compte. Création, modification, commentaire, assignation, fermeture ou suppression : approbation explicite de l'action précise, sauf autorisation déjà donnée. Le skill ClickUp dérive les écritures depuis le local (`brain/TASKS.md`).

Le cœur métier ne dépend pas de MCP ni d'un éditeur. MCP et CLI appelleront les mêmes services, quand ils existeront.
