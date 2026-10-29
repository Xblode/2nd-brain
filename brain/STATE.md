# État du projet — Second Brain

> À lire avant un travail substantiel. Ce fichier décrit l'état réel, pas une cible.
> Dernière mise à jour : 2026-10-29. Commit de référence publié : `d79fb86` sur `main`.

## Résumé

- **Objectif :** une mémoire de projet locale, lisible et contrôlée, pour les agents et les humains.
- **Phase :** squelette documentaire. Le modèle de données et le cycle de vie sont adoptés (DEC-006). Aucun composant d'exécution n'est implémenté.
- **État :** arborescence et contrats de registre posés. Parser, MCP, CLI, index SQLite absents.

## Ce qui existe vraiment

- Arborescence `brain-main/` (système commun), `brain/` (mémoire de ce dépôt) et `brain-main/templates/project/` (modèle générique).
- Documents de vision dans `brain-main/docs/00-vision.md` à `05-sources-verite-integrations.md`.
- Conventions, Skill Second Brain, spécialiste ClickUp (`brain-main/skills/clickup/SKILL.md`) et contrats d'intégration, sous forme de textes. Le spécialiste ne connecte pas ClickUp.
- `AGENTS.md` comme base d'instructions commune. `CLAUDE.md` et `.github/copilot-instructions.md` ne font qu'adapter cette base.
- Décisions acceptées DEC-001 à DEC-006 dans `brain/DECISIONS.md` (alias historiques `D-00x`).
- Contrats registre adoptés : `brain-main/conventions/taxonomy.yaml`, `registry-schema.json`.

La copie locale de travail peut différer de `d79fb86`. Vérifier `git status` avant de considérer un fichier comme publié.

## Ce qui n'est pas implémenté

La présence de ces dossiers ne signifie pas qu'ils fonctionnent :

- `brain-main/core/` : registre runtime, recherche, validation, permissions, index
- `brain-main/mcp-server/`
- `brain-main/cli/`
- `brain-main/scripts/`
- index SQLite sous `brain/runtime/`
- entrées de registre sous `brain/registry/` (foyer réservé ; pas encore de fichier collection)
- connexion réelle à GitHub, ClickUp ou Notion

## Décisions tenues

- Brainstorming d'abord. Un agent de code ne part que sur un lot explicitement choisi.
- `brain-main/` n'est pas recopié intégralement dans les projets clients.
- Les fichiers canoniques sont la source de vérité. SQLite, s'il existe un jour, reste un index reconstructible.
- Une écriture de mémoire durable est proposée, puis approuvée par un humain. Le modèle ne s'approuve pas.
- `brain/inbox/` est une capture manuelle. Aucune IA n'y écrit.
- `.clickup/` et `.notion/` documentent des correspondances. Ils ne connectent pas de MCP.
- Aucun secret dans Git.
- Registre Markdown en collections, IDs stables par kind, cycle de vie explicite (DEC-006 ; OPEN-001 résolu).

## Décisions ouvertes

Ne pas les trancher dans le code sans validation humaine.

| Id | Sujet |
| --- | --- |
| OPEN-002 | Réconciliation entre le local, ClickUp et Notion, et propriétaire de chaque champ |
| OPEN-003 | Ce que le template copie, ce qui reste lié à `brain-main/`, et comment une mise à jour préserve les personnalisations |

Alias historiques : `O-002`, `O-003`. OPEN-001 (alias `O-001`) est résolu par DEC-006.

## Prochaine action utile

Trancher OPEN-002 (sync / propriété des champs) ou créer de premières entrées pilotes au format DEC-006 si un besoin réel apparaît. Le MCP, la CLI et le déploiement du template restent bloqués tant que OPEN-002 / OPEN-003 ne sont pas tranchés selon le besoin.

## Documents de référence

- `AGENTS.md`
- `brain/DECISIONS.md`
- `brain/TASKS.md`
- `brain/ARCHITECTURE.md`
- `README.md`
