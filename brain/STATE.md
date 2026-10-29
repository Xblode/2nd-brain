# État du projet — Second Brain

Point d'entrée opérationnel. Lire avant tout travail substantiel.
Ce fichier décrit l'état réel, pas une cible.

```yaml
updated: "2026-10-29"
project: Second Brain
phase: milestone_1
runtime_status: not_implemented
milestone: M1
current_focus: "Jalon 1 — Chat → brain/ → ClickUp ; valider archi ; skills anti-perte"
next_action: "Tester le flux M1 : message → /note → maj brain/ → /clickup (prévisualisation)."
active_tasks:
  - TASK-007
  - TASK-008
  - TASK-009
  - TASK-010
blockers: []
open_questions: []
decisions:
  adopted:
    - DEC-001
    - DEC-002
    - DEC-003
    - DEC-004
    - DEC-005
    - DEC-006
    - DEC-007
    - DEC-008
    - DEC-009
    - DEC-010
  framing_closed:
    - OPEN-001
    - OPEN-002
    - OPEN-003
canonical_sources:
  agents: AGENTS.md
  overview: brain/OVERVIEW.md
  architecture: brain/ARCHITECTURE.md
  decisions: brain/DECISIONS.md
  tasks: brain/TASKS.md
  ideas: brain/registry/ideas.md
  taxonomy: brain-main/conventions/taxonomy.yaml
  schema: brain-main/conventions/registry-schema.json
  info_map: brain-main/conventions/INFORMATION_MAP.yaml
  memory_policy: brain-main/conventions/memory-policy.md
  clickup_skill: brain-main/skills/clickup/SKILL.md
  commands: brain-main/skills/COMMANDS.md
```

## Distinctions

| Existe réellement | Seulement prévu / pas encore prouvé |
| --- | --- |
| Docs, conventions, skills textuels, DEC-001–010 | Runtime `core/`, parser, SQLite, MCP, CLI |
| Mémoire `brain/` (STATE, OVERVIEW, ARCHITECTURE, DECISIONS, TASKS, inbox, registry/ideas, references, runtime) | Test manuel bout-en-bout M1 (preuve) |
| Skills `/` ancrés sur `brain/` + anti-perte (`/note`, memory-policy) | Sync ClickUp automatisée |
| Template `templates/project/brain/` aligné sur l’exemple | `/build` 100 % automatisé |
| Contrats ClickUp + skill `/clickup` (prévisualisation) | Lot ClickUp réellement poussé et vérifié |
| Pack `web-starter` (optionnel, hors M1) | Application web |

## Jalon 1 — rappel

**Flux :** comprendre → ranger en local (`brain/`) → accord → projeter ClickUp.  
**Détail / critères :** `OVERVIEW.md`. **Décision :** DEC-010. **Tâches :** TASK-007 … TASK-010.
