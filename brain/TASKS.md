# Tâches

Format (DEC-006 / DEC-007) : section `### TASK-NNN — titre` + bloc YAML fenced `entry` + prose courte.
Le local est la source de vérité ; ClickUp est une projection (skill `brain-main/skills/clickup/SKILL.md`).
Optimisé pour lecture IA : métadonnées complètes dans `entry` avant push ClickUp.

## Fait

### TASK-001 — Poser l'arborescence brain-main et brain

```entry
id: TASK-001
kind: task
status: resolved
title: Poser l'arborescence brain-main et brain
summary: Arborescence système commun et mémoire de dépôt en place.
created: 2026-10-29
updated: 2026-10-29
sources:
  - brain/STATE.md
relations: []
scope: system
list: Tasks
```

### TASK-002 — Distinguer mémoire dépôt et modèle projet

```entry
id: TASK-002
kind: task
status: resolved
title: Distinguer mémoire dépôt et modèle projet
summary: brain/ vs templates/project/ clarifiés (DEC-001).
created: 2026-10-29
updated: 2026-10-29
sources:
  - brain/DECISIONS.md
relations:
  - type: related_to
    target_id: DEC-001
scope: system
list: Tasks
```

### TASK-003 — Contrats d'intégration sans secrets

```entry
id: TASK-003
kind: task
status: resolved
title: Contrats d'intégration sans secrets
summary: Contrats GitHub / ClickUp / Notion documentés, sans connexion auto.
created: 2026-10-29
updated: 2026-10-29
sources:
  - brain-main/integrations/
relations:
  - type: related_to
    target_id: DEC-005
scope: system
list: Tasks
```

### TASK-004 — Modèle de données et cycle de vie (OPEN-001)

```entry
id: TASK-004
kind: task
status: resolved
title: Modèle de données et cycle de vie
summary: DEC-006 adoptée ; OPEN-001 résolu.
created: 2026-10-29
updated: 2026-10-29
sources:
  - brain/DECISIONS.md
relations:
  - type: related_to
    target_id: DEC-006
scope: system
list: Tasks
```

### TASK-005 — Réconciliation local / ClickUp / Notion (OPEN-002)

```entry
id: TASK-005
kind: task
status: resolved
title: Réconciliation local / ClickUp / Notion
summary: DEC-007 adoptée — local SoT ; ClickUp projection.
created: 2026-10-29
updated: 2026-10-29
sources:
  - conversation
  - brain/DECISIONS.md
relations:
  - type: related_to
    target_id: DEC-007
scope: system
list: Tasks
```

### TASK-006 — Définir déploiement et mise à jour du template (OPEN-003)

```entry
id: TASK-006
kind: task
status: resolved
title: Définir déploiement et mise à jour du template
summary: DEC-008 adoptée — copy_once / sync_shared / link_only ; manifeste template.
created: 2026-10-29
updated: 2026-10-29
sources:
  - brain/DECISIONS.md
  - brain-main/templates/project/template-manifest.yaml
relations:
  - type: related_to
    target_id: DEC-008
scope: system
list: Tasks
```

## Active

Aucune tâche active de cadrage. Suites possibles : mapping ClickUp + push, ou script d'init DEC-008.
