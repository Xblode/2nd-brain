# Convention ClickUp — référence

Distinguer **observé** (lu dans le workspace) et **cible** (pas encore uniforme). Ne pas inventer d'identifiants.

Workspace : `90151633729`.

Duplication / adaptation d'un nouveau projet : voir uniquement `modules/templates.md`.

## Espaces

| Espace | ID | Rôle |
| --- | --- | --- |
| **Mon organisation** | `90156746496` | Vrac, vie perso. Pas un projet livrable. |
| **Projets** | `90156746497` | Un dossier = un projet. Contient `Template`, `Process`, et les projets. |

Choisir l'espace d'abord. Jamais de tâche projet dans Mon organisation, ni de note perso dans un dossier de Projets.

## Mon organisation (observé)

Inbox, Agenda, Carnet, Laboratoire, Contenus, docs/Bibliothèque. Statuts typiques : aujourd'hui / prochainement. Agenda a son propre workflow.

## Projets (observé)

Liste racine : **Process**. Dossiers : Template, 2nd Brain, FDLM 2027, Modlab, Project Starter, Shirel's.

- **Template** / **2nd Brain** : Inbox, Bugs, Roadmap (+ Phase sur Template).
- **Modlab** / **FDLM** : encore des listes par phase — migration plus tard.
- **Project Starter** : Cadrage / Web / Test.
- **Shirel's** : surtout Inbox.

## Template actuelle (base)

`Projets / Template` (`1201110000005983`) :

| Élément | ID |
| --- | --- |
| Inbox | `1201110000007774` |
| Phase | `1201110000007777` |
| Bugs | `1201110000007775` |
| Roadmap | `1201110000007776` |
| docs/ | `1201110000005984` |

0 tâche à l'inspection. Doc : Registre de cadrage. Pas de custom fields détectés via l'API. Statuts d'espace = surtout phases web, pas un workflow opérationnel.

## Cible listes projet (proposition)

| Liste | Rôle | Interdit |
| --- | --- | --- |
| Inbox | Capture manuelle | Écriture IA (règle dépôt actuelle) |
| Roadmap | Jalons + critères | Dupliquer les tâches |
| Tasks | Actions concrètes | Une liste par phase |
| Decisions | Choix structurants | — |
| Issues / Bugs | Problèmes / risques | — |

Optionnel si besoin démontré : Demandes, Lots. Noms : un mot, sans préfixe numérique. Statut ≠ phase.

## Types et qualité

Types : jalon, demande, tâche, lot (optionnel), statut ≠ phase.  
Flux : idée → décision éventuelle → tâche. Relations plutôt que doublons.

Qualité tâche : titre actionnable, contexte, résultat + critères, statut opérationnel, jalon si utile, dépendances, liens docs, clé de mapping si prévue. Préférer tags/champs aux préfixes `[CORE]` dans le titre à long terme.
