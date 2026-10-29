# 04 — Mémoire

## Sources

1. **Docs de cadrage obligatoires** dans `brain/` (SoT narrative) — voir `naming.md`.
2. **Registre** : éléments atomiques en collections Markdown, une entrée JSON par ligne (DEC-006, DEC-009). Schéma : `conventions/registry-schema.json` ; taxonomie : `conventions/taxonomy.yaml`.
3. Index SQLite local, reconstructible, jamais SoT (hors chemin critique V1).
4. Conversation ou journal : à vérifier avant d’en faire une vérité durable.

Les docs cadrage et les registres ne doivent pas se contredire en silence. Autorité : `PRINCIPLES.md`.

Cible post-V1 documentée (non migrée) : `state.json`, `memory.jsonl`, `projects.jsonl`, `work.jsonl`, `config.toml` derrière une interface I/O commune.

## Cycle de vie (DEC-006)

Création en `proposed` → validation humaine ou lot `/build` approuvé (`accepted` / `rejected` / `deferred`) → selon le kind : `settled`, `active`, `blocked`, `resolved`, `superseded`. Voir `conventions/memory-policy.md`.

Foyers : `brain/DECISIONS.md`, `brain/TASKS.md`, `brain/registry/`. Pas un fichier Markdown par idée. Brainstorming volumineux OK en `proposed` ; promotion via `/build`.

## Intégrations et template

- DEC-007 : local SoT ; ClickUp projection (souvent en fin de `/build`).
- DEC-008 : déploiement template ; voir `templates/README.md`.
- DEC-011 : pipeline V1 et docs cadrage obligatoires.
