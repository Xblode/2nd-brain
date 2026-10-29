# AGENTS.md — Instructions communes du dépôt Second Brain

Règles durables pour tout agent (Cursor, Claude, Copilot, etc.).  
Les détails métier vivent dans `brain/` ; les contrats système dans `brain-main/conventions/`.

## 1. Avant de commencer

1. Lire `brain/STATE.md` (état réel).
2. Selon le besoin, lire les **docs de cadrage obligatoires** :
   - `OBJECTIVES.md`, `ROADMAP.md`, `PRINCIPLES.md`, `PROCESS.md`, `ARCHITECTURE.md`, `GLOSSARY.md`
   - registres : `DECISIONS.md`, `TASKS.md`, `registry/`
3. Pour le système : `brain-main/` (conventions, skills, docs). Commandes : `brain-main/skills/COMMANDS.md`.
4. ClickUp : `/clickup` (`brain-main/skills/clickup/SKILL.md`) — projection seulement (DEC-007).
5. Distinguer implémenté / documenté / proposé. Un dossier ou README ≠ runtime fonctionnel.

## 2. Sources de vérité

| Zone | Rôle |
| --- | --- |
| `brain-main/conventions/` | Constitution (taxonomy, schéma, memory-policy, naming) |
| `brain/*.md` obligatoires | Loi du projet (objectifs, process, principes…) |
| `brain/` registres | SoT data (entrées JSONL) |
| `brain-main/skills/` | Procédures — citent constitution et loi, ne les remplacent pas |
| ClickUp | Projection humaine — jamais SoT des champs |

Détail : `brain/PRINCIPLES.md`. Pipeline : `brain/PROCESS.md`. Décisions : DEC-001…011 dans `brain/DECISIONS.md`.

## 3. Pipeline V1 (DEC-011)

```text
Prompt → brainstorm → registre (proposed) → /build → validation
      → local → /clickup
```

- Brainstorming : accumuler des entrées `proposed` ; pas de promotion auto en tâches.
- `/build` : organisation globale du registre (sous-mode scaffold = template / dogfood).
- Approbation humaine sur les choix structurants et les lots.
- Hors V1 : MCP, CLI, SQLite SoT, recherche vectorielle obligatoire.

## 4. Interdits

- Écrire dans `brain/inbox/` (Inbox manuelle seulement).
- S’auto-approuver ; supprimer du contenu en silence.
- Traiter SQLite / ClickUp / Notion comme SoT.
- Créer un fichier Markdown par idée (utiliser le registre).
- Secrets dans Git.
- Présenter le runtime non implémenté comme fonctionnel.
- Prendre `web-starter` comme mémoire par défaut.

## 5. Écritures et fin de lot

- Proposition puis accord humain avant écriture durable.
- Opérations registre : `append` / `patch` / `add_entry` / `supersede`.
- Fin de lot : vérifier le périmètre, rapporter preuves et contrôles non exécutés ; ne pas annoncer commit/push/sync sans confirmation observable.

## 6. Maintenance de ce fichier

Rester court. Ne pas republier `PROCESS` / `PRINCIPLES` / DEC en long ici. État → `STATE.md` ; décisions → `DECISIONS.md`.
