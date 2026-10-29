# Tâches

Collection canonique (DEC-006 / DEC-007, sérialisation DEC-009) : bloc `jsonl`, **un objet JSON strict par ligne physique**.
Le local est la source de vérité ; ClickUp est une projection (`brain-main/skills/clickup/SKILL.md`).
Contrats : `registry-schema.json`, `taxonomy.yaml`.

## Active

```jsonl
{"id":"TASK-011","kind":"task","status":"active","title":"Valider docs cadrage obligatoires brain/","summary":"Checklist V1 : STATE, OBJECTIVES, ROADMAP, PRINCIPLES, PROCESS, ARCHITECTURE, GLOSSARY, README — cohérents avec template project et utilisables en dogfooding.","created":"2026-10-29","updated":"2026-10-29","sources":["conversation","DEC-011","brain/ROADMAP.md"],"relations":[{"type":"related_to","target_id":"DEC-011"},{"type":"supersedes","target_id":"TASK-007"},{"type":"blocks","target_id":"TASK-012"}],"scope":"system","list":"Tasks","milestone":"V1","acceptance":["Un agent retrouve objectifs/process sans inventer","OVERVIEW n'est plus SoT concurrente","Template project/brain aligné sur la liste obligatoire"]}
{"id":"TASK-012","kind":"task","status":"active","title":"Skills /note et /build alignés pipeline","summary":"/note capture vers registres et docs obligatoires ; /build mode organisation analyse/trie/valide/écrit local puis propose ClickUp ; scaffold = sous-mode.","created":"2026-10-29","updated":"2026-10-29","sources":["conversation","DEC-011","brain/PROCESS.md"],"relations":[{"type":"related_to","target_id":"DEC-011"},{"type":"supersedes","target_id":"TASK-008"},{"type":"blocks","target_id":"TASK-013"}],"scope":"system","list":"Tasks","milestone":"V1","acceptance":["COMMANDS.md et skills build/note/cadrer citent PROCESS et docs obligatoires","Brainstorm = proposed sans promotion auto","/build documenté comme passe globale"]}
{"id":"TASK-013","kind":"task","status":"active","title":"Parcours bout-en-bout local puis ClickUp","summary":"Tester : brainstorm → entrées registre → /build organisation → local validé → /clickup prévisualise (et pousse si accord).","created":"2026-10-29","updated":"2026-10-29","sources":["conversation","DEC-007","DEC-011"],"relations":[{"type":"related_to","target_id":"DEC-007"},{"type":"related_to","target_id":"DEC-011"},{"type":"supersedes","target_id":"TASK-009"},{"type":"blocks","target_id":"TASK-014"}],"scope":"system","list":"Tasks","milestone":"V1","acceptance":["Au moins un lot organisé en local avec preuves","Projection ClickUp proposée après local","Inbox jamais écrite par l'IA"]}
{"id":"TASK-014","kind":"task","status":"active","title":"Clôturer jalon V1","summary":"Quand TASK-011–013 passent /done : STATE phase=v1_done, noter preuves, ouvrir post-V1 seulement après.","created":"2026-10-29","updated":"2026-10-29","sources":["conversation","brain/ROADMAP.md"],"relations":[{"type":"related_to","target_id":"TASK-011"},{"type":"related_to","target_id":"TASK-012"},{"type":"related_to","target_id":"TASK-013"},{"type":"supersedes","target_id":"TASK-010"}],"scope":"system","list":"Tasks","milestone":"V1","acceptance":["Critères ROADMAP V1 cochés avec preuves","Pas de dérive runtime avant v1_done"]}
```

## Resolved

