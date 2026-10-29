# 04 — Mémoire

## Sources

1. Fichiers canoniques, lisibles et versionnés.
2. Registre : éléments atomiques en collections Markdown, une entrée JSON par ligne (DEC-006, DEC-009). Schéma : `conventions/registry-schema.json` ; taxonomie : `conventions/taxonomy.yaml`.
3. Documents de synthèse : état, décisions, tâches, architecture.
4. Index SQLite local, reconstructible, jamais seule copie d'une décision.
5. Journaux techniques temporaires, distincts de la mémoire durable.

Une information importante doit pouvoir se relire dans un fichier. Le registre et les synthèses ne doivent pas se contredire en silence : une seule source est désignée comme référence.

Les préférences récurrentes peuvent être suggérées. Une préférence confirmée et une inférence restent distinctes. Changer une règle commune demande une décision explicite dans `brain-main/`.

## Cycle de vie (DEC-006)

Création en `proposed` → validation humaine (`accepted` / `rejected` / `deferred`) → selon le kind : `settled`, `active`, `blocked`, `resolved`, `superseded`. Voir `conventions/memory-policy.md`.

Foyers d'écriture : `brain/DECISIONS.md` (décisions, questions), `brain/TASKS.md` (tâches), `brain/registry/` (autres kinds, au besoin). Pas un fichier par idée.

## Intégrations et template

- DEC-007 : local SoT ; ClickUp projection.
- DEC-008 : déploiement template (`copy_once` / `sync_shared` / `link_only`) ; voir `templates/README.md`.
