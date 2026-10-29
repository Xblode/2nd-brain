# Templates

| Dossier | Rôle |
| --- | --- |
| `project/` | Socle mémoire + mappings + stubs de commandes. **Ne pas** y copier tout `brain-main/`. |
| `web-starter/` | Pack web optionnel (docs, rules, modèles). **Pas** une application ni la mémoire par défaut. Installé via `/build` seulement si profil web retenu. |

Contrat socle : **DEC-008** + `project/template-manifest.yaml`.  
Commandes : `../skills/COMMANDS.md`. État maître projet : `brain/STATE.md`.

| Politique | Comportement |
| --- | --- |
| `copy_once` | Init seulement ; ensuite propriété du projet (jamais écrasé par une sync template) |
| `sync_shared` | Mise à jour proposée si le fichier projet n'a pas divergé |
| `link_only` | Reste dans `brain-main/` ; le projet pointe via `.second-brain.yaml` → `brain_main_path` |

Init : copier les chemins du manifeste, renseigner `brain_main_path`, adapter `brain/STATE.md` et les mappings.  
Update : `propose_only` + approbation humaine ; script non implémenté (`scripts/README.md`).
