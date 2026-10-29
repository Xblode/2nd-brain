# Roadmap

## Jalon V1 — Pipeline (en cours)

**Objectif :** prouver le flux  
`Prompt → brainstorming → registre → /build → organisation locale → ClickUp`.

**Réussi quand :**

1. Les docs de cadrage obligatoires dans `brain/` sont en place et cohérents avec le template projet.
2. `/note` (et agents) classent vers registres / docs sans suppression silencieuse.
3. `/build` (mode organisation) traite un lot d’entrées `proposed` : analyse, tri, validation sélective, écriture locale.
4. Après le local validé, projection ClickUp via `/clickup` (ClickUp ≠ SoT).

**Pas dans V1 :** runtime MCP/CLI, SQLite SoT, recherche sémantique obligatoire, multi-agents spécialisés par défaut.

## Post-V1 (indicatif)

- Fichiers data purs (`state.json`, `*.jsonl`, `config.toml`) derrière une interface I/O commune.
- Index SQLite reconstructible (jamais SoT).
- MCP / CLI si un besoin réel le justifie.
- Raffinement multi-projets et skills spécialisés à la demande.

## Historique

- **DEC-010** (jalon Chat → local → ClickUp) : recentré par **DEC-011** — ClickUp reste l’étape finale après `/build`, plus le seul critère de succès isolé.
