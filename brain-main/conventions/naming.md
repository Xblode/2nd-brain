# Nomenclature

- Noms de fichiers stables, en anglais. Le contenu peut être en français.
- Pas de variantes numérotées (`ROADMAP-final-v2.md`), sauf le parcours `docs/00` à `docs/05`.
- Documents requis d'un projet : `brain/README.md`, `brain/STATE.md`.
- Documents à créer seulement si le besoin est réel : `OVERVIEW`, `ARCHITECTURE`, `DECISIONS`, `TASKS`, `CHANGELOG`, `GLOSSARY`, `ROADMAP`.

## Identifiants de registre (DEC-006)

- Forme : `{PREFIX}-{NNN}` (au moins 3 chiffres), numérotation monotone par kind.
- Jamais réassigner un id retiré.
- Préfixes :

| Kind | Préfixe |
| --- | --- |
| fact | `FACT-` |
| hypothesis | `HYP-` |
| idea | `IDEA-` |
| question | `OPEN-` |
| decision | `DEC-` |
| task | `TASK-` |
| issue | `ISSUE-` |
| reference | `REF-` |

- Alias historiques de ce dépôt : `D-00x` → `DEC-00x`, `O-00x` → `OPEN-00x` (lecture seule).
- Stockage en fichiers **collection** (plusieurs entrées par fichier), jamais un fichier par idée.
- Sérialisation (DEC-009) : une entrée = un objet JSON par ligne physique dans un bloc `jsonl`. Voir `taxonomy.yaml` et `registry-schema.json`.
