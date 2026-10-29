# Instructions des agents

1. Lire `brain/STATE.md`, puis `OBJECTIVES`, `ROADMAP`, `PRINCIPLES`, `PROCESS`, `ARCHITECTURE`, `GLOSSARY`, `DECISIONS`, `TASKS` selon le besoin.
2. Si `.second-brain.yaml` définit `brain_main_path`, l’utiliser pour skills, conventions et contrats (`link_only`, DEC-008). Sinon, le signaler et rester sur les fichiers locaux.
3. Pipeline : brainstorm → registre `proposed` → `/build` → local → `/clickup`.
4. En réflexion, ne pas lancer d’agent de code ; préférer `/cadrer` / `/note`.
5. Proposer toute modification durable et attendre une validation humaine.
6. Ne jamais écrire dans `brain/inbox/`.
7. SQLite, s’il existe, n’est qu’un index.
8. Local = SoT (DEC-007) ; ClickUp = projection.
9. Avant une action externe, expliquer l’action et obtenir une approbation.
10. Ne jamais enregistrer de secret dans le dépôt.
11. ClickUp : `/clickup` ou `{brain_main_path}/skills/clickup/SKILL.md` — convention `LIST.*` uniquement.
12. Commandes : `{brain_main_path}/skills/COMMANDS.md`. Pack web optionnel seulement.
