# Tâches

Collection canonique (DEC-006 / DEC-007, sérialisation DEC-009) : bloc `jsonl`, **un objet JSON strict par ligne physique**.
Le local est la source de vérité ; ClickUp est une projection (`brain-main/skills/clickup/SKILL.md`).
Contrats : `registry-schema.json`, `taxonomy.yaml`.

## Proposed

```jsonl
{"id":"TASK-011","kind":"task","status":"proposed","title":"Tableau message→fichier→preuve dans le rapport C","summary":"Rédiger le tableau message → fichier → opération → preuve dans le rapport Sub-agent C (preview /note).","created":"2026-10-29","updated":"2026-10-29","sources":["conversation","test M1 TASK-008"],"relations":[{"type":"related_to","target_id":"TASK-008"}],"scope":"system","list":"LIST.TASKS","milestone":"M1","acceptance":["Tableau message→destination→opération→contenu exact","Confirmation aucune idée omise","Liste des IDs proposés"]}
```

## Active

```jsonl
{"id":"TASK-012","kind":"task","status":"active","title":"Push ClickUp après mapping (écart M1)","summary":"Créer LIST.TASKS sous Projets/2nd Brain, ajouter .clickup/mapping.yaml + status_map, harmoniser list=LIST.TASKS, puis /clickup preview + push après accord.","created":"2026-10-29","updated":"2026-10-29","sources":["conversation","clôture M1","subagent D"],"relations":[{"type":"related_to","target_id":"TASK-009"},{"type":"related_to","target_id":"DEC-007"},{"type":"related_to","target_id":"DEC-010"}],"scope":"system","list":"LIST.TASKS","milestone":"M1.1","acceptance":["mapping.yaml projet avec IDs réels","LIST.TASKS existe","Lot TASK- prévisualisé puis poussé après oui","Inbox intacte"]}
```

## Resolved

```jsonl
{"id":"TASK-009","kind":"task","status":"resolved","title":"Flux Chat → local → ClickUp","summary":"Preview MCP réelle OK ; push non fait — écart accepté à la clôture M1, reporté en TASK-012.","created":"2026-10-29","updated":"2026-10-29","sources":["conversation","DEC-007","subagent D","clôture M1"],"relations":[{"type":"related_to","target_id":"DEC-007"},{"type":"related_to","target_id":"DEC-010"},{"type":"depends_on","target_id":"TASK-008"},{"type":"related_to","target_id":"TASK-012"}],"scope":"system","list":"LIST.TASKS","milestone":"M1","acceptance":["Au moins un lot TASK- projeté ou prévisualisé avec outils réels","Local reste SoT","Inbox jamais écrite par l'IA"]}
{"id":"TASK-010","kind":"task","status":"resolved","title":"Clôturer jalon 1","summary":"M1 clos 2026-10-29 : critères 1–3 OK ; critère 4 partiel (preview OK, push → TASK-012). phase=m1_done.","created":"2026-10-29","updated":"2026-10-29","sources":["conversation","brain/OVERVIEW.md","clôture M1"],"relations":[{"type":"depends_on","target_id":"TASK-007"},{"type":"depends_on","target_id":"TASK-008"},{"type":"depends_on","target_id":"TASK-009"}],"scope":"system","list":"LIST.TASKS","milestone":"M1","acceptance":["Critères OVERVIEW M1 cochés avec preuves","Pas de dérive vers runtime avant M1 done"]}
{"id":"TASK-007","kind":"task","status":"resolved","title":"Valider et tester l'architecture brain/","summary":"Template project/brain aligné structurellement sur brain/ (Sub-agent A). Contenu dogfood non recopié.","created":"2026-10-29","updated":"2026-10-29","sources":["conversation","brain/OVERVIEW.md","subagent A"],"relations":[{"type":"related_to","target_id":"DEC-010"}],"scope":"system","list":"LIST.TASKS","milestone":"M1","acceptance":["Un agent retrouve l'état sans inventer","Template project/brain aligne sur l'exemple","Écarts documentés via /sync ou /audit"]}
{"id":"TASK-008","kind":"task","status":"resolved","title":"Skills : comprendre, classer, ranger sans perte","summary":"Skills anti-perte + 3 messages test → IDEA-001/002, DEC-011/012, TASK-011 écrits après oui.","created":"2026-10-29","updated":"2026-10-29","sources":["conversation","brain/OVERVIEW.md","subagent B","subagent C"],"relations":[{"type":"related_to","target_id":"DEC-010"},{"type":"related_to","target_id":"TASK-007"}],"scope":"system","list":"LIST.TASKS","milestone":"M1","acceptance":["/note et /cadrer proposent une destination pour chaque idée","Pas de suppression silencieuse de contenu existant","Test manuel : 3 messages hétérogènes correctement rangés"]}
{"id":"TASK-001","kind":"task","status":"resolved","title":"Poser l'arborescence brain-main et brain","summary":"Arborescence système commun et mémoire de dépôt en place.","created":"2026-10-29","updated":"2026-10-29","sources":["brain/STATE.md"],"relations":[],"scope":"system","list":"LIST.TASKS"}
{"id":"TASK-002","kind":"task","status":"resolved","title":"Distinguer mémoire dépôt et modèle projet","summary":"brain/ vs templates/project/ clarifiés (DEC-001).","created":"2026-10-29","updated":"2026-10-29","sources":["brain/DECISIONS.md"],"relations":[{"type":"related_to","target_id":"DEC-001"}],"scope":"system","list":"LIST.TASKS"}
{"id":"TASK-003","kind":"task","status":"resolved","title":"Contrats d'intégration sans secrets","summary":"Contrats GitHub / ClickUp / Notion documentés, sans connexion auto.","created":"2026-10-29","updated":"2026-10-29","sources":["brain-main/integrations/"],"relations":[{"type":"related_to","target_id":"DEC-005"}],"scope":"system","list":"LIST.TASKS"}
{"id":"TASK-004","kind":"task","status":"resolved","title":"Modèle de données et cycle de vie","summary":"DEC-006 adoptée ; OPEN-001 résolu.","created":"2026-10-29","updated":"2026-10-29","sources":["brain/DECISIONS.md"],"relations":[{"type":"related_to","target_id":"DEC-006"}],"scope":"system","list":"LIST.TASKS"}
{"id":"TASK-005","kind":"task","status":"resolved","title":"Réconciliation local / ClickUp / Notion","summary":"DEC-007 adoptée — local SoT ; ClickUp projection.","created":"2026-10-29","updated":"2026-10-29","sources":["conversation","brain/DECISIONS.md"],"relations":[{"type":"related_to","target_id":"DEC-007"}],"scope":"system","list":"LIST.TASKS"}
{"id":"TASK-006","kind":"task","status":"resolved","title":"Définir déploiement et mise à jour du template","summary":"DEC-008 adoptée — copy_once / sync_shared / link_only ; manifeste template.","created":"2026-10-29","updated":"2026-10-29","sources":["brain/DECISIONS.md","brain-main/templates/project/template-manifest.yaml"],"relations":[{"type":"related_to","target_id":"DEC-008"}],"scope":"system","list":"LIST.TASKS"}
```

## Blocked

```jsonl
```
