# Glossaire

Vocabulaire du cycle idée → décision → tâche → lot → fait.

## Kinds (registre)

| Kind | Préfixe | Sens |
| --- | --- | --- |
| idea | `IDEA-` | Piste ou suggestion ; pas encore engagée |
| hypothesis | `HYP-` | Affirmation à vérifier |
| question | `OPEN-` | Inconnue bloquante ou ouverte |
| decision | `DEC-` | Choix tranché (après acceptation → souvent `settled`) |
| task | `TASK-` | Travail vérifiable |
| issue | `ISSUE-` | Problème / bug suivi |
| fact | `FACT-` | Connaissance durable acceptée |
| reference | `REF-` | Pointeur vers une source externe |

Contrats : `brain-main/conventions/taxonomy.yaml`.

## Statuts courants

| Statut | Usage typique |
| --- | --- |
| `proposed` | Entrée brainstorm / proposition ; pas encore validée |
| `accepted` | Humain a accepté de conserver / engager |
| `rejected` | Écartée explicitement |
| `deferred` | Reportée |
| `active` | En cours (tâche, issue, question) |
| `blocked` | Bloquée |
| `resolved` | Clôturée (tâche, issue, question) |
| `settled` | Décision figée |
| `superseded` | Remplacée par une entrée plus récente (`supersedes`) |

Seul un humain fait passer `proposed` → `accepted` | `rejected` | `deferred` (sauf confirmation de lot `/build` qui joue ce rôle explicitement).

## Concepts pipeline

| Terme | Définition |
| --- | --- |
| **Registre** | Collections d’entrées structurées (JSONL dans Markdown pour l’instant) |
| **Doc de cadrage** | `.md` obligatoire dans `brain/` (objectifs, roadmap, process…) — SoT narrative |
| **Lot** | Ensemble cohérent de changements : objectif, périmètre, critères, risques |
| **`/build`** | Passe globale : analyse et organisation du registre → local → ClickUp |
| **Projection** | Copie / vue dans ClickUp ; le local reste SoT |
| **Inbox** | Capture manuelle uniquement ; hors registre automatisé |

## Promotion

Une `idea` / `hypothesis` **acceptée** reste du même kind. Pour en faire une tâche ou une décision, créer une **nouvelle** entrée liée (`derived_from`), ne pas changer le kind in-place.
