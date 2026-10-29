# Décisions

Format d'entrée (D-006) : section `### {id} — {title}` + bloc YAML fenced `entry` + prose.

**Alias historiques :** `D-00x` → `DEC-00x`, `O-00x` → `OPEN-00x`. Les anciens préfixes restent des alias de lecture uniquement ; les nouveaux IDs sont canoniques.

## Settled

### DEC-001 — Séparer système commun et mémoire projet

```entry
id: DEC-001
kind: decision
status: settled
title: Séparer système commun et mémoire projet
summary: brain-main/ porte les règles communes ; brain/ porte la mémoire de ce dépôt.
created: 2026-10-29
updated: 2026-10-29
sources:
  - conversation
  - brain/ARCHITECTURE.md
relations: []
scope: system
```

`brain-main/` porte les règles communes. `brain/` porte la mémoire de ce dépôt. Un autre projet reçoit `templates/project/`, pas une copie de tout `brain-main/`.

Alias historique : `D-001`.

### DEC-002 — Fichiers canoniques

```entry
id: DEC-002
kind: decision
status: settled
title: Fichiers canoniques
summary: Les fichiers lisibles sont la source de vérité ; SQLite est un index reconstructible.
created: 2026-10-29
updated: 2026-10-29
sources:
  - conversation
relations: []
scope: system
```

Les fichiers lisibles sont la source de vérité. SQLite sera un index reconstructible.

Alias historique : `D-002`.

### DEC-003 — Validation humaine

```entry
id: DEC-003
kind: decision
status: settled
title: Validation humaine
summary: Une écriture durable proposée par un modèle attend une approbation humaine distincte.
created: 2026-10-29
updated: 2026-10-29
sources:
  - conversation
relations: []
scope: system
```

Une écriture durable proposée par un modèle attend une approbation humaine distincte. Le modèle ne s'approuve pas.

Alias historique : `D-003`.

### DEC-004 — Inbox manuelle

```entry
id: DEC-004
kind: decision
status: settled
title: Inbox manuelle
summary: Aucune automatisation n'écrit dans l'Inbox.
created: 2026-10-29
updated: 2026-10-29
sources:
  - conversation
relations: []
scope: system
```

Aucune automatisation n'écrit dans l'Inbox.

Alias historique : `D-004`.

### DEC-005 — Intégrations

```entry
id: DEC-005
kind: decision
status: settled
title: Intégrations
summary: Contrats communs dans brain-main/integrations/ ; .clickup/ et .notion/ sans secret ni MCP.
created: 2026-10-29
updated: 2026-10-29
sources:
  - conversation
  - brain-main/integrations/
relations: []
scope: system
```

Les contrats communs sont dans `brain-main/integrations/`. `.github/` est reconnu par GitHub. `.clickup/` et `.notion/` sont des conventions de correspondance, sans secret et sans connexion MCP.

Alias historique : `D-005`.

### DEC-006 — Modèle de données canonique et cycle de vie

```entry
id: DEC-006
kind: decision
status: settled
title: Modèle de données canonique et cycle de vie
summary: Registre Markdown en collections, IDs stables par kind, cycle de vie explicite ; clôture OPEN-001.
created: 2026-10-29
updated: 2026-10-29
sources:
  - conversation
  - plan O-001 (Build approuvé)
  - brain-main/conventions/taxonomy.yaml
  - brain-main/conventions/registry-schema.json
relations:
  - type: derived_from
    target_id: OPEN-001
scope: system
```

**Format canonique :** Markdown structuré, versionné dans Git. Pas de JSON atomique comme source de vérité. SQLite reste un index dérivé (DEC-002).

**Stockage :** fichiers **collection** (plusieurs entrées par fichier), pas un fichier par idée.

- décisions / questions ouvertes → `brain/DECISIONS.md`
- tâches → `brain/TASKS.md`
- état / architecture → synthèses non-atomiques (`brain/STATE.md`, `brain/ARCHITECTURE.md`)
- kinds sans foyer actuel (`fact`, `hypothesis`, `idea`, `issue`, `reference`) → un fichier collection sous `brain/registry/` (ex. `facts.md`), créé seulement au premier besoin réel

**Schéma d'entrée (requis) :** `id`, `kind`, `status`, `title`, `summary` (optionnel si le corps suffit), `created` / `updated`, `sources`, `relations` (`{ type, target_id }`). Optionnels : `scope`, `certainty`, `superseded_by`, clés de mapping externes (réservées pour OPEN-002).

**Forme Markdown :** `### {id} — {title}` + bloc YAML fenced `entry` + prose.

**Préfixes d'ID :** `FACT-`, `HYP-`, `IDEA-`, `OPEN-`, `DEC-`, `TASK-`, `ISSUE-`, `REF-`. Numérotation monotone par kind ; jamais réassigner un id retiré.

**Kinds adoptés :** `fact`, `hypothesis`, `idea`, `question`, `decision`, `task`, `issue`, `reference`. Hors registre : plans détaillés, notes de session, Inbox. `requirement` / `plan` / `insight` / `note` ne sont pas adoptés.

**Relations :** `supports`, `contradicts`, `supersedes`, `derived_from`, `implements`, `related_to`, `blocks`, `duplicate_of`.

**Cycle de vie :** `proposed` → `accepted` | `rejected` | `deferred` (validation humaine, DEC-003) ; puis selon le kind `active` / `blocked` / `resolved` / `settled` / `superseded`. Contrats : `taxonomy.yaml` et `registry-schema.json` (status `adopted`).

Alias historique : `D-006`. Clôture `OPEN-001` (alias `O-001`).

## Resolved

### OPEN-001 — Modèle de données

```entry
id: OPEN-001
kind: question
status: resolved
title: Modèle de données
summary: Tranché par DEC-006 — Markdown collection, IDs stables, cycle de vie explicite.
created: 2026-10-29
updated: 2026-10-29
sources:
  - conversation
  - brain/STATE.md
relations:
  - type: related_to
    target_id: DEC-006
scope: system
```

Markdown structuré ou JSON atomique, identifiants, relations, métadonnées, et cycle de vie d'une information. Tranché par DEC-006.

Alias historique : `O-001`.

## Active

### OPEN-002 — Synchronisation

```entry
id: OPEN-002
kind: question
status: active
title: Synchronisation
summary: Réconciliation local / ClickUp / Notion et propriété des champs.
created: 2026-10-29
updated: 2026-10-29
sources:
  - conversation
  - brain/STATE.md
relations: []
scope: system
```

Comment un changement local, ClickUp ou Notion est proposé, validé et réconcilié. Qui est propriétaire de quel champ.

Alias historique : `O-002`.

### OPEN-003 — Déploiement du template

```entry
id: OPEN-003
kind: question
status: active
title: Déploiement du template
summary: Périmètre de copie template vs lien brain-main/, et préservation des personnalisations.
created: 2026-10-29
updated: 2026-10-29
sources:
  - conversation
  - brain/STATE.md
relations: []
scope: system
```

Ce qui est copié dans un projet, ce qui reste lié à `brain-main/`, et comment une mise à jour préserve les personnalisations.

Alias historique : `O-003`.
