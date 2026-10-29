---
name: note
description: >-
  Comprends un message, le classe, le range dans brain/ sans perte ni
  suppression silencieuse, après prévisualisation. À utiliser avec /note.
  Pas d'Inbox IA. ClickUp ensuite via /clickup.
disable-model-invocation: true
---

# /note — Capture structurée (jalon 1)

## Objectif

Un message → **au moins une destination proposée** dans `brain/`.  
Comprendre → classer → ranger → mettre à jour **sans effacer** l’existant.  
Ne jamais laisser une idée « tomber » sans proposition.

## Destinations

| Nature | Destination |
| --- | --- |
| Décision / question | `brain/DECISIONS.md` (JSONL, `add_entry`) |
| Tâche vérifiable | `brain/TASKS.md` (JSONL, `add_entry`) |
| Vision / périmètre | `brain/OVERVIEW.md` (`patch` ciblé) |
| Zones / relations | `brain/ARCHITECTURE.md` (`patch` ciblé) |
| État opérationnel | `brain/STATE.md` (`patch` court) |
| Idée / hypothèse / fait | `brain/registry/` — créer la collection au besoin (`ideas.md`, `hypotheses.md`, `facts.md`) |
| Pointeur externe | `brain/references/` ou registry `reference` |
| Message mixte | **plusieurs** propositions ordonnées (une par nature), pas un seul fourre-tout |

## Règles anti-perte (M1)

1. Toute idée exprimée → entrée `idea` proposée (même floue) ; ne pas « laisser de côté ».
2. Opérations autorisées : `append`, `patch`, `add_entry`, `supersede`. Pas de `replace` fichier entier sauf accord explicite sur tout le contenu.
3. Relire le fichier cible **avant** d’écrire ; ne toucher que la zone / ligne concernée.
4. Contradiction : signaler + lier `contradicts` ; ne pas écraser.
5. Remplacement de sens : nouvelle entrée + `supersedes` ; ancienne → `superseded`.

## Workflow

1. Lire `brain/STATE.md` et le(s) fichier(s) cible(s) probables.
2. Reformuler en une phrase ce qui doit être conservé (faits / idées / décisions / tâches).
3. Classer ; si plusieurs natures → lister les éléments (max raisonnable, grouper le lié).
4. Montrer pour chaque élément : destination, opération, texte exact (ou ligne JSONL).
5. Attendre un oui (global ou par élément).
6. Appliquer uniquement l’approuvé ; relire ; confirmer ce qui a changé.
7. Projection ClickUp : proposer `/clickup` si des `TASK-` (ou docs projetés) sont concernés — **lot séparé**, local d’abord.
8. Ne jamais écrire dans `brain/inbox/` ni Inbox ClickUp.
