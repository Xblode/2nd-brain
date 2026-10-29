---
name: build
description: >-
  Organisation globale du registre (analyse, tri, validation, écriture locale,
  puis projection ClickUp). Sous-mode scaffold : template / dogfood brain-main.
  À utiliser avec /build.
disable-model-invocation: true
---

# /build — Organisation globale (DEC-011)

Lire d’abord : `brain/STATE.md`, `brain/PROCESS.md`, `brain/PRINCIPLES.md`, `brain/OBJECTIVES.md`, `brain/ROADMAP.md`, registres (`DECISIONS`, `TASKS`, `registry/`).

Autorité : conventions `brain-main/conventions/` (format / cycle de vie) ; docs `brain/` (quoi / quand projet). Ne pas inventer de règle locale.

## Mode A — Organisation registre (défaut)

Traite les entrées `proposed` (et lots à trier) accumulées en brainstorming.

1. Inventorier les entrées pending (id, kind, title, contradictions, alignement objectifs/roadmap).
2. Proposer un plan de tri par entrée ou groupe :
   - garder / fusionner / différer / rejeter ;
   - promouvoir → `task` / `decision` / patch doc cadrage (nouvelle entrée liée `derived_from` si besoin) ;
   - signaler conflits et priorités.
3. **Validation humaine sélective** :
   - lot global pour le triage évident ;
   - questions explicites pour conflits, priorités, suppressions de sens, création/modif de docs cadrage.
4. Attendre l’accord sur **ce lot exact**. Noter dans `STATE.md` : `Build: proposé` puis `Build: appliqué` après écriture.
5. Appliquer uniquement l’approuvé en local (`add_entry` / `patch` / `supersede` ; relire avant écriture). Pas d’Inbox.
6. Proposer ensuite `/clickup` pour projeter le sous-ensemble local validé (prévisualisation → accord → push). Local reste SoT.

## Mode B — Scaffold / dogfood (sous-mode)

Seulement si l’utilisateur demande explicitement un scaffold, une install template, ou un lot de construction `brain-main` / pack web.

### B1 — Dogfooding Second Brain

1. Lister le lot exact (fichiers `brain-main/…` et màj `brain/` éventuelles).
2. Accord sur ce lot → appliquer → maj `STATE` / `TASKS`.

### B2 — Nouveau projet / template

1. Proposer copie depuis `templates/project/` (manifeste DEC-008).
2. Pack `web-starter` : optionnel, seulement si profil web retenu.
3. Accord → copier sans écraser le project-owned → noter résultat.

## Interdit

- Promouvoir en silence tout le registre sans validation.
- Écrire dans Inbox.
- Prendre ClickUp comme SoT.
- Imposer `web-starter`.
- Lancer le mode scaffold sans demande explicite alors que des entrées `proposed` attendent un triage.
