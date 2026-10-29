---
name: spec
description: >-
  Définit une capacité ou fonctionnalité de façon testable avant exécution,
  ancrée dans brain/ (STATE, TASKS, DECISIONS). À utiliser avec /spec.
disable-model-invocation: true
---

# /spec — Spécification

## Prérequis

Cadrage suffisant dans `brain/OBJECTIVES.md` / `brain/STATE.md` / `brain/PROCESS.md` (et décisions utiles). Profil stack seulement si le lot est applicatif web.

## Où écrire

Par défaut (structure `brain/`) :

1. Reformuler le résultat attendu dans le chat.
2. Après accord : créer ou mettre à jour une entrée `TASK-` (et sous-tâches si besoin) dans **`brain/TASKS.md`**, et si la spec est longue, un document dédié sous **`brain/registry/`** (ex. collection ou fichier `specs.md` JSONL / Markdown court) — **pas** un fichier par idée dispersé.
3. Critères d’acceptation vérifiables dans la tâche ou la spec.
4. Impacts architecture → patch proposé de `brain/ARCHITECTURE.md` si nécessaire.
5. S’arrêter avant le code ; proposer `/faire`.

### Variante pack web (seulement si installé)

Si `docs/01-product/FEATURES/` existe via web-starter : on peut y placer `FEAT-###-nom/spec.md` **en plus** du reflet dans `brain/TASKS.md`. Sinon ne pas créer cette arborescence.

## Dogfooding Second Brain

La « fonctionnalité » est souvent une capacité de `brain-main/` (skill, convention, contrat). La spec décrit le comportement attendu du système ; l’implémentation ira sous `brain-main/` via `/faire`.

## Réussite

Un testeur (humain) peut vérifier chaque critère sans deviner.
