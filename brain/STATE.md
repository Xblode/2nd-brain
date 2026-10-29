# État du projet — Second Brain

Point d’entrée opérationnel. Lire avant tout travail substantiel.
Ce fichier décrit l’état réel, pas une cible.

```yaml
updated: "2026-10-29"
project: Second Brain
phase: v1_pipeline
runtime_status: not_implemented
milestone: V1
current_focus: "V1 — Prompt → brainstorm → registre → /build → local → ClickUp"
next_action: "Valider docs cadrage obligatoires et tester /note puis /build (organisation)."
active_tasks:
  - TASK-011
  - TASK-012
  - TASK-013
  - TASK-014
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
    - DEC-011
  framing_closed:
    - OPEN-001
    - OPEN-002
    - OPEN-003
canonical_sources:
  agents: AGENTS.md
  state: brain/STATE.md
  objectives: brain/OBJECTIVES.md
  roadmap: brain/ROADMAP.md
  principles: brain/PRINCIPLES.md
  process: brain/PROCESS.md
  architecture: brain/ARCHITECTURE.md
  glossary: brain/GLOSSARY.md
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
| Docs cadrage obligatoires V1, conventions, skills textuels, DEC-001–011 | Runtime `core/`, parser, SQLite SoT, MCP, CLI |
| Mémoire `brain/` (STATE, OBJECTIVES, ROADMAP, PRINCIPLES, PROCESS, ARCHITECTURE, GLOSSARY, registres) | Preuve bout-en-bout `/build` organisation + ClickUp |
| Skills `/` ancrés sur `brain/` + anti-perte | Sync ClickUp automatisée |
| Template `templates/project/brain/` à aligner V1 | `/build` scaffold 100 % automatisé |
| Contrats ClickUp + skill `/clickup` (prévisualisation) | Lot ClickUp poussé et vérifié en prod |
| Pack `web-starter` (optionnel, hors V1) | Application web |

## Jalon V1 — rappel

**Flux :** prompt → brainstorm → registre `proposed` → `/build` → validation → local → `/clickup`.  
**Détail :** `PROCESS.md`, `ROADMAP.md`. **Décision :** DEC-011. **Tâches :** TASK-011 … TASK-014.
