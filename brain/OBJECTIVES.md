# Objectifs — Second Brain

**Finalité :** mémoire de projet locale, lisible et contrôlée, pour passer du brainstorming à l’organisation puis à l’exécution sans perdre les idées ni les décisions — et projeter le suivi validé vers ClickUp.

**Usagers :** humains et agents IA (Cursor, Claude, etc.) qui partagent les mêmes contrats.

## Périmètre V1

- Docs de cadrage obligatoires dans `brain/` (fils conducteurs, SoT narrative).
- Registres d’entrées structurées (idées, tâches, décisions, etc.) en collections versionnées.
- Pipeline : prompt → brainstorming → registre (`proposed`) → `/build` → local validé → ClickUp.
- Skills textuels et dogfooding sur ce dépôt.

## Hors périmètre V1

- Serveur MCP dédié, CLI runtime, parser/index SQLite comme source de vérité.
- Recherche vectorielle obligatoire.
- Sync automatique silencieuse vers ClickUp / Notion.
- Pack `web-starter` comme mémoire par défaut ou cœur du produit.

## Critères de succès V1

1. Un agent retrouve objectifs, roadmap, process et état sans inventer.
2. Le brainstorming peut accumuler des entrées `proposed` sans les transformer automatiquement en tâches.
3. `/build` analyse, trie, demande validation sur les choix structurants, organise en local, puis propose la projection ClickUp.
4. Aucune idée n’est jetée en silence ; Inbox jamais écrite par une IA.
