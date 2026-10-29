# Nomenclature

- Noms de fichiers stables, en anglais. Le contenu peut être en français.
- Pas de variantes numérotées (`ROADMAP-final-v2.md`), sauf le parcours `docs/00` à `docs/05`.

## Documents requis d’un projet (`brain/`) — DEC-011

| Fichier | Rôle |
| --- | --- |
| `README.md` | Index de navigation |
| `STATE.md` | État opérationnel |
| `OBJECTIVES.md` | Vision, usagers, périmètre |
| `ROADMAP.md` | Jalons et critères |
| `PRINCIPLES.md` | Non négociables + autorité |
| `PROCESS.md` | Pipeline idée → `/build` → ClickUp |
| `ARCHITECTURE.md` | Zones et modes |
| `GLOSSARY.md` | Vocabulaire et cycle de vie |

`OVERVIEW.md` n’est plus SoT (éventuel pointeur de compatibilité seulement).

## Registres (données)

Toujours présents une fois le projet actif : `DECISIONS.md`, `TASKS.md`.  
Autres collections sous `registry/` au premier besoin (`ideas.md`, etc.).

## Identifiants de registre (DEC-006)

- Forme : `{PREFIX}-{NNN}` (au moins 3 chiffres), numérotation monotone par kind.
- Jamais réassigner un id retiré.
- Préfixes : `FACT-`, `HYP-`, `IDEA-`, `OPEN-`, `DEC-`, `TASK-`, `ISSUE-`, `REF-` (voir `taxonomy.yaml`).
- Alias historiques : `D-00x` → `DEC-00x`, `O-00x` → `OPEN-00x` (lecture seule).
- Stockage en fichiers **collection** ; sérialisation DEC-009 : un objet JSON par ligne physique dans un bloc `jsonl`.
