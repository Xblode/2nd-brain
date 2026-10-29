# Second Brain

Mémoire de projet locale, lisible et contrôlée — et **lanceur de projets** via des commandes Cursor.  
Ce dépôt est encore en grande partie un **squelette documentaire** : la présence d’un dossier ne prouve pas qu’un runtime est implémenté.

## Trois niveaux

| Emplacement | Fonction |
| --- | --- |
| `brain-main/` | Règles, contrats, skills et packs communs. Une seule source. |
| `brain/` | Mémoire de **ce** dépôt (dont l’état maître `brain/STATE.md`). |
| `brain-main/templates/project/` | Socle mémoire copié dans un futur projet (DEC-008). |
| `brain-main/templates/web-starter/` | Pack web : docs, rules, modèles — **pas** une application. |

## Principes

- Brainstorming d’abord ; lots ensuite ; code sur demande.
- Conventions communes dans `brain-main/` ; ClickUp = projection (DEC-007), clés `LIST.*`.
- **`brain/` est la mémoire projet** (`STATE.md` = seul état maître ; plus `OVERVIEW`, `ARCHITECTURE`, `DECISIONS`, `TASKS`). Pas de `PROJECT_STATE.md` concurrent.
- Dogfooding : on construit `brain-main/` en s’appuyant sur `brain/` (exemple pratique de test).
- Pack `web-starter` = optionnel (projet web), jamais la mémoire par défaut.
- Écriture canonique : proposition puis approbation humaine. Inbox = capture manuelle uniquement.
- SQLite = index dérivé. Secrets hors Git.

## Commandes

Canon : `brain-main/skills/<nom>/SKILL.md`.  
Stubs Cursor : `.cursor/skills/<nom>/` (recharger une conversation Agent après ajout).  
Catalogue : `brain-main/skills/COMMANDS.md`.

### Lancer / cadrer

| Commande | Fait |
| --- | --- |
| `/cadrer` | Cadrage via `brain/` (reprise de l’existant) ; s’arrête avant install. |
| `/build` | Lot de construction : template, évolutions `brain-main`, ou pack web **si** décidé. |

Dogfooding typique : `/cadrer` (sur SB) → lots dans `TASKS` → `/faire` sur `brain-main/`.  
Projet web neuf : `/cadrer` → `/build` (pack optionnel) → `/spec` → `/faire`.

### Pilotage

| Commande | Fait |
| --- | --- |
| `/go` | Contexte `brain/` + **une** prochaine commande. N’écrit rien. |
| `/statut` | Phase, blocages, priorités (lecture seule). |
| `/note` | Un élément dans `brain/` après prévisualisation. Pas d’Inbox IA. |
| `/sync` | Écarts vs structure `brain/` attendue → lot à approuver. |
| `/audit` | Contradictions entre fichiers `brain/` (+ `brain-main` en dogfood). |
| `/fin` | Clôture de session ; écritures seulement après oui. |

### Exécution

| Commande | Fait |
| --- | --- |
| `/spec` | Spec testable ancrée dans `TASKS` / registry. |
| `/faire` | Implémenter une tranche déjà approuvée. |
| `/ui` | Revue UI/UX (si pertinent). |
| `/done` | Revue avant de déclarer terminé (preuves). |

### ClickUp

| Commande | Fait |
| --- | --- |
| `/clickup` | Prévisualise puis (après accord) projette le **local** vers ClickUp. Convention Second Brain uniquement (`LIST.*`, DEC-007). |

Ne pas utiliser d’anciennes conventions de listes métier (Cadrage / Web, etc.).

## Décisions de cadrage adoptées

| Décision | Contenu |
| --- | --- |
| DEC-006 | Registre : collections Markdown, IDs stables, cycle de vie. |
| DEC-007 | Local = SoT ; ClickUp = projection humaine. |
| DEC-008 | Template : `copy_once` / `sync_shared` / `link_only` ; `brain-main` par référence. |
| DEC-009 | Sérialisation : une entrée = un objet JSON par ligne physique (`jsonl`). |

Voir `brain/DECISIONS.md`, `brain-main/conventions/taxonomy.yaml`, `registry-schema.json`.

## Travaux restants (non implémentés)

- Parser / validation des collections JSONL
- Services registre, recherche, propositions
- Index SQLite reconstructible
- Serveur MCP, CLI, scripts d’init/update template automatiques
- Sync runtime ClickUp / Notion
- `/build` pleinement automatisé (aujourd’hui procédure skill + outils disponibles)

## Lecture

1. `brain/STATE.md`
2. `brain-main/skills/COMMANDS.md`
3. `brain-main/docs/00-vision.md`
4. `AGENTS.md`
