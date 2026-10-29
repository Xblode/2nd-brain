# Mémoire du projet

Mémoire propre à ce projet. Distincte de `brain-main/` (non recopié ici).  
Référence de structure : le `brain/` du dépôt Second Brain (exemple pratique).

## Navigation

1. Lire `STATE.md` en premier.
2. Consulter ensuite uniquement les fichiers pertinents.
3. `OVERVIEW.md` — vision / brief.
4. `ARCHITECTURE.md` — zones et responsabilités.
5. `DECISIONS.md` — décisions et questions (collection JSONL).
6. `TASKS.md` — tâches (collection JSONL).
7. `registry/` / `references/` — au besoin.
8. Ne jamais écrire automatiquement dans `inbox/`.
9. Ne pas créer un fichier par idée ou conversation.

| Chemin | Rôle |
| --- | --- |
| `STATE.md` | État, blocages, prochaine action |
| `OVERVIEW.md` | Vision / brief |
| `ARCHITECTURE.md` | Zones et responsabilités |
| `DECISIONS.md` | Décisions et questions (JSONL) |
| `TASKS.md` | Tâches (JSONL) |
| `inbox/` | Capture manuelle uniquement |
| `registry/` | Autres kinds, au besoin |
| `references/` | Pointeurs externes |
| `runtime/` | Index local dérivé (hors Git) — jamais SoT |

## Format des collections

Conteneur Markdown ; entrées = objets JSON, une ligne physique chacun (DEC-009).  
Contrats : `{brain_main_path}/conventions/` (`taxonomy.yaml`, `registry-schema.json`).  
Les docs d’un pack web (`docs/…`) sont optionnels et ne remplacent pas cette mémoire.
