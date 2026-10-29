# Décisions

## Acceptées

### D-001 — Séparer système commun et mémoire projet

`brain-main/` porte les règles communes. `brain/` porte la mémoire de ce dépôt. Un autre projet reçoit `templates/project/`, pas une copie de tout `brain-main/`.

### D-002 — Fichiers canoniques

Les fichiers lisibles sont la source de vérité. SQLite sera un index reconstructible.

### D-003 — Validation humaine

Une écriture durable proposée par un modèle attend une approbation humaine distincte. Le modèle ne s'approuve pas.

### D-004 — Inbox manuelle

Aucune automatisation n'écrit dans l'Inbox.

### D-005 — Intégrations

Les contrats communs sont dans `brain-main/integrations/`. `.github/` est reconnu par GitHub. `.clickup/` et `.notion/` sont des conventions de correspondance, sans secret et sans connexion MCP.

## Ouvertes

### O-001 — Modèle de données

Markdown structuré ou JSON atomique, identifiants, relations, métadonnées, et cycle de vie d'une information. `taxonomy.yaml` et `registry-schema.json` sont des emplacements, pas une décision.

### O-002 — Synchronisation

Comment un changement local, ClickUp ou Notion est proposé, validé et réconcilié. Qui est propriétaire de quel champ.

### O-003 — Déploiement du template

Ce qui est copié dans un projet, ce qui reste lié à `brain-main/`, et comment une mise à jour préserve les personnalisations.
