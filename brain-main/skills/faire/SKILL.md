---
name: faire
description: >-
  Implémente une tâche ou tranche déjà approuvée (souvent dans brain-main/
  en dogfooding), avec vérifications et périmètre limité. À utiliser avec /faire.
disable-model-invocation: true
---

# /faire — Implémenter une tranche

## Prérequis

Tâche / spec approuvée. Lire `brain/STATE.md`, l’entrée `TASK-` concernée, `brain/ARCHITECTURE.md`, décisions liées.

## Workflow

1. Lire la tâche, l’architecture, et les fichiers cibles (souvent sous `brain-main/` pour Second Brain).
2. Inspecter Git ; préserver le travail non commité.
3. Annoncer fichiers, hypothèses, vérifications ; accord si le plan n’est pas déjà approuvé.
4. Implémenter **uniquement** le périmètre approuvé.
5. Tests / lint / build s’ils existent ; sinon contrôles manuels pertinents ; rapporter commandes et résultats réels.
6. Mettre à jour la doc concernée sous `brain-main/` et, après oui si durable, `brain/TASKS.md` / `STATE.md`.
7. Relire le diff (secrets, hors périmètre).
8. Résumer : changement, vérifs, limites, tâche suivante. Proposer `/done` si fin de tranche.

## Interdit

- Élargir au pack web ou à une stack non décidée.
- Écrire dans Inbox.
- Annoncer succès sans preuve observable.
