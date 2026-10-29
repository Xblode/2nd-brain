---
name: audit
description: >-
  Signale les contradictions entre brain/STATE, OBJECTIVES, ROADMAP,
  PRINCIPLES, PROCESS, ARCHITECTURE, DECISIONS et TASKS, puis propose des
  corrections. À utiliser avec /audit.
disable-model-invocation: true
---

# /audit — Rapport d’écarts

1. Lire **`brain/STATE.md`**, `OBJECTIVES.md`, `ROADMAP.md`, `PRINCIPLES.md`, `PROCESS.md`, `ARCHITECTURE.md`, `DECISIONS.md`, `TASKS.md`.
2. Comparer décisions entre elles et avec les tâches / l’état / le process annoncé.
3. En dogfooding : vérifier que ce que `brain/` affirme comme « existant » vs « prévu » colle à `brain-main/` (dossiers vides ≠ runtime).
4. Si pack web présent et livraison en cours : criteria + définition de terminé du pack.
5. Lister écarts : document, contradiction, correction proposée.
6. Distinguer contrôle agent vs décision humaine. Portes utiles : spec avant code ; `/done` avant « terminé ».
7. S’arrêter au rapport sauf validation d’un lot de corrections.
