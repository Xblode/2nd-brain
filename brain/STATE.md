# État du projet — Second Brain

Point d'entrée opérationnel. Lire avant tout travail substantiel.
Ce fichier décrit l'état réel, pas une cible.

```yaml
updated: "2026-10-29"
project: Second Brain
phase: m1_done
runtime_status: not_implemented
milestone: M1
milestone_status: closed
current_focus: "M1 clos — écart ClickUp push résolu (TASK-012) ; jalon 2 non ouvert"
next_action: "Quand prêt : cadrer jalon 2, ou traiter TASK-011 (proposed) / DEC-011–012."
active_tasks: []
resolved_m1:
  - TASK-007
  - TASK-008
  - TASK-009
  - TASK-010
resolved_m1_1:
  - TASK-012
blockers: []
known_gaps:
  - "Statuts ClickUp espace Projets = phases web ; status_map minimal Open/Closed (pas de en cours / bloquée)"
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
  proposed:
    - DEC-011
    - DEC-012
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
  clickup_mapping: .clickup/mapping.yaml
  commands: brain-main/skills/COMMANDS.md
```

## Distinctions

| Existe réellement | Seulement prévu / reporté |
| --- | --- |
| Docs, conventions, skills, DEC-001–010 | Runtime `core/`, parser, SQLite, MCP SB, CLI |
| Mémoire `brain/` + template structurel aligné | — |
| Preuve Chat → local (`/note`) | — |
| Preview + **push** `/clickup` (TASK-001…012 → LIST.TASKS) | — |
| Pack `web-starter` (optionnel) | Application web |
| `.clickup/mapping.yaml` projet (IDs réels) | Workflow statuts opérationnels dédiés sur l’espace Projets |

## Clôture M1 / M1.1

- Preuves : TASK-007…010 resolved ; détail dans `OVERVIEW.md`.
- TASK-012 resolved 2026-10-29 : mapping + LIST.TASKS + push lot.
- Pas de jalon 2 ouvert automatiquement.
