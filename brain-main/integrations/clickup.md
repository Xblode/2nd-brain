# ClickUp

L'agent qui traite ClickUp est `brain-main/skills/clickup/SKILL.md`. Le charger avant une lecture ou une action. Il ne remplace pas ce contrat et ne crée pas la connexion.

## Rôle (DEC-007)

- **Local** (`brain/TASKS.md` et registre) : source de vérité de toutes les informations, y compris tâches — format optimisé pour l'IA.
- **ClickUp** : vue opérationnelle pour l'humain. Le skill lit le local et propose les mises à jour ClickUp.
- Direction : **local → ClickUp**. Pas de sync silencieuse. Pas de ClickUp comme SoT d'un champ.

`brain/TASKS.md` reste le document canonique des tâches. ClickUp n'y substitue pas.

Espaces du workspace (observés) :

- **Mon organisation** : vrac, vie perso, notes générales.
- **Projets** : un dossier par projet, plus le dossier **Template** (base) et la liste **Process**.

La topologie détaillée est dans `brain-main/skills/clickup/modules/convention.md`. La sync conception : `modules/sync.md`.

Le dossier `.clickup/` décrit la correspondance : espaces, listes, mapping d'IDs, mode `propose_only`. ClickUp ne lit pas ce dossier. Connexion = client MCP, sans secret dans Git.

Démarrer en lecture ou en proposition. Ne pas créer, modifier, assigner ou supprimer une tâche ClickUp sans approbation explicite, et sans entrée locale quand l'IA initie le travail. Ne pas effacer une tâche parce qu'une recherche locale ou distante est incomplète.
