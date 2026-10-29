# Instructions des agents

1. Lire `brain/STATE.md`, puis les documents concernés.
2. Si `.second-brain.yaml` définit `brain_main_path`, l'utiliser pour skills, conventions et contrats (`link_only`, DEC-008). Sinon, le signaler et rester sur les fichiers locaux.
3. En réflexion, ne pas lancer d'agent de code.
4. Proposer toute modification durable et attendre une validation humaine.
5. Ne jamais écrire dans `brain/inbox/`.
6. SQLite, s'il existe, n'est qu'un index.
7. Local = source de vérité des tâches et du registre (DEC-007) ; ClickUp = projection.
8. Avant une action externe, expliquer l'action et obtenir une approbation.
9. Ne jamais enregistrer de secret dans le dépôt.
10. `.clickup/` et `.notion/` décrivent des correspondances. Ils ne connectent pas les services.
11. Une demande ClickUp charge `{brain_main_path}/skills/clickup/SKILL.md` lorsque le chemin est résolu.
