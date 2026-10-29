# Vision de ce projet

**Finalité :** mémoire de projet locale, lisible et contrôlée, pour passer du brainstorming à l'exécution sans perdre les idées ni les décisions — puis projeter le suivi vers ClickUp.

**Usagers :** humains et agents IA (Cursor, etc.) qui partagent les mêmes contrats.

**Périmètre actuel :** squelette documentaire + skills textuels ; dogfooding sur `brain/` ; jalon 1 **clos** ; écart ClickUp push résolu (TASK-012).

**Principes non négociables :** fichiers canoniques = source de vérité ; écriture durable = proposition puis approbation humaine ; Inbox manuelle ; mise à jour sans suppression silencieuse ; aucun secret dans Git ; SQLite dérivé seulement.

**Hors périmètre actuel :** moteur exécutable (parser, index, MCP SB, CLI), sync automatique, pack web comme cœur du produit.

## Roadmap — Jalon 1 (clos — 2026-10-29)

**Objectif :** communiquer et conventionner le flux **Chatbot → infos en local (`brain/`) → ClickUp**.

| Critère | Statut |
| --- | --- |
| 1. Architecture `brain/` validée / testée (modèle) | Fait |
| 2. Skills classent / rangent / patchent sans effacer | Fait |
| 3. Pas de perte d’idée entre chat et local | Fait (preuve `/note`) |
| 4. `/clickup` projette le lot approuvé | **Fait** — preview + push TASK-001…012 via TASK-012 (2026-10-29) |

**Écart ClickUp (clos via TASK-012) :** `.clickup/mapping.yaml` + `LIST.TASKS` (`1201110000007783`) sous Projets/2nd Brain ; lot local projeté. Résidu : `status_map` minimal Open/Closed (statuts d’espace = phases web).

**Pas dans le jalon 1 :** automatisation runtime, Notion comme SoT, multi-agents complexes, pack web obligatoire.
