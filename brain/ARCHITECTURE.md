# Architecture

Responsabilités et relations. Décision : DEC-011.

## Zones

| Zone | Responsabilité |
| --- | --- |
| `brain/` | Mémoire de **ce** dépôt : docs cadrage obligatoires + registres + état |
| `brain-main/` | Système partagé : conventions, docs doctrine, skills, contrats, templates |
| `brain-main/templates/project/` | Modèle générique pour futurs projets |
| Fichiers canoniques | SoT versionnée (docs Markdown + entrées registre JSONL) |
| ClickUp | Projection humaine après organisation locale (DEC-007) |
| SQLite / MCP / CLI | Emplacements futurs — **hors V1**, jamais SoT |

```
2nd-brain/
├── brain-main/     système commun (conventions, skills, docs, templates)
└── brain/          mémoire de ce dépôt
    ├── *.md        docs cadrage obligatoires (SoT narrative)
    ├── DECISIONS.md, TASKS.md, registry/   registres (SoT data)
    └── inbox/      capture manuelle seulement
```

`brain/` ≠ `templates/project/brain/`.

## Docs cadrage vs registres

- **Docs cadrage** (`OBJECTIVES`, `ROADMAP`, `PRINCIPLES`, `PROCESS`, `GLOSSARY`, `ARCHITECTURE`, `STATE`, `README`) : fils conducteurs, documentation, SoT narrative.
- **Registres** : entrées atomiques (idées, tâches, décisions…) — volume OK en brainstorming (`proposed`).
- Cible post-V1 documentée : `state.json` + `*.jsonl` purs + `config.toml` ; **non migrée** en V1.

## Quatre modes orchestrateur

1. **Réflexion** — questions, alternatives ; pas d’agent de code.
2. **Organisation** — `/build` : tri du registre, validation, écriture locale.
3. **Exécution** — lot approuvé → agent de code / `/faire`.
4. **Consolidation** — maj mémoire et décisions confirmées seulement.

## Pipeline V1

```text
Prompt → brainstorm → registre (proposed) → /build → validation
      → local (tâches, docs, décisions) → /clickup
```

## Hors chemin critique V1

`brain-main/core/`, `mcp-server/`, `cli/`, index SQLite, recherche vectorielle, sync auto.
