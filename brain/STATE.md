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
current_focus: "M1 clos — écart ClickUp push documenté ; suite = TASK-012 ou jalon 2"
next_action: "Quand prêt : créer LIST.TASKS + .clickup/mapping.yaml puis /clickup (TASK-012) ; sinon cadrer jalon 2."
active_tasks:
  - TASK-012
resolved_m1:
  - TASK-007
  - TASK-008
  - TASK-009
  - TASK-010
blockers: []
known_gaps:
  - "ClickUp push : mapping projet + LIST.TASKS + status_map (TASK-012)"
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
  commands: brain-main/skills/COMMANDS.md
```

## Distinctions

| Existe réellement | Seulement prévu / reporté |
| --- | --- |
| Docs, conventions, skills, DEC-001–010 | Runtime `core/`, parser, SQLite, MCP SB, CLI |
| Mémoire `brain/` + template structurel aligné | — |
| Preuve Chat → local (`/note`) | — |
| Preview `/clickup` MCP (lot documenté) | **Push** ClickUp (TASK-012) |
| Pack `web-starter` (optionnel) | Application web |

## Clôture M1

- Preuves : TASK-007…010 resolved ; détail dans `OVERVIEW.md`.
- Écart accepté : push ClickUp plus tard → **TASK-012**.
- Pas de jalon 2 ouvert automatiquement.
