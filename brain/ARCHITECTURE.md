# Architecture

```
2nd-brain/
├── .github/          configuration GitHub de ce dépôt
├── brain-main/       système commun
│   ├── docs/
│   ├── conventions/
│   ├── skills/
│   ├── core/         non implémenté
│   ├── integrations/
│   ├── adapters/
│   ├── mcp-server/   non implémenté
│   ├── cli/          non implémenté
│   ├── scripts/      non implémenté
│   └── templates/project/
└── brain/            mémoire de ce dépôt
```

`brain/` et `templates/project/brain/` ne sont pas interchangeables. Le premier décrit ce dépôt. Le second est le modèle des autres projets.

Recherche prévue : état, puis fichiers canoniques, puis index s'il existe. Écriture prévue : proposition, validation humaine, application. Action externe prévue : outil disponible, proposition, approbation, rapport.

Rien de ces flux n'est codé.
