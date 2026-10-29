# Commandes Second Brain

Catalogue des commandes `/` exposées via `.cursor/skills/`.  
Canon : dossiers sous `brain-main/skills/<commande>/SKILL.md`.

## Mémoire projet (obligatoire)

Toutes les commandes s’ancrent dans **`brain/`** — exemple pratique : le `brain/` de ce dépôt.

| Chemin | Rôle |
| --- | --- |
| `brain/STATE.md` | **État maître** (jamais un second état concurrent) |
| `brain/OVERVIEW.md` | Vision / brief |
| `brain/ARCHITECTURE.md` | Zones et responsabilités |
| `brain/DECISIONS.md` | Décisions & questions (JSONL) |
| `brain/TASKS.md` | Tâches (JSONL) |
| `brain/inbox/` | Capture manuelle uniquement |
| `brain/registry/`, `references/`, `runtime/` | Au besoin |

Dogfooding : on fait évoluer **`brain-main/`** en s’appuyant sur cette mémoire.  
Pack `web-starter` / `docs/…` : **optionnel**, seulement si un profil web a été décidé via `/build`.

## Jalon 1 — flux à réussir

```
Chat → comprendre & classer (/note, /cadrer, …)
     → écrire en local dans brain/ (après accord, sans supprimer)
     → /clickup : prévisualiser → accord → projeter
```

Critères : `brain/OVERVIEW.md` (section Roadmap M1). Tâches : `TASK-007` … `TASK-010`.  
Anti-perte : `memory-policy.md` + `/note` — aucune idée jetée en silence.

| Commande | Skill | Rôle |
| --- | --- | --- |
| `/cadrer` | `cadrer` | Cadrage via `brain/` (reprise ou brief) ; stop avant install |
| `/build` | `build` | Lot de construction : template, dogfood `brain-main`, ou pack web optionnel |
| `/go` | `go` | Contexte `brain/` + une seule prochaine commande |
| `/statut` | `statut` | État, blocages, priorités (lecture seule) |
| `/note` | `note` | Un élément structuré dans `brain/` après prévisualisation |
| `/sync` | `sync` | Écarts vs structure `brain/` attendue → lot à approuver |
| `/clickup` | `clickup` | Projection local → ClickUp (prévisualisation, convention 2nd-brain) |
| `/spec` | `spec` | Spec testable ancrée dans `TASKS` / registry |
| `/faire` | `faire` | Implémenter une tranche déjà approuvée |
| `/ui` | `ui` | Revue UI/UX |
| `/done` | `done` | Revue avant de déclarer terminé (preuves) |
| `/audit` | `audit` | Contradictions entre fichiers `brain/` (+ `brain-main` en dogfood) |
| `/fin` | `fin` | Clôture de session |

ClickUp : `brain-main/skills/clickup/modules/convention.md` (DEC-007).
