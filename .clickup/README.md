# ClickUp — correspondance du projet (dogfood Second Brain)

Convention Second Brain (DEC-007). ClickUp ne découvre pas ce dossier et il ne connecte pas le MCP.

- **Local** = source de vérité (tâches dans `brain/TASKS.md`, format IA).
- **ClickUp** = vue humaine ; le skill lit le local et pousse ici après approbation.

## Emplacement ClickUp

| Niveau | Nom | ID |
| --- | --- | --- |
| Workspace | — | `90151633729` |
| Space | Projets | `90156746497` |
| Folder | 2nd Brain | `1201110000005979` |

## Contenu de `mapping.yaml`

- `resources.lists` : clés logiques stables → IDs ClickUp **de ce projet**
  - Socle : `LIST.INBOX`, `LIST.DOCS`
  - Options : `LIST.TASKS`, `LIST.ROADMAP`, `LIST.BUGS`
- `sync.mode` : défaut `propose_only`
- `sync.status_map` : statut registre local → libellé statut ClickUp du projet (Open / Closed ; écart phases web documenté)
- Aucun token ici. Ne jamais coller les IDs de la Template ou d’un autre dossier.

Le champ `list` d’une entrée locale utilise la clé (`LIST.TASKS`), pas le nom affiché.

Après un push réussi : mettre à jour `clickup.task_id`, `list_id`, `last_pushed` sur l’entrée (voir `brain-main/skills/clickup/modules/sync.md`).

`source_of_truth` doit rester `local`.
