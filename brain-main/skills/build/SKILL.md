---
name: build
description: >-
  Après cadrage, applique un lot de construction : socle projet (template),
  évolutions brain-main en dogfooding, ou pack web optionnel. À utiliser avec /build.
disable-model-invocation: true
---

# /build — Construction après décision

## Prérequis

`brain/STATE.md` (et idéalement `OVERVIEW` / `DECISIONS`) contient un dossier de décision, ou l’utilisateur confirme construire avec les hypothèses affichées. Sinon renvoyer vers `/cadrer`.

Lire d’abord : `brain/STATE.md`, `brain/OVERVIEW.md`, `brain/ARCHITECTURE.md`, `brain/DECISIONS.md`, `brain/TASKS.md`.  
Compléments selon le lot : `brain-main/templates/project/template-manifest.yaml` (DEC-008), et seulement si profil web retenu `templates/web-starter/README.md` + `STACK_PROFILES.md`.

## Deux modes

### A — Dogfooding Second Brain (ce dépôt)

Objectif : faire avancer **`brain-main/`** (skills, conventions, docs, emplacements runtime) en s’appuyant sur la mémoire **`brain/`**.

1. Lister le lot exact (fichiers `brain-main/…` et éventuelles màj `brain/TASKS.md` / `STATE.md`).
2. Noter dans `STATE.md` : `Build: proposé`. Attendre accord sur **ce lot**.
3. Appliquer uniquement le périmètre approuvé. Pas d’installation stack web sauf demande explicite.
4. Mettre à jour `brain/STATE.md` / `TASKS.md` avec le résultat réel. `Build: appliqué`.

### B — Nouveau projet / template

1. Proposer ce qui est copié depuis `templates/project/` (manifeste DEC-008) vs laissé de côté.
2. **Pack `web-starter` : optionnel**, seulement si le cadrage a retenu un profil web. Sinon ne pas l’installer.
3. Noter `Build: proposé` dans `STATE.md`. Attendre accord.
4. Copier selon le manifeste sans écraser le project-owned (`brain/STATE.md`, mappings, etc.).
5. Si pack web accepté : copier docs/rules/prompts retenus ; installer la stack du profil ; vérifier la doc officielle ; rapporter les résultats réels.
6. Un générateur qui refuse un dossier non vide : générer en temporaire, fusionner sans écraser `brain/`, `.cursor/`, `.github/`, docs déjà validés.
7. Skills optionnels du pack → `.cursor/skills/` seulement si listés dans l’accord.
8. Noter `Build: installé` puis validations / commit si demandés (`Build: commité`).

## Tâches et ClickUp

- Plan local : toujours `brain/TASKS.md` (JSONL DEC-009).
- Roadmap `docs/06-delivery/…` : seulement si pack web présent et utile.
- Projection ClickUp : lot séparé via `/clickup`. Sans connexion : rester en local.

## Interdit

- Imposer `web-starter` comme étape obligatoire.
- Réutiliser IDs ClickUp d’un autre projet.
- Écrire dans Inbox.
- Écraser la mémoire `brain/` existante pour coller à un modèle générique.
