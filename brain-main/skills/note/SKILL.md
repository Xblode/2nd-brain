---
name: note
description: >-
  Comprends un message, le classe, le range dans brain/ sans perte ni
  suppression silencieuse, après prévisualisation. À utiliser avec /note.
  Pas d'Inbox IA. Promotion de masse via /build ; ClickUp via /clickup.
disable-model-invocation: true
---

# /note — Capture structurée (V1)

## Objectif

Un message → **au moins une destination proposée** dans `brain/`.  
Comprendre → classer → ranger → mettre à jour **sans effacer** l’existant.  
Ne jamais laisser une idée « tomber » sans proposition.

Brainstorming : préférer des entrées registre `proposed`. Ne pas promouvoir automatiquement en tâches — ça relève de `/build`.

## Destinations

| Nature | Destination |
| --- | --- |
| Décision / question | `brain/DECISIONS.md` (JSONL, `add_entry`) |
| Tâche vérifiable (si déjà engagée) | `brain/TASKS.md` (JSONL, `add_entry`) |
| Idée / hypothèse / fait | `brain/registry/` — créer la collection au besoin |
| Vision / périmètre | `brain/OBJECTIVES.md` (`patch` ciblé) |
| Jalons | `brain/ROADMAP.md` (`patch` ciblé) |
| Process / principes | `brain/PROCESS.md` / `PRINCIPLES.md` (`patch` ciblé) |
| Zones / relations | `brain/ARCHITECTURE.md` (`patch` ciblé) |
| État opérationnel | `brain/STATE.md` (`patch` court) |
| Pointeur externe | `brain/references/` ou registry `reference` |
| Message mixte | **plusieurs** propositions ordonnées |

`OVERVIEW.md` n’est plus une cible SoT (pointeur seulement).

## Règles anti-perte

1. Toute idée exprimée → entrée `idea` proposée (même floue).
2. Opérations : `append`, `patch`, `add_entry`, `supersede`. Pas de `replace` fichier entier sans accord.
3. Relire la cible **avant** d’écrire.
4. Contradiction : signaler + lier `contradicts`.
5. Remplacement de sens : nouvelle entrée + `supersedes`.

## Workflow

1. Lire `brain/STATE.md` et le(s) fichier(s) cible(s) ; consulter `OBJECTIVES` / `ROADMAP` si le filtrage périmètre compte.
2. Reformuler ce qui doit être conservé.
3. Classer ; si plusieurs natures → lister les éléments.
4. Montrer pour chaque élément : destination, opération, texte exact (ou ligne JSONL), statut `proposed` par défaut.
5. Attendre un oui (global ou par élément).
6. Appliquer uniquement l’approuvé ; confirmer ce qui a changé.
7. Si le registre `proposed` grossit : proposer `/build` pour l’organisation globale — **lot séparé**.
8. Projection ClickUp : via `/build` ou `/clickup` après organisation locale — pas pendant la capture.
9. Ne jamais écrire dans `brain/inbox/`.
