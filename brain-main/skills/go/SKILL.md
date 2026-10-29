---
name: go
description: >-
  Identifie le contexte depuis brain/, lit STATE et propose une seule
  prochaine commande. À utiliser avec /go. Ne rien écrire.
disable-model-invocation: true
---

# /go — Démarrer la session

1. Lire `AGENTS.md` et **`brain/STATE.md`**.
2. Compléter si besoin avec `brain/OVERVIEW.md`, `brain/TASKS.md` (actives), et un coup d’œil à `brain/DECISIONS.md` pour les questions ouvertes.
3. Si `.clickup/mapping.yaml` nomme un dossier projet et que les outils ClickUp sont dispo : lecture seule utile — signaler les contradictions avec le local, sans écrire.
4. Proposer **une seule** prochaine commande parmi : `/statut`, `/note`, `/sync`, `/cadrer`, `/build`, `/clickup`, `/spec`, `/faire`, `/audit`, `/fin`.
5. En dogfooding Second Brain : préférer la commande qui fait avancer `brain-main/` selon `STATE.next_action` / tâches actives.
6. S’arrêter. Aucune écriture dépôt ni ClickUp.
