# Décisions

Collection canonique (DEC-006, sérialisation DEC-009) : bloc `jsonl`, **un objet JSON strict par ligne physique**.
Contrats : `brain-main/conventions/registry-schema.json`, `taxonomy.yaml`.
Détails de fond : `memory-policy.md`, `naming.md`, `templates/README.md`, `skills/clickup/modules/sync.md`.

**Alias historiques (lecture seule) :** `D-00x` → `DEC-00x`, `O-00x` → `OPEN-00x`.

## Settled

```jsonl
{"id":"DEC-001","kind":"decision","status":"settled","title":"Séparer système commun et mémoire projet","summary":"brain-main/ porte les règles communes ; brain/ porte la mémoire de ce dépôt. Un autre projet reçoit templates/project/, pas une copie de tout brain-main/.","created":"2026-10-29","updated":"2026-10-29","sources":["conversation","brain/ARCHITECTURE.md"],"relations":[],"scope":"system"}
{"id":"DEC-002","kind":"decision","status":"settled","title":"Fichiers canoniques","summary":"Les fichiers lisibles versionnés sont la source de vérité ; SQLite est un index reconstructible.","created":"2026-10-29","updated":"2026-10-29","sources":["conversation"],"relations":[],"scope":"system"}
{"id":"DEC-003","kind":"decision","status":"settled","title":"Validation humaine","summary":"Une écriture durable proposée par un modèle attend une approbation humaine distincte. Le modèle ne s'approuve pas.","created":"2026-10-29","updated":"2026-10-29","sources":["conversation"],"relations":[],"scope":"system"}
{"id":"DEC-004","kind":"decision","status":"settled","title":"Inbox manuelle","summary":"Aucune automatisation n'écrit dans l'Inbox.","created":"2026-10-29","updated":"2026-10-29","sources":["conversation"],"relations":[],"scope":"system"}
{"id":"DEC-005","kind":"decision","status":"settled","title":"Intégrations","summary":"Contrats communs dans brain-main/integrations/ ; .clickup/ et .notion/ sans secret ni MCP.","created":"2026-10-29","updated":"2026-10-29","sources":["conversation","brain-main/integrations/"],"relations":[],"scope":"system"}
{"id":"DEC-006","kind":"decision","status":"settled","title":"Modèle de données canonique et cycle de vie","summary":"Registre en collections Markdown versionnées, IDs stables par kind, cycle de vie explicite ; clôture OPEN-001. Sérialisation des entrées : DEC-009. Contrats taxonomy.yaml et registry-schema.json.","created":"2026-10-29","updated":"2026-10-29","sources":["conversation","plan O-001 (Build approuvé)","brain-main/conventions/taxonomy.yaml","brain-main/conventions/registry-schema.json"],"relations":[{"type":"derived_from","target_id":"OPEN-001"}],"scope":"system"}
{"id":"DEC-007","kind":"decision","status":"settled","title":"Local source de vérité ; ClickUp projection humaine","summary":"Le local porte tous les champs (y compris tâches). ClickUp est la vue humaine ; le skill lit le local et pousse après approbation. Pas de sync silencieuse. Clôture OPEN-002.","created":"2026-10-29","updated":"2026-10-29","sources":["conversation","brain-main/integrations/clickup.md","brain-main/skills/clickup/modules/sync.md"],"relations":[{"type":"derived_from","target_id":"OPEN-002"},{"type":"related_to","target_id":"DEC-006"}],"scope":"system"}
{"id":"DEC-008","kind":"decision","status":"settled","title":"Déploiement du template et mises à jour","summary":"Politiques copy_once / sync_shared / link_only via template-manifest.yaml ; brain-main lié par .second-brain.yaml ; mises à jour propose-only. Clôture OPEN-003. Script non implémenté.","created":"2026-10-29","updated":"2026-10-29","sources":["conversation","brain-main/templates/README.md","DEC-001"],"relations":[{"type":"derived_from","target_id":"OPEN-003"},{"type":"related_to","target_id":"DEC-001"}],"scope":"system"}
{"id":"DEC-009","kind":"decision","status":"settled","title":"Format compact JSONL des collections","summary":"Sérialisation des entrées de registre : conteneur Markdown + bloc jsonl, un objet JSON strict par ligne physique. Ne change pas les principes de fond DEC-006 (collections, IDs, kinds, relations, cycle de vie).","created":"2026-10-29","updated":"2026-10-29","sources":["conversation","mission consolidation squelette"],"relations":[{"type":"related_to","target_id":"DEC-006"}],"scope":"system"}
{"id":"DEC-010","kind":"decision","status":"settled","title":"Jalon 1 — Chat vers local puis ClickUp","summary":"Premier jalon roadmap : communiquer et conventionner Chatbot → infos en local (brain/) → projection ClickUp. Valider l'architecture dossiers projet. Skills doivent classer/ranger/mettre à jour sans suppression silencieuse ni perte d'idées. Runtime et pack web hors M1.","created":"2026-10-29","updated":"2026-10-29","sources":["conversation","brain/OVERVIEW.md"],"relations":[{"type":"related_to","target_id":"DEC-007"},{"type":"related_to","target_id":"TASK-007"}],"scope":"system"}
```

## Resolved

```jsonl
{"id":"OPEN-001","kind":"question","status":"resolved","title":"Modèle de données","summary":"Tranché par DEC-006 — collections Markdown, IDs stables, cycle de vie explicite ; sérialisation précisée par DEC-009.","created":"2026-10-29","updated":"2026-10-29","sources":["conversation","brain/STATE.md"],"relations":[{"type":"related_to","target_id":"DEC-006"}],"scope":"system"}
{"id":"OPEN-002","kind":"question","status":"resolved","title":"Synchronisation","summary":"Tranché par DEC-007 — local SoT complète ; ClickUp projection via skill ; pas de sync silencieuse.","created":"2026-10-29","updated":"2026-10-29","sources":["conversation","brain/STATE.md"],"relations":[{"type":"related_to","target_id":"DEC-007"}],"scope":"system"}
{"id":"OPEN-003","kind":"question","status":"resolved","title":"Déploiement du template","summary":"Tranché par DEC-008 — copy_once / sync_shared / link_only ; brain-main par référence.","created":"2026-10-29","updated":"2026-10-29","sources":["conversation","brain/STATE.md"],"relations":[{"type":"related_to","target_id":"DEC-008"}],"scope":"system"}
```
