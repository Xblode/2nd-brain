---
name: fin
description: >-
  Clôture session. Commande /fin. Résoudre brain_main_path puis suivre le Skill canonique.
disable-model-invocation: true
---

# /fin

1. Lire `.second-brain.yaml` et résoudre `brain_main_path` (relatif au dépôt, sous-module ou chemin absolu).
2. Si absent, null ou inaccessible : **le signaler** ; ne pas prétendre avoir chargé la procédure ; se limiter aux fichiers locaux du projet.
3. Ouvrir et suivre `{brain_main_path}/skills/fin/SKILL.md`.
Catalogue : `{brain_main_path}/skills/COMMANDS.md`.

Mettre à jour `brain/STATE.md` après accord.
