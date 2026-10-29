# 05 — Sources de vérité et intégrations

## Ordre

1. Instruction humaine explicite et décision récente.
2. Docs de cadrage obligatoires du projet (`brain/OBJECTIVES`, `ROADMAP`, `PRINCIPLES`, `PROCESS`, …).
3. Registre atomique (entrées JSONL, DEC-009) dans `DECISIONS` / `TASKS` / `registry/`.
4. Index SQLite, pour retrouver une source, pas pour la remplacer.
5. Conversation ou journal, à vérifier avant d’en faire une vérité durable.
6. GitHub, ClickUp, Notion : surfaces spécialisées — **jamais SoT silencieuse** (DEC-007).

ClickUp est une projection du local (souvent après `/build`). Notion est un miroir optionnel. GitHub porte le code.

En cas de contradiction local ↔ distant : montrer les deux ; proposer un patch ; local gagne jusqu’à décision contraire explicite.

## Qui configure quoi

| Emplacement | Rôle |
| --- | --- |
| `brain-main/conventions/` | Constitution : taxonomy, schéma, memory-policy, naming |
| `brain/*.md` obligatoires | Loi du projet |
| `brain-main/skills/` | Procédures (`/note`, `/build`, `/clickup`) |
| `brain-main/integrations/` | Contrat commun integrations |
| `.clickup/` | Mapping `LIST.*` ; `source_of_truth: local` |
| Client MCP | Auth et secrets — jamais dans Git ; hors V1 |

## Actions externes

Lecture selon les droits du compte. Création / modification ClickUp : approbation explicite. Le skill ClickUp dérive les écritures depuis le local (`brain/TASKS.md` et registres concernés).
