# brain-main

Source commune du Second Brain. Les projets n'en reçoivent pas une copie intégrale. Ils reçoivent le modèle `templates/project/` et, plus tard, une mise à jour contrôlée des éléments réellement partagés.

## Dossiers

- `docs/` : vision et fonctionnement.
- `conventions/` : règles communes. Le format du registre n'est pas encore choisi.
- `skills/second-brain/` : Skill et modules d'instructions.
- `core/` : emplacement de la logique métier. Pas encore de code.
- `integrations/` : contrats communs GitHub, ClickUp, Notion et MCP.
- `adapters/` : points d'entrée par assistant, sans recopier les règles.
- `mcp-server/`, `cli/`, `scripts/` : interfaces prévues, non implémentées.
- `templates/project/` : fichiers à installer dans un autre dépôt.

## Règles de conception

- Peu de Skills, des modules courts.
- Le transport (MCP, CLI, éditeur) ne contient pas la logique métier.
- Les fichiers canoniques priment sur SQLite.
- L'Inbox n'est pas une cible d'écriture automatique.
- Aucun secret dans Git.
