# Commandes Second Brain

Catalogue des commandes `/` exposées via `.cursor/skills/`.  
Canon : dossiers sous `brain-main/skills/<commande>/SKILL.md`.

## Mémoire projet (obligatoire)

Toutes les commandes s’ancrent dans **`brain/`**.

| Chemin | Rôle |
| --- | --- |
| `brain/STATE.md` | État maître |
| `brain/OBJECTIVES.md` | Vision / périmètre |
| `brain/ROADMAP.md` | Jalons |
| `brain/PRINCIPLES.md` | Non négociables + autorité |
| `brain/PROCESS.md` | Pipeline |
| `brain/ARCHITECTURE.md` | Zones / modes |
| `brain/GLOSSARY.md` | Vocabulaire |
| `brain/DECISIONS.md` | Décisions & questions (JSONL) |
| `brain/TASKS.md` | Tâches (JSONL) |
| `brain/inbox/` | Capture manuelle uniquement |
| `brain/registry/` | Autres kinds au besoin |

Dogfooding : on fait évoluer **`brain-main/`** en s’appuyant sur cette mémoire.  
Pack `web-starter` : **optionnel**.

## Pipeline V1

```text
Chat / prompt → brainstorm (/note, agents)
             → registre proposed
             → /build (organisation)
             → validation → local
             → /clickup
```

Critères : `brain/ROADMAP.md`. Décision : DEC-011. Tâches : TASK-011 … TASK-014.  
Anti-perte : `memory-policy.md` + `/note`.

| Commande | Skill | Rôle |
| --- | --- | --- |
| `/note` | `note` | Capturer / classer vers registre ou docs cadrage (prévisualisation) |
| `/build` | `build` | **Organisation globale** du registre → local → propose ClickUp ; sous-mode scaffold |
| `/cadrer` | `cadrer` | Cadrage via `brain/` ; stop avant scaffold / code |
| `/go` | `go` | Contexte `brain/` + une seule prochaine commande |
| `/statut` | `statut` | État, blocages, priorités (lecture seule) |
| `/sync` | `sync` | Écarts vs structure `brain/` attendue → lot à approuver |
| `/clickup` | `clickup` | Projection local → ClickUp (souvent en fin de `/build`) |
| `/spec` | `spec` | Spec testable ancrée dans `TASKS` / registry |
| `/faire` | `faire` | Implémenter une tranche déjà approuvée |
| `/ui` | `ui` | Revue UI/UX |
| `/done` | `done` | Revue avant de déclarer terminé (preuves) |
| `/audit` | `audit` | Contradictions entre fichiers `brain/` |
| `/fin` | `fin` | Clôture de session |

ClickUp : `brain-main/skills/clickup/modules/convention.md` (DEC-007). Autorité des règles : `brain/PRINCIPLES.md`.
