# Registre

Emplacement cible du **composant runtime** (parser, index, API) — **non implémenté**.

Le **format canonique** est décidé (DEC-006) : Markdown structuré en fichiers collection, IDs stables, cycle de vie explicite. Contrats :

- `brain-main/conventions/taxonomy.yaml` (`status: adopted`)
- `brain-main/conventions/registry-schema.json`

Les entrées projet vivent dans la mémoire du projet (`brain/DECISIONS.md`, `brain/TASKS.md`, `brain/registry/`), pas dans ce dossier runtime.
