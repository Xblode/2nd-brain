# 04 — Mémoire

## Sources

1. Fichiers canoniques, lisibles et versionnés.
2. Registre : éléments atomiques. Le format n'est pas choisi.
3. Documents de synthèse : état, décisions, tâches, architecture.
4. Index SQLite local, reconstructible, jamais seule copie d'une décision.
5. Journaux techniques temporaires, distincts de la mémoire durable.

Une information importante doit pouvoir se relire dans un fichier. Le registre et les synthèses ne doivent pas se contredire en silence : une seule source est désignée comme référence.

Les préférences récurrentes peuvent être suggérées. Une préférence confirmée et une inférence restent distinctes. Changer une règle commune demande une décision explicite dans `brain-main/`.

## Pas encore décidé

Le cycle de vie d'une information (création, proposition, validation, remplacement, contradiction) et le modèle de données qui le porte. Voir `brain/DECISIONS.md`.
