# Memory

- **Role:** rechercher, réconcilier et préparer des propositions de mises à jour de la mémoire canonique.
- **Scope:** lecture des collections JSONL, détection de drift/doublons, propositions d'entrées.
- **Boundaries:** propose-only jusqu'à approbation humaine (DEC-003) ; pas d'écriture Inbox ; SQLite n'est pas SoT.
- **Dependencies:** DEC-006 / DEC-009, `memory-policy.md`, modules `registry-write.md` / `search-reconcile.md`.
- **Status:** planned — not implemented.
