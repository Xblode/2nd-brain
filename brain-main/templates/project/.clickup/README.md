# ClickUp — correspondance du projet

Convention Second Brain (DEC-007). ClickUp ne découvre pas ce dossier et il ne connecte pas le MCP.

- **Local** = source de vérité (tâches dans `brain/TASKS.md`, format IA).
- **ClickUp** = vue humaine ; le skill lit le local et pousse ici après approbation.

Renseigner les identifiants non secrets dans `mapping.yaml`. Laisser `enabled: false` tant que les listes ne sont pas renseignées. `source_of_truth` doit rester `local`. Aucun token ici.
