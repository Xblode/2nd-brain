# État du projet — Second Brain

> À lire avant un travail substantiel. Ce fichier décrit l'état réel, pas une cible.
> Dernière mise à jour : 2026-10-29. Commit de référence publié : `d79fb86` sur `main`.

## Résumé

- **Objectif :** une mémoire de projet locale, lisible et contrôlée, pour les agents et les humains.
- **Phase :** squelette documentaire. L'arborescence et les règles communes sont posées. Le modèle de données n'est pas choisi.
- **État :** les dossiers cibles existent. Aucun composant d'exécution n'est implémenté.

## Ce qui existe vraiment

- Arborescence `brain-main/` (système commun), `brain/` (mémoire de ce dépôt) et `brain-main/templates/project/` (modèle générique).
- Documents de vision dans `brain-main/docs/00-vision.md` à `05-sources-verite-integrations.md`.
- Conventions, Skill Second Brain, spécialiste ClickUp (`brain-main/skills/clickup/SKILL.md`) et contrats d'intégration, sous forme de textes. Le spécialiste ne connecte pas ClickUp.
- `AGENTS.md` comme base d'instructions commune. `CLAUDE.md` et `.github/copilot-instructions.md` ne font qu'adapter cette base.
- Décisions acceptées D-001 à D-005 dans `brain/DECISIONS.md`.

La copie locale de travail peut différer de `d79fb86`. Vérifier `git status` avant de considérer un fichier comme publié.

## Ce qui n'est pas implémenté

La présence de ces dossiers ne signifie pas qu'ils fonctionnent :

- `brain-main/core/` : registre, recherche, validation, permissions, index
- `brain-main/mcp-server/`
- `brain-main/cli/`
- `brain-main/scripts/`
- index SQLite sous `brain/runtime/`
- entrées de registre sous `brain/registry/`
- connexion réelle à GitHub, ClickUp ou Notion

`taxonomy.yaml` et `registry-schema.json` sont des emplacements réservés, pas un format adopté.

## Décisions tenues

- Brainstorming d'abord. Un agent de code ne part que sur un lot explicitement choisi.
- `brain-main/` n'est pas recopié intégralement dans les projets clients.
- Les fichiers canoniques sont la source de vérité. SQLite, s'il existe un jour, reste un index reconstructible.
- Une écriture de mémoire durable est proposée, puis approuvée par un humain. Le modèle ne s'approuve pas.
- `brain/inbox/` est une capture manuelle. Aucune IA n'y écrit.
- `.clickup/` et `.notion/` documentent des correspondances. Ils ne connectent pas de MCP.
- Aucun secret dans Git.

## Décisions ouvertes

Ne pas les trancher dans le code ou dans un schéma.

| Id | Sujet |
| --- | --- |
| O-001 | Format du registre, identifiants, relations, métadonnées, cycle de vie et statuts |
| O-002 | Réconciliation entre le local, ClickUp et Notion, et propriétaire de chaque champ |
| O-003 | Ce que le template copie, ce qui reste lié à `brain-main/`, et comment une mise à jour préserve les personnalisations |

## Prochaine action utile

Choisir le modèle de données canonique et le cycle de vie d'une information (O-001). Le registre, le MCP, la CLI et le déploiement du template en dépendent.

## Documents de référence

- `AGENTS.md`
- `brain/DECISIONS.md`
- `brain/TASKS.md`
- `brain/ARCHITECTURE.md`
- `README.md`
