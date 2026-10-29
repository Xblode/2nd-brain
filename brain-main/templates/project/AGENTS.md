# Instructions des agents

1. Lire `brain/STATE.md`, puis `OVERVIEW`, `ARCHITECTURE`, `DECISIONS`, `TASKS` selon le besoin.
2. Si `.second-brain.yaml` définit `brain_main_path`, l'utiliser pour skills, conventions et contrats (`link_only`, DEC-008). Sinon, le signaler et rester sur les fichiers locaux.
3. En réflexion, ne pas lancer d'agent de code ; préférer `/cadrer` pour clarifier.
4. Proposer toute modification durable et attendre une validation humaine.
5. Ne jamais écrire dans `brain/inbox/`.
6. SQLite, s'il existe, n'est qu'un index.
7. Local = source de vérité des tâches et du registre (DEC-007) ; ClickUp = projection.
8. Avant une action externe, expliquer l'action et obtenir une approbation.
9. Ne jamais enregistrer de secret dans le dépôt.
10. `.clickup/` et `.notion/` décrivent des correspondances. Ils ne connectent pas les services.
11. Une demande ClickUp : `/clickup` ou `{brain_main_path}/skills/clickup/SKILL.md`. Convention Second Brain (`LIST.*`) uniquement.
12. Commandes : `{brain_main_path}/skills/COMMANDS.md`. Mémoire = structure `brain/` ; pack web optionnel seulement.
