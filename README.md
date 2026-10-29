# Second Brain

Mémoire de projet locale, lisible et contrôlée. Ce dépôt est un squelette : les dossiers décrivent des emplacements cibles. Leur présence ne signifie pas que le composant est implémenté.

## Trois niveaux

| Emplacement | Fonction |
| --- | --- |
| `brain-main/` | Règles, contrats et modules communs. Une seule source, pas une copie dans chaque projet. |
| `brain/` | Mémoire du projet qui développe Second Brain. |
| `brain-main/templates/project/` | Modèle copié dans un futur projet. Il ne contient pas tout `brain-main/`. |

## Principes

- Le chat commence par le brainstorming, repère les angles morts et regroupe les changements avant de solliciter un agent de code.
- Les conventions communes restent dans `brain-main/`.
- Une écriture canonique est proposée, puis validée par un humain.
- L'Inbox est en capture manuelle. L'IA n'y écrit pas.
- SQLite est un index dérivé. Les données canoniques restent lisibles sans la base.
- Chaque intégration a un contrat écrit avant d'être implémentée. Les secrets restent dans le client MCP.

## À figer avant de coder

1. Le modèle de données canonique et le cycle de vie d'une information.
2. La synchronisation entre le système local, ClickUp et Notion.
3. Le déploiement du template : ce qui est copié, ce qui reste lié à `brain-main/`, et comment une mise à jour évite d'écraser les personnalisations.

Voir `brain/STATE.md` et `brain/DECISIONS.md`.

## Lecture

1. `brain/STATE.md`
2. `brain-main/docs/00-vision.md`
3. `brain-main/docs/05-sources-verite-integrations.md`
4. `AGENTS.md`
