# 03 — Architecture des agents

Rôles logiques, pas forcément des processus séparés. Modes : Réflexion, Organisation, Exécution, Consolidation (DEC-011).

- **Orchestrateur** : intention, mode, mémoire, questions, lots, délégation ; reste en réflexion par défaut.
- **Capture / note** : classer vers registre ou docs cadrage (`/note`).
- **Organisation (`/build`)** : traiter le registre pending, demander validation, écrire local, enchaîner ClickUp.
- **Réalisation** : code d’un lot déjà choisi (`/faire`).
- **Revue** : écarts par rapport aux critères (`/done`, `/audit`).
- **Mémoire** : prépare une proposition, ne l’applique pas et ne l’approuve pas.
- **ClickUp** : projection selon `brain-main/skills/clickup/SKILL.md` — pas SoT, pas d’écriture sans accord.

## Délégation

- Un seul agent si la tâche est simple.
- Regrouper les changements liés avant un agent de code.
- Paralléliser seulement des sous-tâches indépendantes.
- Ne pas créer un agent par message de brainstorming.

Tous les rôles utilisent les mêmes conventions. Autorité : `brain/PRINCIPLES.md`. Particularités outil dans `adapters/` et `AGENTS.md` / `CLAUDE.md`.
