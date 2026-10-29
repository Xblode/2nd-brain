# 03 — Architecture des agents

Rôles logiques, pas forcément des processus séparés.

- **Orchestrateur** : intention, mode, mémoire, questions, lots, délégation.
- **Recherche** : lecture seule, sources citées.
- **Cadrage** : exigences, décisions ouvertes, risques.
- **Réalisation** : code d'un lot déjà choisi.
- **Revue** : écarts par rapport aux critères.
- **Mémoire** : prépare une proposition, ne l'applique pas et ne l'approuve pas.
- **ClickUp** : lit ou propose des actions ClickUp selon `brain-main/skills/clickup/SKILL.md`. Il ne décide pas de la source de vérité et n'écrit pas sans accord explicite.

## Délégation

- Un seul agent si la tâche est simple.
- Regrouper les changements liés avant un agent de code.
- Paralléliser seulement des sous-tâches indépendantes.
- Expliquer le bénéfice d'une délégation.

Tous les rôles utilisent les mêmes conventions. Les particularités Cursor ou Claude Code restent dans `adapters/` et les fichiers d'entrée (`AGENTS.md`, `CLAUDE.md`).
