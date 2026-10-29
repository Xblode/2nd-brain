---
name: fin
description: >-
  Résume la session, propose les écritures brain/ à enregistrer et la prochaine
  action. À utiliser avec /fin. Écriture seulement après oui.
disable-model-invocation: true
---

# /fin — Clôture de session

1. Lire la conversation et **`brain/STATE.md`** (compléments `TASKS` / `DECISIONS` si cités).
2. Montrer trois blocs : décisions à ajouter dans `DECISIONS.md` ; questions ouvertes ; **une** prochaine action pour `STATE.md`.
3. Si tâches locales ou ClickUp en jeu : ne proposer `resolved` / terminé que s’il y a preuve dans la conversation ; sinon « pas assez de preuve ».
4. Attendre un oui avant de modifier `brain/STATE.md` et les autres fichiers `brain/` listés. Ce oui ne clôture pas les tâches distantes.
5. Second oui listant les `TASK-` / IDs exacts avant toute mise à jour de statut (local puis `/clickup` si projection).
6. Pas de création de liste ClickUp. Pas d’Inbox.
