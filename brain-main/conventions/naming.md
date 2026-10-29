# Nomenclature

- Noms de fichiers stables, en anglais. Le contenu peut être en français.
- Pas de variantes numérotées (`ROADMAP-final-v2.md`), sauf le parcours `docs/00` à `docs/05`.

## Documents projet

Deux niveaux (ne pas les confondre) :

| Niveau | Fichiers | Quand |
| --- | --- | --- |
| **Socle minimal** | `brain/README.md`, `brain/STATE.md` | Toujours |
| **Profil Second Brain complet** | + `OVERVIEW`, `ARCHITECTURE`, `DECISIONS`, `TASKS`, + `brain/registry/ideas.md` | Template `project` et commandes `/cadrer`, `/note`, `/audit`, `/sync` |

Le manifeste `templates/project/template-manifest.yaml` installe le **profil complet** par défaut.  
Documents encore au premier besoin : `CHANGELOG`, `GLOSSARY`, `ROADMAP`, et les autres collections registry (`facts.md`, `hypotheses.md`, `issues.md`, …).

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
