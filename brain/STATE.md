# État du projet — Second Brain

> À lire avant un travail substantiel. Ce fichier décrit l'état réel, pas une cible.
> Dernière mise à jour : 2026-10-29. Commit de référence à vérifier via `git log` / `git status`.

## Résumé

- **Objectif :** une mémoire de projet locale, lisible et contrôlée, pour les agents et les humains.
- **Phase :** squelette documentaire. DEC-006 (registre), DEC-007 (sync/propriété), DEC-008 (template) adoptées. Aucun composant d'exécution n'est implémenté.
- **État :** décisions ouvertes de cadrage fermées. Parser, MCP, CLI, index SQLite, script de déploiement absents.

## Ce qui existe vraiment

- Arborescence `brain-main/`, `brain/`, `brain-main/templates/project/`.
- Documents de vision `brain-main/docs/00`–`05`.
- Conventions, skills, contrats d'intégration (textes).
- `AGENTS.md` comme base d'instructions commune.
- Décisions DEC-001 à DEC-008 dans `brain/DECISIONS.md`.
- Contrats registre + champs ClickUp ; `template-manifest.yaml` + `.second-brain.yaml` (DEC-008).
- Tâches au format entry dans `brain/TASKS.md`.

## Ce qui n'est pas implémenté

- Runtime `core/`, MCP, CLI, scripts (y compris install/update template)
- index SQLite
- fichiers collection hors DECISIONS/TASKS sous `brain/registry/`
- connexion / push automatique ClickUp ou Notion

## Décisions tenues

- Brainstorming d'abord ; agent de code seulement sur lot choisi.
- Fichiers canoniques = SoT ; SQLite = index dérivé.
- Écriture durable : proposition puis approbation humaine.
- Inbox manuelle ; aucune IA n'y écrit.
- Aucun secret dans Git.
- DEC-006 : registre Markdown collections + cycle de vie.
- DEC-007 : local SoT ; ClickUp projection via skill.
- DEC-008 : template `copy_once` / `sync_shared` / `link_only` ; `brain-main` par référence.

## Décisions ouvertes

Aucune question `OPEN-` active dans `brain/DECISIONS.md` pour le cadrage initial.

## Prochaine action utile

Convention ClickUp harmonisée (socle Inbox+docs, clés `LIST.*`, `LIST.BUGS`, `status_map`, contrat parent Template) — docs seulement, pas de runtime. Suites possibles : renseigner `.clickup/mapping.yaml` du dépôt + `status_map` réel ; aligner la Template ClickUp (ajouter Tasks si voulu, clarifier Phase en champ) ; script d'init DEC-008 ; ou premières entrées pilotes.

## Documents de référence

- `AGENTS.md`
- `brain/DECISIONS.md`
- `brain/TASKS.md`
- `brain-main/templates/README.md`
- `brain-main/skills/clickup/SKILL.md`
- `README.md`
