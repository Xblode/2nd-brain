# Convention ClickUp — référence

Ce document définit la **convention générique** réutilisable.  
L’**inventaire observé** du workspace actuel est en annexe, clairement séparé : ses IDs ne doivent jamais être collés dans un nouveau projet.

Distinguer **convention** (règles stables), **observé** (lu dans un workspace) et **cible projet** (ce qui est réellement créé pour un dossier). Ne pas inventer d’identifiants.

Duplication / adaptation d’un nouveau projet : `modules/templates.md`.  
Sync local → ClickUp : `modules/sync.md`.

---

## 1. Structure des listes (contrat)

### Socle obligatoire

| Clé logique | Nom affiché typique | Rôle | Interdit |
| --- | --- | --- | --- |
| `LIST.INBOX` | Inbox | Capture humaine uniquement | Écriture IA / automatisée |
| `LIST.DOCS` | docs | Documents et contrat du projet dans ClickUp | Remplacer la mémoire locale versionnée |

La mémoire canonique (décisions, tâches, issues, état) reste dans les fichiers Git du projet. `docs` est la surface documentaire ClickUp, pas la SoT.

### Ajouts selon les besoins

| Clé logique | Nom affiché typique | Quand l’ajouter | Interdit |
| --- | --- | --- | --- |
| `LIST.TASKS` | Tasks | Suivi d’exécution utile dans ClickUp | Une liste par phase |
| `LIST.ROADMAP` | Roadmap | Jalons, résultats attendus, critères de réussite | Recopier les tâches opérationnelles |
| `LIST.BUGS` | Bugs | Problèmes / risques / blocages à suivre côté humain | Créer aussi une liste « Issues » |

**Nom retenu pour les problèmes :** `Bugs` (aligné sur la Template actuelle).  
Clé logique unique : `LIST.BUGS`. Les libellés « Issues », « Issues / Bugs » ou synonymes désignent **la même liste** — un agent ne doit pas les traiter comme trois listes distinctes.

### Non imposés

- **Decisions** — canon dans `brain/DECISIONS.md`. Une liste ClickUp miroir n’est ajoutée que si un besoin humain concret le justifie ; elle n’est pas dans le socle ni dans la cible par défaut.
- **Phases en listes séparées** — à éviter. Préférer un champ `Phase` / `milestone` et des vues filtrées. Des listes Phase N seulement après validation explicite du cadrage, jamais par défaut.
- **Batches / Lots** — pas de liste dédiée. Voir §3.

Noms affichés : un seul mot, sans préfixe numérique. Statut opérationnel ≠ phase.

---

## 2. Clés logiques (contrat agents)

Les agents raisonnent uniquement avec les clés `LIST.*`.  
`.clickup/mapping.yaml` associe chaque clé à l’ID ClickUp du **projet courant**.

Renommer une liste dans ClickUp ne change pas la clé logique.  
Changer de workspace / projet = nouveaux IDs dans le mapping, **jamais** ceux de la Template ni d’un autre dossier.

Clés reconnues :

- `LIST.INBOX`
- `LIST.DOCS`
- `LIST.TASKS`
- `LIST.ROADMAP`
- `LIST.BUGS`

Dans une entrée locale, le champ `list` utilise ces clés (ex. `LIST.TASKS`), pas le nom affiché ni l’ID brut.

---

## 3. Lots de travail (exceptionnels)

Le chat sert d’abord à réfléchir, repérer les angles morts et regrouper les demandes **avant** de lancer un agent codeur (`AGENTS.md` §4).

Un **lot** n’est créé (conceptuellement ou comme objet ClickUp) que s’il y a :

- plusieurs tâches réellement liées, **ou**
- une dépendance réelle, **ou**
- une validation humaine commune.

Pas de liste `Batches` / `Lots` « au cas où ». Pas d’objet supplémentaire pour chaque petite modification isolée.

---

## 4. Types et qualité

Types utiles : jalon, demande, tâche, lot (exceptionnel).  
Flux : idée → décision éventuelle (locale) → tâche. Relations plutôt que doublons.

Qualité d’une tâche destinée à ClickUp : titre actionnable, contexte, résultat + critères, statut opérationnel local, jalon si utile, dépendances, liens docs, clé `list` + mapping. Préférer tags/champs aux préfixes `[CORE]` dans le titre.

---

## 5. Statuts

Le **statut registre** local (`proposed`, `active`, `blocked`, `resolved`, …) est canonique.  
Le **statut ClickUp** est une projection : chaque projet déclare sa table dans `.clickup/mapping.yaml` (`status_map`).

Ne pas supposer que tous les projets partagent les mêmes statuts ClickUp.  
Si un statut local n’a pas de correspondance : **signaler l’écart**, ne pas choisir une valeur approximative.

Détail du protocole : `modules/sync.md`.

---

## Annexe A — Inventaire observé (workspace actuel)

> **Non portable.** Documentation de l’installation actuelle uniquement.  
> Les projets futurs reçoivent leurs propres IDs dans `.clickup/mapping.yaml`.

Workspace observé : `90151633729`.

### Espaces

| Espace | ID | Rôle |
| --- | --- | --- |
| **Mon organisation** | `90156746496` | Vrac, vie perso. Pas un projet livrable. |
| **Projets** | `90156746497` | Un dossier = un projet. Contient Template, Process, et les projets. |

Choisir l’espace d’abord. Jamais de tâche projet dans Mon organisation, ni de note perso dans un dossier de Projets.

### Mon organisation (observé)

Inbox, Agenda, Carnet, Laboratoire, Contenus, docs/Bibliothèque. Statuts typiques : aujourd’hui / prochainement. Agenda a son propre workflow.

### Projets (observé)

Liste racine : **Process**. Dossiers : Template, 2nd Brain, FDLM 2027, Modlab, Project Starter, Shirel's.

- **Template** / **2nd Brain** : Inbox, Bugs, Roadmap (+ Phase sur Template) — proches de la convention.
- **Modlab** / **FDLM** : listes par phase — migration plus tard ; ne pas copier.
- **Project Starter** : Cadrage / Web / Test — autre convention.
- **Shirel's** : surtout Inbox — trop incomplet comme modèle.

### Template actuelle (base observée)

`Projets / Template` (`1201110000005983`) :

| Clé logique | Nom affiché | ID (inventaire seulement) |
| --- | --- | --- |
| `LIST.INBOX` | Inbox | `1201110000007774` |
| *(hors contrat listes — champ/liste Phase)* | Phase | `1201110000007777` |
| `LIST.BUGS` | Bugs | `1201110000007775` |
| `LIST.ROADMAP` | Roadmap | `1201110000007776` |
| `LIST.DOCS` | docs/ | `1201110000005984` |

0 tâche à l’inspection. Doc : Registre de cadrage. Pas de custom fields détectés via l’API. Statuts d’espace = surtout phases web, pas un workflow opérationnel idéal.

Écarts connus vs convention cible : pas encore de `LIST.TASKS` sur la Template ; présence d’une liste Phase (à migrer idéalement vers un champ).
