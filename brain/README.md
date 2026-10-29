# Mémoire de ce dépôt

Mémoire du projet qui construit Second Brain.  
Ne pas confondre avec `brain-main/` (système) ni `brain-main/templates/project/brain/` (modèle générique).

## Docs de cadrage obligatoires

Lire dans cet ordre selon le besoin :

1. `STATE.md` — état actuel, priorités, blocages
2. `OBJECTIVES.md` — vision, usagers, périmètre
3. `ROADMAP.md` — jalons et critères de passage
4. `PRINCIPLES.md` — règles non négociables + autorité des conventions
5. `PROCESS.md` — pipeline idée → registre → `/build` → ClickUp
6. `ARCHITECTURE.md` — zones et modes
7. `GLOSSARY.md` — vocabulaire et cycle de vie

## Registres (données)

- `DECISIONS.md` — décisions et questions (JSONL)
- `TASKS.md` — tâches (JSONL)
- `registry/` — autres kinds (`ideas`, etc.)
- `references/` — pointeurs externes au besoin

## Règles courtes

- Ne jamais écrire automatiquement dans `inbox/`.
- Ne pas créer un fichier Markdown par idée : utiliser le registre.
- Format registre actuel : conteneur Markdown + JSONL (DEC-009). Contrats : `registry-schema.json`, `taxonomy.yaml`.
