# brain-main

Source commune du Second Brain. Les projets n'en reçoivent pas une copie intégrale (DEC-001, DEC-008). Ils reçoivent `templates/project/` et lient ce dossier via `.second-brain.yaml` → `brain_main_path`.

## Points d'entrée (IA)

| Emplacement | Rôle |
| --- | --- |
| `skills/COMMANDS.md` | Catalogue des commandes `/` |
| `skills/{cadrer,build,go,statut,note,sync,spec,faire,ui,done,audit,fin}/` | Skills de commandes |
| `skills/second-brain/` | Skill général + modules |
| `skills/clickup/` | Spécialiste ClickUp (projection, DEC-007) |
| `skills/{research,planning,implementation,review,memory}/` | Emplacements prévus (README only) |
| `conventions/` | Taxonomie, schéma registre, naming, memory-policy, carte |

## Dossiers

- `docs/` : vision et fonctionnement.
- `conventions/` : règles communes, taxonomie et schéma registre (DEC-006, DEC-009).
- `skills/` : commandes, Skill général, ClickUp, emplacements futurs.
- `core/` : emplacement de la logique métier. Pas encore de code.
- `tests/` : emplacement prévu des tests. Pas encore de code.
- `integrations/` : contrats communs GitHub, ClickUp, Notion et MCP.
- `adapters/` : points d'entrée par assistant, sans recopier les règles.
- `mcp-server/`, `cli/`, `scripts/` : interfaces prévues, non implémentées.
- `templates/project/` : scaffold + `template-manifest.yaml` (DEC-008, profil complet).
- `templates/web-starter/` : pack web **optionnel** (pas une application).

## Règles de conception

- Peu de Skills, des modules courts.
- Le transport (MCP, CLI, éditeur) ne contient pas la logique métier.
- Les fichiers canoniques priment sur SQLite.
- L'Inbox n'est pas une cible d'écriture automatique.
- Aucun secret dans Git.
- Mise à jour template : `propose_only`, jamais écraser `copy_once`.
