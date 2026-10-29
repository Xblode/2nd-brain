---
name: clickup
description: >-
  Applique la convention ClickUp du Second Brain, lit les tâches locales
  (brain/TASKS.md, registre DEC-006/007) et prépare les écritures ClickUp en
  projection. À utiliser dès qu'une demande parle de ClickUp, tâche, liste,
  statut, assignation, commentaire, échéance, jalon, .clickup/, mapping ou
  duplication de template. Pas pour Notion ni pour trancher le registre.
---

# ClickUp — Second Brain

Spécialiste ClickUp. Ne remplace ni l'orchestrateur ni les agents de code.

**DEC-007 :** le local est la source de tout (y compris tâches). ClickUp est la vue humaine. Ce skill lit le local et aligne ClickUp — il ne prend pas ClickUp comme vérité des champs.

## Avant de travailler

1. `AGENTS.md`
2. `brain/STATE.md`
3. `brain-main/integrations/clickup.md`
4. **`brain/TASKS.md`** (et entrées `task` / `issue` liées) — source des payloads
5. `.clickup/README.md` et `.clickup/mapping.yaml` s'ils existent
6. Outils ClickUp réellement disponibles — sinon le dire, ne pas simuler
7. Espace : **Mon organisation** (vrac / perso) ou **Projets** (un dossier = un projet). Détail : `modules/convention.md`

Ne pas traiter une fonctionnalité documentée comme implémentée. Vérifier.

Charger un seul module selon le besoin : `modules/convention.md`, `modules/sync.md`, `modules/templates.md`.

## Sources

| Source | Rôle |
| --- | --- |
| Fichiers locaux (`brain/TASKS.md`, registre) | **Source de vérité** de tous les champs |
| ClickUp | Projection humaine ; drift à signaler, pas à imposer au local |
| GitHub | Code et historique |
| Conversation | Cadrage seulement |
| SQLite | Index dérivé, jamais seule copie |

## Convention listes (contrat)

Socle obligatoire : **Inbox** (`LIST.INBOX`, capture humaine — l'IA n'y écrit pas) + **docs** (`LIST.DOCS`).

Selon besoin : **Tasks** (`LIST.TASKS`), **Roadmap** (`LIST.ROADMAP`, jalons + critères seulement), **Bugs** (`LIST.BUGS` — un seul nom ; « Issues » = la même liste).

Pas de liste Decisions / Batches par défaut. Phases = champ ou vues, pas listes séparées. Détail : `modules/convention.md`.

## Qualité d'une tâche (local d'abord)

Une tâche destinée à ClickUp doit exister en local en bloc `entry` avec au minimum : `id`, `kind`, `status`, `title`, `created`, `updated`, `sources`, `relations`, plus selon besoin `assignees`, `due`, `priority`, `list`, `milestone`, `acceptance`, `clickup`.

Le skill **mappe** ces champs vers ClickUp ; il ne complète pas un vide local en inventant depuis ClickUp sans proposition de patch local.

## Workflow

1. Lire le local (`TASKS.md` / registre) et le mapping
2. Lire ClickUp seulement pour comparer / vérifier
3. Qualifier l'écart (créer / mettre à jour / drift)
4. Prévisualiser le diff ClickUp dérivé du local
5. Faire approuver — préparer ≠ autoriser
6. Exécuter via outils disponibles
7. Vérifier et reporter
8. Mettre à jour `clickup.task_id` / `list_id` / `last_pushed` si succès

## Sync et templates

Conception : `modules/sync.md` (DEC-007). Pas d'implémentation runtime automatique.

Duplication de template : `modules/templates.md`.

## Règles dures

- Ne pas prendre une tâche ClickUp comme canon sans entrée locale.
- Ne pas écraser le local pour coller à ClickUp sans proposition approuvée.
- Ne pas écrire dans une Inbox.
- Ne pas inventer d'ID, de résultat d'API, ni d'outil disponible.
- Ne pas changer la convention listes / clés `LIST.*` en passant : proposer, attendre.
- Ne pas approximer un statut ClickUp absent du `status_map` : signaler l'écart.

## Réponse

1. **État local vérifié** (entrées lues)
2. **Écart ClickUp** (si inspecté)
3. **Proposition** (local et/ou ClickUp) — non appliquée
4. **Risques / drift**
5. **Approbation demandée**

## Succès

Sans l'historique : savoir quelles `TASK-` / `ISSUE-` locales existent, lesquelles sont mappées, ce qui doit être poussé, et ce qui a divergé sur ClickUp.
