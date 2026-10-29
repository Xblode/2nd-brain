# Module — Proposition d'écriture

1. Vérifier que l’information mérite d’être conservée.
2. Chercher un document canonique ou une entrée existante (même portée).
3. Choisir le foyer selon le kind (DEC-006) :
   - `decision` / `question` → `brain/DECISIONS.md`
   - `task` → `brain/TASKS.md` (éviter de créer des tâches pendant le pur brainstorm — préférer `idea` puis `/build`)
   - `fact` / `hypothesis` / `idea` / `issue` / `reference` → `brain/registry/` (créer le fichier au premier besoin)
   - patches cadrage → `OBJECTIVES` / `ROADMAP` / `PRINCIPLES` / `PROCESS` / `ARCHITECTURE` / `STATE` selon nature
4. Préparer une entrée au schéma `registry-schema.json` : **une ligne JSON** dans le bloc `jsonl` (DEC-009). Statut initial : `proposed`.
5. Exclure toute cible sous `inbox/`.
6. Demander une approbation humaine (ou lot `/build`). Ne pas s’auto-approuver (DEC-003).
7. Après accord, relire la cible avant d’écrire.
8. Contradiction : lier `contradicts`. Remplacement : `supersedes`.
9. Rapporter le résultat réel. Ne pas prétendre qu’un parser, MCP, CLI ou index SQLite a été exécuté.
