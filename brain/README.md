# Mémoire de ce dépôt

Mémoire du projet qui construit Second Brain. À ne pas confondre avec :

- `brain-main/` — règles et contrats communs ;
- `brain-main/templates/project/brain/` — modèle générique pour d'autres projets.

## Navigation

1. Lire `STATE.md` en premier.
2. Consulter ensuite uniquement les fichiers pertinents.
3. `OVERVIEW.md` — vision / brief.
4. `ARCHITECTURE.md` — zones et responsabilités.
5. `DECISIONS.md` — décisions et questions (collection JSONL).
6. `TASKS.md` — tâches (collection JSONL).
7. `registry/` / `references/` — au besoin.
8. Ne jamais écrire automatiquement dans `inbox/`.
9. Ne pas créer un fichier par idée ou conversation.

Ce dossier est l’**exemple pratique** pour les commandes `/` et le dogfooding : on fait évoluer `brain-main/` en s’appuyant sur cette mémoire.

## Format des collections

Conteneur Markdown ; entrées = objets JSON, une ligne physique chacun (DEC-009). Validation : `registry-schema.json` + `taxonomy.yaml`.
