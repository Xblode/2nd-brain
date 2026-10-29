# Principes

Règles non négociables de ce projet. Détail procédural : `PROCESS.md`. Contrats système : `brain-main/conventions/`.

## Non négociables

1. **Fichiers canoniques = source de vérité** ; SQLite éventuel = index dérivé seulement.
2. **Écriture durable = proposition puis approbation humaine** (validation sélective sur les choix structurants et les lots `/build`).
3. **Inbox manuelle uniquement** — aucune IA n’écrit dans `brain/inbox/`.
4. **Anti-perte** — toute idée a une destination proposée ; pas de suppression silencieuse (`append` / `patch` / `add_entry` / `supersede`).
5. **Local SoT** — ClickUp (et Notion) sont des projections ; jamais la source des champs.
6. **Aucun secret dans Git.**
7. **Brainstorming volumineux OK** — entrées en `proposed` dans les registres ; la promotion en tâches / docs / décisions acceptées passe par `/build` (ou accord explicite équivalent).
8. **Ne pas inventer le runtime** — MCP, CLI, index : documentés comme non implémentés tant que non prouvés.

## Matrice d’autorité

| Couche | Foyer | Décide |
| --- | --- | --- |
| Constitution | `brain-main/conventions/` | Taxonomy, schéma, politique mémoire, naming, gouvernance |
| Loi du projet | `brain/*.md` obligatoires | Objectifs, roadmap, process, principes, glossaire, état |
| Procédures | `brain-main/skills/` | Ordre des étapes `/note`, `/build`, `/clickup` — citent constitution et loi, ne les remplacent pas |
| Entrée outils | `AGENTS.md`, rules Cursor/Claude | Pointeurs courts |
| Projection | `.clickup/mapping.yaml` + skill clickup | Listes `LIST.*` seulement |

**Conflits :** `brain/PRINCIPLES` + `PROCESS` > skill pour le « quoi / quand » projet ; `brain-main/conventions/*` > skill pour format et cycle de vie ; **local > ClickUp** pour les champs.
