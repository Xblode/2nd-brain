---
name: done
description: >-
  Revue avant de déclarer une tranche terminée, avec preuves. Met à jour
  brain/TASKS.md et STATE.md seulement après oui. À utiliser avec /done.
disable-model-invocation: true
---

# /done — Déclarer terminé

1. Lire la tâche `TASK-` / critères dans `brain/TASKS.md` et le contexte `STATE`.
2. Vérifier chaque critère : `pass` / `fail` / `non exécuté` avec preuve (diff, commande, observation).
3. Contrôler hors périmètre, secrets, docs `brain/` ou `brain-main/` à jour.
4. Si ClickUp en jeu : ne pas marquer distant sans `/clickup` et accord.
5. `ready` seulement si les critères essentiels sont `pass`.
6. Mettre à jour `brain/TASKS.md` / `STATE.md` **après** oui explicite.
