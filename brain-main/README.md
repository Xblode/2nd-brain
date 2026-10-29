# brain-main

Source commune du Second Brain. Les projets n'en reçoivent pas une copie intégrale (DEC-001, DEC-008). Ils reçoivent `templates/project/` et lient ce dossier via `.second-brain.yaml` → `brain_main_path`.

## Dossiers

- `docs/` : vision et fonctionnement.
- `conventions/` : règles communes, taxonomie et schéma registre (DEC-006).
- `skills/second-brain/` : Skill et modules d'instructions.
- `skills/clickup/` : spécialiste ClickUp (projection depuis le local, DEC-007).
- `core/` : emplacement de la logique métier. Pas encore de code.
- `integrations/` : contrats communs GitHub, ClickUp, Notion et MCP.
- `adapters/` : points d'entrée par assistant, sans recopier les règles.
- `mcp-server/`, `cli/`, `scripts/` : interfaces prévues, non implémentées.
- `templates/project/` : scaffold + `template-manifest.yaml` (DEC-008).

## Règles de conception

- Peu de Skills, des modules courts.
- Le transport (MCP, CLI, éditeur) ne contient pas la logique métier.
- Les fichiers canoniques priment sur SQLite.
- L'Inbox n'est pas une cible d'écriture automatique.
- Aucun secret dans Git.
- Mise à jour template : `propose_only`, jamais écraser `copy_once`.
