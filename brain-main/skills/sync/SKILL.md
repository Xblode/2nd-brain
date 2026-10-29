---
name: sync
description: >-
  Compare la structure brain/ attendue (et packs optionnels) à l'existant,
  propose un lot de créations ou mises à jour. À utiliser avec /sync.
disable-model-invocation: true
---

# /sync — Écarts documentaires

## Objectif

Voir ce qui manque ou est en retard dans la mémoire projet, sans réécrire un doc approuvé en silence.

## Référence attendue (par défaut)

Structure **`brain/`** — exemple pratique : le `brain/` de Second Brain + modèle `brain-main/templates/project/brain/` + `INFORMATION_MAP.yaml` :

- Docs cadrage : `STATE.md`, `OBJECTIVES.md`, `ROADMAP.md`, `PRINCIPLES.md`, `PROCESS.md`, `ARCHITECTURE.md`, `GLOSSARY.md`, `README.md`
- Registres : `DECISIONS.md`, `TASKS.md`
- `inbox/`, `registry/`, `references/`, `runtime/` (README / emplacements)
- `OVERVIEW.md` : pointeur optionnel seulement (plus SoT)

Pack `web-starter` / `docs/…` : comparer **seulement** si `STATE` indique que le pack est installé ou que le projet est explicitement web.

## Workflow

1. Lire **`brain/STATE.md`**, puis lister les fichiers `brain/` présents.
2. Pour chaque doc attendu de la structure mémoire : présent / incomplet / absent. Pas de doublon sous un autre nom.
3. En dogfooding : signaler aussi les écarts évidents entre ce que `brain/` décide et ce qui manque encore sous `brain-main/` (rapport, sans tout réécrire).
4. Montrer le lot (créations / patches). `replace` seulement si la page entière est dans le lot.
5. Attendre un oui. Cet oui **ne** couvre **pas** les tâches ClickUp (`/clickup`).
6. Après écriture : mettre à jour `brain/STATE.md` si l’état change. Relire et rapporter.
7. Sans outil distant : rester en Markdown local.
