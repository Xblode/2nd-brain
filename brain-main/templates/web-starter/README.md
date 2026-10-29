# Pack web-starter

Kit **documentaire et agentique** pour lancer un projet web avec Second Brain.  
Ce n’est **pas** une application : aucun `src/`, aucun site à copier.

Provenance des idées de workflow : skills / rules / arborescence docs d’un starter kit web externe — **réécrits** pour Second Brain.

## Ce que contient ce pack

| Zone | Contenu |
| --- | --- |
| `docs/` | Squelette produit / design / archi / data / qualité / livraison + modèles |
| `rules/` | Rules Cursor d’ingénierie (frontend, sécu, Next, garde ClickUp SB…) |
| `docs/90-templates/` | Modèles FEAT, tâches, DoD, FIRST_PROMPT, skills/rules optionnels |
| `prompts/` | Secours si les commandes `/` ne sont pas disponibles |
| `scripts/validate-kit.mjs` | Contrôle de forme du pack installé dans un projet |

## Ce qu’il ne contient pas

- Code applicatif, assets, `package.json` produit
- Convention ClickUp d’un autre dépôt (listes Cadrage/Web, etc.)
- Un second fichier d’état concurrent : **`brain/STATE.md` est le seul état maître**

## Installation

1. Socle mémoire : `templates/project/` (DEC-008) + `brain_main_path`
2. Cadrage : `/cadrer`
3. Après dossier de décision : `/build` copie ce pack (docs/rules acceptés) dans le projet cible
4. Commands : stubs sous `.cursor/skills/` (voir `brain-main/skills/COMMANDS.md`)

## Docs attendus (après install typique)

Socle discovery (compléments de `brain/STATE.md`, pas un doublon d’état) :

- `docs/00-discovery/PROJECT_BRIEF.md`
- `docs/00-discovery/OPEN_QUESTIONS.md`
- `docs/00-discovery/ASSUMPTIONS_RISKS.md`
- `docs/00-discovery/SKILLS_SELECTION.md`

Puis selon besoin : `01-product` … `06-delivery`.  
**Pas** de `PROJECT_STATE.md` : l’état court vit dans `brain/STATE.md`.

## ClickUp

Toujours `brain-main/skills/clickup/` + `.clickup/mapping.yaml` du projet (`LIST.*`).  
La rule `rules/clickup-write-guard.mdc` pointe vers cette convention.
