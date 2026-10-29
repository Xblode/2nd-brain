# Architecture

Responsabilités et relations. Détail des composants : leurs README.

| Zone | Responsabilité |
| --- | --- |
| `brain/` | Mémoire de **ce** dépôt (état, décisions, tâches, registre au besoin). |
| `brain-main/` | Système partagé : conventions, docs, skills, contrats, emplacements runtime. |
| `brain-main/templates/project/` | Modèle générique pour futurs projets (pas la mémoire de ce dépôt). |
| Fichiers canoniques | Source de vérité versionnée (Markdown + entrées JSONL). |
| SQLite (`brain/runtime/`) | Index reconstructible — jamais SoT. |
| MCP / CLI | Interfaces futures ; doivent partager la logique `core/` (non implémenté). |
| Intégrations | Opérations externes encadrées par `integrations/` + permissions + approbation. |

```
2nd-brain/
├── brain-main/     système commun
│   ├── conventions/ skills/ docs/ integrations/
│   ├── core/ mcp-server/ cli/ scripts/   # emplacements, non implémentés
│   └── templates/project/
└── brain/          mémoire de ce dépôt
```

`brain/` ≠ `templates/project/brain/`.

## Flux jalon 1 (canonique)

```
Chat (humain) → comprendre & classer (skills)
             → proposer écriture dans brain/ (sans supprimer l'existant)
             → accord humain → appliquer
             → /clickup : prévisualiser → accord → projeter ClickUp
```

Inbox = capture manuelle seulement. ClickUp n’est jamais la source des champs.  
Flux runtime (index, MCP, sync auto) : prévus, hors jalon 1.
