# Architecture

Responsabilités et relations. À compléter pendant `/cadrer`.

| Zone | Responsabilité |
| --- | --- |
| `brain/` | Mémoire de **ce** projet (état, décisions, tâches, registre au besoin). |
| `brain-main/` | Système partagé (lié via `.second-brain.yaml`, non vendu en entier). |
| `brain-main/templates/project/` | Modèle générique d’où vient cette mémoire (ne pas confondre avec `brain/`). |
| Fichiers canoniques | Source de vérité versionnée (Markdown + entrées JSONL). |
| SQLite (`brain/runtime/`) | Index reconstructible — jamais SoT. |
| MCP / CLI | Interfaces éventuelles ; partagent la logique `core/` si implémentée. |
| Intégrations | Opérations externes encadrées (`integrations/` + mapping local + approbation). |

## Flux mémoire (référence)

```
Chat → comprendre & classer (skills)
     → proposer écriture dans brain/ (sans supprimer l'existant)
     → accord humain → appliquer
     → /clickup : prévisualiser → accord → projeter ClickUp
```

Inbox = capture manuelle seulement. ClickUp n’est jamais la source des champs.
