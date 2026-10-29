# Tâches

Collection canonique (DEC-006 / DEC-007, sérialisation DEC-009) : bloc `jsonl`, **un objet JSON strict par ligne physique**.
Le local est la source de vérité ; ClickUp est une projection (`brain-main/skills/clickup/SKILL.md`).
Contrats : `registry-schema.json`, `taxonomy.yaml`.

## Active

```jsonl
{"id":"TASK-007","kind":"task","status":"active","title":"Valider et tester l'architecture brain/","summary":"Checklist : STATE, OVERVIEW, ARCHITECTURE, DECISIONS, TASKS, inbox, registry, references, runtime — cohérents avec template project et utilisables en dogfooding.","created":"2026-10-29","updated":"2026-10-29","sources":["conversation","brain/OVERVIEW.md"],"relations":[{"type":"related_to","target_id":"DEC-010"}],"scope":"system","list":"Tasks","milestone":"M1","acceptance":["Un agent retrouve l'état sans inventer","Template project/brain aligne sur l'exemple","Écarts documentés via /sync ou /audit"]}
{"id":"TASK-008","kind":"task","status":"active","title":"Skills : comprendre, classer, ranger sans perte","summary":"Messages classés vers la bonne destination brain/ ; mise à jour par patch/append/supersede ; aucune idée ni info jetée en silence.","created":"2026-10-29","updated":"2026-10-29","sources":["conversation","brain/OVERVIEW.md"],"relations":[{"type":"related_to","target_id":"DEC-010"},{"type":"related_to","target_id":"TASK-007"}],"scope":"system","list":"Tasks","milestone":"M1","acceptance":["/note et /cadrer proposent une destination pour chaque idée","Pas de suppression silencieuse de contenu existant","Test manuel : 3 messages hétérogènes correctement rangés"]}
{"id":"TASK-009","kind":"task","status":"active","title":"Flux Chat → local → ClickUp","summary":"Conventionner et tester : chat → écriture locale approuvée → /clickup prévisualise puis pousse après accord.","created":"2026-10-29","updated":"2026-10-29","sources":["conversation","DEC-007"],"relations":[{"type":"related_to","target_id":"DEC-007"},{"type":"related_to","target_id":"DEC-010"},{"type":"depends_on","target_id":"TASK-008"}],"scope":"system","list":"Tasks","milestone":"M1","acceptance":["Au moins un lot TASK- projeté ou prévisualisé avec outils réels","Local reste SoT","Inbox jamais écrite par l'IA"]}
{"id":"TASK-010","kind":"task","status":"active","title":"Clôturer jalon 1","summary":"Quand TASK-007–009 passent /done : mettre STATE phase=m1_done, noter preuves, ouvrir jalon 2 seulement après.","created":"2026-10-29","updated":"2026-10-29","sources":["conversation","brain/OVERVIEW.md"],"relations":[{"type":"depends_on","target_id":"TASK-007"},{"type":"depends_on","target_id":"TASK-008"},{"type":"depends_on","target_id":"TASK-009"}],"scope":"system","list":"Tasks","milestone":"M1","acceptance":["Critères OVERVIEW M1 cochés avec preuves","Pas de dérive vers runtime avant M1 done"]}
```

## Resolved

```jsonl
{"id":"TASK-001","kind":"task","status":"resolved","title":"Poser l'arborescence brain-main et brain","summary":"Arborescence système commun et mémoire de dépôt en place.","created":"2026-10-29","updated":"2026-10-29","sources":["brain/STATE.md"],"relations":[],"scope":"system","list":"Tasks"}
{"id":"TASK-002","kind":"task","status":"resolved","title":"Distinguer mémoire dépôt et modèle projet","summary":"brain/ vs templates/project/ clarifiés (DEC-001).","created":"2026-10-29","updated":"2026-10-29","sources":["brain/DECISIONS.md"],"relations":[{"type":"related_to","target_id":"DEC-001"}],"scope":"system","list":"Tasks"}
{"id":"TASK-003","kind":"task","status":"resolved","title":"Contrats d'intégration sans secrets","summary":"Contrats GitHub / ClickUp / Notion documentés, sans connexion auto.","created":"2026-10-29","updated":"2026-10-29","sources":["brain-main/integrations/"],"relations":[{"type":"related_to","target_id":"DEC-005"}],"scope":"system","list":"Tasks"}
{"id":"TASK-004","kind":"task","status":"resolved","title":"Modèle de données et cycle de vie","summary":"DEC-006 adoptée ; OPEN-001 résolu.","created":"2026-10-29","updated":"2026-10-29","sources":["brain/DECISIONS.md"],"relations":[{"type":"related_to","target_id":"DEC-006"}],"scope":"system","list":"Tasks"}
{"id":"TASK-005","kind":"task","status":"resolved","title":"Réconciliation local / ClickUp / Notion","summary":"DEC-007 adoptée — local SoT ; ClickUp projection.","created":"2026-10-29","updated":"2026-10-29","sources":["conversation","brain/DECISIONS.md"],"relations":[{"type":"related_to","target_id":"DEC-007"}],"scope":"system","list":"Tasks"}
{"id":"TASK-006","kind":"task","status":"resolved","title":"Définir déploiement et mise à jour du template","summary":"DEC-008 adoptée — copy_once / sync_shared / link_only ; manifeste template.","created":"2026-10-29","updated":"2026-10-29","sources":["brain/DECISIONS.md","brain-main/templates/project/template-manifest.yaml"],"relations":[{"type":"related_to","target_id":"DEC-008"}],"scope":"system","list":"Tasks"}
```

## Blocked

```jsonl
```
