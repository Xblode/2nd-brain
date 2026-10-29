# Module — Proposition d'écriture

1. Vérifier que l'information mérite d'être conservée.
2. Chercher un document canonique ou une entrée existante (même portée).
3. Choisir le foyer selon le kind (DEC-006) :
   - `decision` / `question` → `brain/DECISIONS.md`
   - `task` → `brain/TASKS.md`
   - `fact` / `hypothesis` / `idea` / `issue` / `reference` → fichier collection sous `brain/registry/` (créer le fichier seulement au premier besoin)
4. Préparer une entrée au schéma `registry-schema.json` : **une ligne JSON** dans le bloc `jsonl` de la collection (DEC-009). Nouveau id monotone avec le préfixe du kind (`taxonomy.yaml`). Statut initial : `proposed`. Pas de prose dupliquant l'entrée sous la ligne.
5. Exclure toute cible sous `inbox/`.
6. Opération proposée : `append` | `patch` | `add_entry` | `supersede` uniquement.
7. Demander une approbation humaine. Ne pas l'accorder soi-même (DEC-003).
8. Après accord, relire la cible avant d'écrire ; appliquer le statut validé (`accepted` / `rejected` / `deferred`, puis transitions de kind).
9. En cas de contradiction : lier `contradicts`, ne pas écraser. En cas de remplacement : nouvelle entrée + `supersedes`, ancienne → `superseded`.
10. Rapporter le résultat réel. Ne pas prétendre qu'un parser, MCP, CLI ou index SQLite a été exécuté.
