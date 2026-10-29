# Second Brain

Mémoire de projet locale, lisible et contrôlée — et lanceur via des commandes Cursor.  
Squelette documentaire V1 : un dossier ≠ runtime implémenté.

## Trois niveaux

| Emplacement | Fonction |
| --- | --- |
| `brain-main/` | Conventions, skills, docs système, templates |
| `brain/` | Mémoire de **ce** dépôt (docs cadrage + registres) |
| `brain-main/templates/project/` | Socle mémoire pour futurs projets (DEC-008) |
| `brain-main/templates/web-starter/` | Pack web optionnel — pas la mémoire par défaut |

## Pipeline V1

```text
Prompt → brainstorm → registre (proposed) → /build → local validé → ClickUp
```

Docs cadrage : `brain/OBJECTIVES.md`, `ROADMAP.md`, `PRINCIPLES.md`, `PROCESS.md`.  
État : `brain/STATE.md`. Décision : DEC-011.

## Principes (résumé)

- Constitution = `brain-main/conventions/` ; loi projet = `brain/*.md` ; procédures = skills.
- Local = SoT ; ClickUp = projection (DEC-007).
- Inbox manuelle ; pas de secret dans Git ; SQLite dérivé seulement.

## Commandes

Canon : `brain-main/skills/<nom>/SKILL.md`.  
Catalogue : [`brain-main/skills/COMMANDS.md`](brain-main/skills/COMMANDS.md).

| Commande | Rôle |
| --- | --- |
| `/note` | Capture → registre / docs (prévisualisation) |
| `/build` | **Organisation globale** du registre → local → propose `/clickup` ; sous-mode scaffold |
| `/cadrer` | Cadrage via `brain/` ; stop avant install |
| `/clickup` | Projection local → ClickUp après accord |
| `/faire` | Implémenter un lot déjà approuvé |
| `/go` `/statut` `/sync` `/audit` `/done` `/fin` | Pilotage / revue / clôture |

## Décisions clés

DEC-006/009 registre · DEC-007 local SoT · DEC-008 template · **DEC-011** V1 pipeline.

## Hors V1 (non implémenté)

Parser/runtime, MCP, CLI, SQLite SoT, sync auto, recherche vectorielle obligatoire.

## Lecture

1. `brain/STATE.md`
2. `brain/PROCESS.md`
3. `brain-main/skills/COMMANDS.md`
4. `AGENTS.md`
