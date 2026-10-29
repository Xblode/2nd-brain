# Politique mémoire

- Conserver le durable dans des fichiers lisibles.
- Réutiliser un document existant quand la portée est la même.
- Ne pas créer un fichier par idée ou par conversation.
- Ne pas écrire automatiquement dans l'Inbox.
- Traiter SQLite comme une projection reconstructible.
- Proposer, puis attendre une approbation humaine.
- **Ne jamais jeter une idée ou une info en silence** : proposer une destination (`registry/ideas`, décisions, tâches, references) ou demander où la ranger.
- **Mettre à jour sans supprimer** : préférer append, patch ciblé, ou nouvelle entrée + `supersedes`. Interdit d’écraser un fichier entier ou d’effacer une entrée sans proposition explicite et accord.

Créer un document seulement s'il a une portée durable, un lecteur identifiable et un usage distinct. Sinon, rattacher l'information à un document existant, ou (humain) la laisser dans l'Inbox jusqu'au triage.

Une proposition indique : cible, opération (`append` | `patch` | `add_entry` | `supersede`), raison, contenu ou diff, sources, et risque de conflit. L'application **relit la cible avant d'écrire** et conserve le contenu non concerné.

## Registre et cycle de vie (DEC-006, sérialisation DEC-009)

- Conteneur : Markdown versionné en **collections** (plusieurs entrées par fichier).
- Sérialisation d'une entrée : objet JSON strict sur **une ligne physique** dans un bloc `jsonl` (DEC-009). Pas de prose dupliquant l'entrée sous la ligne.
- Contrats : `taxonomy.yaml`, `registry-schema.json`.
- Foyers : décisions/questions → `brain/DECISIONS.md` ; tâches → `brain/TASKS.md` ; autres kinds → `brain/registry/{kind}s.md` au premier besoin (ex. `ideas.md`).
- Toute nouvelle entrée durable démarre en `proposed` (sauf capture Inbox, hors registre).
- Seul un humain fait passer `proposed` → `accepted` | `rejected` | `deferred` (DEC-003).
- Après acceptation : `decision` → `settled` ; `task`/`issue` → `active` puis `blocked`|`resolved` ; `question` → `active` jusqu'à `resolved` ; `fact`/`reference` restent `accepted` (ou `superseded`) ; `idea`/`hypothesis` : `accepted` = on garde ; promotion = nouvelles entrées liées (`derived_from`), pas de changement de kind in-place.
- Contradiction : lier `contradicts`, ne pas écraser.
- Remplacement : nouvelle entrée + `supersedes` ; l'ancienne passe `superseded`.

## Intégrations (DEC-007) — jalon 1

- Flux : Chat → local (`brain/`) → projection ClickUp après accord.
- Le local porte tous les champs (y compris tâches) ; entrées JSONL optimisées pour l'IA.
- ClickUp = projection humaine ; le skill lit `brain/TASKS.md` et pousse après approbation.
- Ne pas écraser le local pour coller à ClickUp/Notion sans proposition approuvée.