```jsonl
{"id":"TASK-001","kind":"task","status":"resolved","title":"Poser l'arborescence brain-main et brain","summary":"Arborescence système commun et mémoire de dépôt en place.","created":"2026-10-29","updated":"2026-10-29","sources":["brain/STATE.md"],"relations":[],"scope":"system","list":"Tasks"}
{"id":"TASK-002","kind":"task","status":"resolved","title":"Distinguer mémoire dépôt et modèle projet","summary":"brain/ vs templates/project/ clarifiés (DEC-001).","created":"2026-10-29","updated":"2026-10-29","sources":["brain/DECISIONS.md"],"relations":[{"type":"related_to","target_id":"DEC-001"}],"scope":"system","list":"Tasks"}
{"id":"TASK-003","kind":"task","status":"resolved","title":"Contrats d'intégration sans secrets","summary":"Contrats GitHub / ClickUp / Notion documentés, sans connexion auto.","created":"2026-10-29","updated":"2026-10-29","sources":["brain-main/integrations/"],"relations":[{"type":"related_to","target_id":"DEC-005"}],"scope":"system","list":"Tasks"}
{"id":"TASK-004","kind":"task","status":"resolved","title":"Modèle de données et cycle de vie","summary":"DEC-006 adoptée ; OPEN-001 résolu.","created":"2026-10-29","updated":"2026-10-29","sources":["brain/DECISIONS.md"],"relations":[{"type":"related_to","target_id":"DEC-006"}],"scope":"system","list":"Tasks"}
{"id":"TASK-005","kind":"task","status":"resolved","title":"Réconciliation local / ClickUp / Notion","summary":"DEC-007 adoptée — local SoT ; ClickUp projection.","created":"2026-10-29","updated":"2026-10-29","sources":["conversation","brain/DECISIONS.md"],"relations":[{"type":"related_to","target_id":"DEC-007"}],"scope":"system","list":"Tasks"}
{"id":"TASK-006","kind":"task","status":"resolved","title":"Définir déploiement et mise à jour du template","summary":"DEC-008 adoptée — copy_once / sync_shared / link_only ; manifeste template.","created":"2026-10-29","updated":"2026-10-29","sources":["brain/DECISIONS.md","brain-main/templates/project/template-manifest.yaml"],"relations":[{"type":"related_to","target_id":"DEC-008"}],"scope":"system","list":"Tasks"}
{"id":"TASK-007","kind":"task","status":"resolved","title":"Valider et tester l'architecture brain/","summary":"Remplacée par TASK-011 (docs cadrage V1). Ancien critère M1 OVERVIEW/ARCHITECTURE absorbé.","created":"2026-10-29","updated":"2026-10-29","sources":["DEC-011"],"relations":[{"type":"related_to","target_id":"DEC-010"},{"type":"related_to","target_id":"TASK-011"}],"scope":"system","list":"Tasks","milestone":"M1"}
{"id":"TASK-008","kind":"task","status":"resolved","title":"Skills : comprendre, classer, ranger sans perte","summary":"Remplacée par TASK-012 (alignement /note et /build pipeline).","created":"2026-10-29","updated":"2026-10-29","sources":["DEC-011"],"relations":[{"type":"related_to","target_id":"DEC-010"},{"type":"related_to","target_id":"TASK-012"}],"scope":"system","list":"Tasks","milestone":"M1"}
{"id":"TASK-009","kind":"task","status":"resolved","title":"Flux Chat → local → ClickUp","summary":"Remplacée par TASK-013 (parcours /build puis ClickUp).","created":"2026-10-29","updated":"2026-10-29","sources":["DEC-011"],"relations":[{"type":"related_to","target_id":"DEC-010"},{"type":"related_to","target_id":"TASK-013"}],"scope":"system","list":"Tasks","milestone":"M1"}
{"id":"TASK-010","kind":"task","status":"resolved","title":"Clôturer jalon 1","summary":"Remplacée par TASK-014 (clôture V1).","created":"2026-10-29","updated":"2026-10-29","sources":["DEC-011"],"relations":[{"type":"related_to","target_id":"TASK-014"}],"scope":"system","list":"Tasks","milestone":"M1"}
```

## Blocked

```jsonl
```
