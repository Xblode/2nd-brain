# État — Second Brain

## Résumé

- **Objectif :** une mémoire locale pour projets et agents, lisible sans base opaque.
- **Phase :** squelette d'emplacements. Le modèle de données n'est pas figé.
- **État :** les dossiers existent. Le cœur, le MCP, la CLI, l'index et les scripts ne sont pas implémentés.

## Décisions déjà tenues

- Brainstorming d'abord, agent de code sur un lot choisi.
- `brain-main/` est la source commune. `brain/` est la mémoire de ce dépôt.
- Les projets ne recopient pas tout `brain-main/`.
- Écriture durable seulement après validation humaine.
- L'Inbox est manuelle.
- SQLite sera un index dérivé.
- `.clickup/` et `.notion/` sont des conventions de correspondance, pas des connexions.
- Les secrets restent hors de Git.

## Prochaine action

Définir le modèle de données canonique et le cycle de vie d'une information avant d'écrire le registre, le MCP, les agents ou un script de déploiement.

## Ouvert

- Format du registre.
- Réconciliation local / ClickUp / Notion.
- Contenu copié du template et stratégie de mise à jour.
