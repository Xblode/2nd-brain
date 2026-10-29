# Politique mémoire

- Conserver le durable dans des fichiers lisibles.
- Réutiliser un document existant quand la portée est la même.
- Ne pas créer un fichier par idée ou par conversation.
- Ne pas écrire automatiquement dans l'Inbox.
- Traiter SQLite comme une projection reconstructible.
- Proposer, puis attendre une approbation humaine.

Créer un document seulement s'il a une portée durable, un lecteur identifiable et un usage distinct. Sinon, rattacher l'information à un document existant, ou la laisser dans l'Inbox jusqu'au triage.

Une proposition indique : cible, opération, raison, contenu ou diff, sources, et risque de conflit. L'application relit la cible avant d'écrire.

Le format du registre et le cycle de vie d'une entrée ne sont pas fixés. Ne pas les inventer dans un fichier technique tant que `brain/DECISIONS.md` ne les marque pas comme acceptés.
