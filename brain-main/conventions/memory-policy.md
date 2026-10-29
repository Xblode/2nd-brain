# Politique mémoire

- Conserver le durable dans des fichiers lisibles.
- Docs de cadrage obligatoires = SoT narrative ; registres = SoT data (DEC-011).
- Réutiliser un document existant quand la portée est la même.
- Ne pas créer un fichier Markdown par idée ou par conversation — utiliser le registre.
- **Brainstorming volumineux OK** : accumuler des entrées `proposed` ; ne pas promouvoir automatiquement en tâches.
- **Promotion** : via `/build` (organisation) ou accord humain explicite équivalent.
- Ne pas écrire automatiquement dans l’Inbox.
- Traiter SQLite comme une projection reconstructible (hors chemin critique V1).
- Proposer, puis attendre une approbation humaine (validation sélective sur les choix structurants).
- **Ne jamais jeter une idée ou une info en silence** : proposer une destination registre / docs ou demander où la ranger.
- **Mettre à jour sans supprimer** : `append`, `patch`, `add_entry`, ou nouvelle entrée + `supersedes`. Interdit d’écraser un fichier entier ou d’effacer une entrée sans proposition et accord.

Créer un document de cadrage seulement s’il a une portée durable et un usage distinct de la liste obligatoire. Sinon, rattacher l’information à un doc existant ou au registre.

Une proposition indique : cible, opération (`append` | `patch` | `add_entry` | `supersede`), raison, contenu ou diff, sources, et risque de conflit. L’application **relit la cible avant d’écrire** et conserve le contenu non concerné.

## Registre et cycle de vie (DEC-006, sérialisation DEC-009)

- Conteneur : Markdown versionné en **collections** (plusieurs entrées par fichier).
- Sérialisation : objet JSON strict sur **une ligne physique** dans un bloc `jsonl`.
- Contrats : `taxonomy.yaml`, `registry-schema.json`.
- Foyers : décisions/questions → `brain/DECISIONS.md` ; tâches → `brain/TASKS.md` ; autres kinds → `brain/registry/{kind}s.md` au premier besoin.
- Toute nouvelle entrée durable démarre en `proposed` (sauf capture Inbox, hors registre).
- Seul un humain (ou un lot `/build` explicitement approuvé) fait passer `proposed` → `accepted` | `rejected` | `deferred` (DEC-003).
- Après acceptation : `decision` → `settled` ; `task`/`issue` → `active` puis `blocked`|`resolved` ; etc. Voir `taxonomy.yaml`.
- Contradiction : lier `contradicts`, ne pas écraser.
- Remplacement : nouvelle entrée + `supersedes` ; l’ancienne passe `superseded`.

## Intégrations (DEC-007) — pipeline V1

- Flux : Prompt → brainstorm → registre → `/build` → local → projection ClickUp après accord.
- Le local porte tous les champs ; ClickUp = projection humaine.
- Ne pas écraser le local pour coller à ClickUp/Notion sans proposition approuvée.
