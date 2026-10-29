# 05 — Sources de vérité et intégrations

## Ordre

1. Instruction humaine explicite et décision récente.
2. Documents canoniques du projet.
3. Registre, une fois son format adopté.
4. Index SQLite, pour retrouver une source, pas pour la remplacer.
5. Conversation ou journal, à vérifier avant d'en faire une vérité durable.
6. GitHub, ClickUp, Notion : sources spécialisées, citées, jamais synchronisées en silence.

En cas de contradiction, montrer les deux sources, leur date et leur portée. Ne pas fusionner sans règle.

## Qui configure quoi

| Emplacement | Rôle |
| --- | --- |
| `brain-main/integrations/` | Contrat commun : permissions, limites, synchronisation. |
| `.github/` à la racine | Configuration reconnue par GitHub pour ce dépôt. |
| `templates/project/.github/` | Même rôle, pour un futur projet. |
| `.clickup/` | Correspondance des tâches, listes, conflits. Convention Second Brain, pas une connexion ClickUp. |
| `.notion/` | Correspondance des pages et bases. Convention Second Brain, pas une connexion Notion. |
| Client MCP | Authentification et secrets. Jamais dans Git. |

## Actions externes

Lecture selon les droits du compte. Création, modification, commentaire, assignation, fermeture ou suppression : approbation explicite de l'action précise, sauf autorisation déjà donnée. Sans contrat de conflits, rester en lecture ou en proposition.

Le cœur métier ne dépend pas de MCP ni d'un éditeur. MCP et CLI appelleront les mêmes services, quand ils existeront.
