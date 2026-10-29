# ClickUp

L'agent qui traite ClickUp est `brain-main/skills/clickup/SKILL.md`. Le charger avant une lecture ou une action. Il ne remplace pas ce contrat et ne crée pas la connexion.

## Rôle (DEC-007)

- **Local** (`brain/TASKS.md` et registre) : source de vérité de toutes les informations, y compris tâches — format optimisé pour l'IA.
- **ClickUp** : vue opérationnelle pour l'humain. Le skill lit le local et propose les mises à jour ClickUp.
- Direction : **local → ClickUp**. Pas de sync silencieuse. Pas de ClickUp comme SoT d'un champ.

`brain/TASKS.md` reste le document canonique des tâches. ClickUp n'y substitue pas.

## Structure (aperçu)

Socle : Inbox + docs. Options selon besoin : Tasks, Roadmap, Bugs (`LIST.BUGS` — pas une seconde liste « Issues »).  
Décisions et mémoire riche : fichiers locaux. Clés logiques et détails : `brain-main/skills/clickup/modules/convention.md`.

Espaces (rôles génériques) :

- **Mon organisation** : vrac, vie perso, notes générales.
- **Projets** : un dossier par projet, plus le dossier **Template** (base) et la liste **Process**.

Les IDs concrets d’un workspace appartiennent à l’inventaire / au mapping projet, pas à ce contrat commun.

La topologie détaillée : `modules/convention.md`. Sync : `modules/sync.md`. Duplication : `modules/templates.md`.

Le dossier `.clickup/` décrit la correspondance : clés `LIST.*`, IDs, `status_map`, mode `propose_only`. ClickUp ne lit pas ce dossier. Connexion = client MCP, sans secret dans Git.

Démarrer en lecture ou en proposition. Ne pas créer, modifier, assigner ou supprimer une tâche ClickUp sans approbation explicite, et sans entrée locale quand l'IA initie le travail. Ne pas effacer une tâche parce qu'une recherche locale ou distante est incomplète.
