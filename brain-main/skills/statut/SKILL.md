---
name: statut
description: >-
  Affiche l'état du projet depuis brain/STATE.md et les compléments brain/,
  sans écrire. À utiliser avec /statut.
disable-model-invocation: true
---

# /statut — État (lecture seule)

## Lecture

**`brain/STATE.md`** en maître. Compléments : `brain/OVERVIEW.md`, `brain/TASKS.md`, `brain/DECISIONS.md` (ouvertes). Ne pas inventer une date de sync absente. Ignorer les `docs/` web s’ils n’existent pas.

## Sortie

```text
PROJET · [nom]
Phase : [lue ou inconnue]
Dernière màj STATE : [si connue]

Terminé / validé
[faits et décisions settled / tâches resolved — seulement si lus]

En attente
[décisions ou dépendances ouvertes]

PROCHAINE ACTION
[une action] — résultat attendu : […]

Priorités
1. …
2. …
3. …
```

Aucune modification de fichier ni ClickUp.
