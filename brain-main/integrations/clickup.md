# ClickUp

L'agent qui traite ClickUp est `brain-main/skills/clickup/SKILL.md`. Le charger avant une lecture ou une action. Il ne remplace pas ce contrat et ne crée pas la connexion.

ClickUp peut porter le suivi opérationnel. `brain/TASKS.md` reste le document local tant qu'une décision n'a pas désigné une autre source.

Le dossier `.clickup/` d'un projet décrit la correspondance : espaces, listes, champs, création, mise à jour, suppression, conflits. ClickUp ne lit pas ce dossier. La connexion se fait dans le client MCP, sans secret dans Git.

Démarrer en lecture ou en proposition. Ne pas créer, modifier, assigner ou supprimer une tâche sans approbation explicite. Ne pas effacer une tâche parce qu'une recherche locale est incomplète.

La façon de proposer, valider et réconcilier un changement venu de ClickUp n'est pas encore décidée.
