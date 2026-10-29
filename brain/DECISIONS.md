# Décisions

Format d'entrée (D-006) : section `### {id} — {title}` + bloc YAML fenced `entry` + prose.

**Alias historiques :** `D-00x` → `DEC-00x`, `O-00x` → `OPEN-00x`. Les anciens préfixes restent des alias de lecture uniquement ; les nouveaux IDs sont canoniques.

## Settled

### DEC-001 — Séparer système commun et mémoire projet

```entry
id: DEC-001
kind: decision
status: settled
title: Séparer système commun et mémoire projet
summary: brain-main/ porte les règles communes ; brain/ porte la mémoire de ce dépôt.
created: 2026-10-29
updated: 2026-10-29
sources:
  - conversation
  - brain/ARCHITECTURE.md
relations: []
scope: system
```

`brain-main/` porte les règles communes. `brain/` porte la mémoire de ce dépôt. Un autre projet reçoit `templates/project/`, pas une copie de tout `brain-main/`.

Alias historique : `D-001`.

### DEC-002 — Fichiers canoniques

```entry
id: DEC-002
kind: decision
status: settled
title: Fichiers canoniques
summary: Les fichiers lisibles sont la source de vérité ; SQLite est un index reconstructible.
created: 2026-10-29
updated: 2026-10-29
sources:
  - conversation
relations: []
scope: system
```

Les fichiers lisibles sont la source de vérité. SQLite sera un index reconstructible.

Alias historique : `D-002`.

### DEC-003 — Validation humaine

```entry
id: DEC-003
kind: decision
status: settled
title: Validation humaine
summary: Une écriture durable proposée par un modèle attend une approbation humaine distincte.
created: 2026-10-29
updated: 2026-10-29
sources:
  - conversation
relations: []
scope: system
```

Une écriture durable proposée par un modèle attend une approbation humaine distincte. Le modèle ne s'approuve pas.

Alias historique : `D-003`.

### DEC-004 — Inbox manuelle

```entry
id: DEC-004
kind: decision
status: settled
title: Inbox manuelle
summary: Aucune automatisation n'écrit dans l'Inbox.
created: 2026-10-29
updated: 2026-10-29
sources:
  - conversation
relations: []
scope: system
```

Aucune automatisation n'écrit dans l'Inbox.

Alias historique : `D-004`.

### DEC-005 — Intégrations

```entry
id: DEC-005
kind: decision
status: settled
title: Intégrations
summary: Contrats communs dans brain-main/integrations/ ; .clickup/ et .notion/ sans secret ni MCP.
created: 2026-10-29
updated: 2026-10-29
sources:
  - conversation
  - brain-main/integrations/
relations: []
scope: system
```

Les contrats communs sont dans `brain-main/integrations/`. `.github/` est reconnu par GitHub. `.clickup/` et `.notion/` sont des conventions de correspondance, sans secret et sans connexion MCP.

Alias historique : `D-005`.

### DEC-006 — Modèle de données canonique et cycle de vie

```entry
id: DEC-006
kind: decision
status: settled
title: Modèle de données canonique et cycle de vie
summary: Registre Markdown en collections, IDs stables par kind, cycle de vie explicite ; clôture OPEN-001.
created: 2026-10-29
updated: 2026-10-29
sources:
  - conversation
  - plan O-001 (Build approuvé)
  - brain-main/conventions/taxonomy.yaml
  - brain-main/conventions/registry-schema.json
relations:
  - type: derived_from
    target_id: OPEN-001
scope: system
```

**Format canonique :** Markdown structuré, versionné dans Git. Pas de JSON atomique comme source de vérité. SQLite reste un index dérivé (DEC-002).

**Stockage :** fichiers **collection** (plusieurs entrées par fichier), pas un fichier par idée.

- décisions / questions ouvertes → `brain/DECISIONS.md`
- tâches → `brain/TASKS.md`
- état / architecture → synthèses non-atomiques (`brain/STATE.md`, `brain/ARCHITECTURE.md`)
- kinds sans foyer actuel (`fact`, `hypothesis`, `idea`, `issue`, `reference`) → un fichier collection sous `brain/registry/` (ex. `facts.md`), créé seulement au premier besoin réel

**Schéma d'entrée (requis) :** `id`, `kind`, `status`, `title`, `summary` (optionnel si le corps suffit), `created` / `updated`, `sources`, `relations` (`{ type, target_id }`). Optionnels : `scope`, `certainty`, `superseded_by`, champs opérationnels et mapping ClickUp (DEC-007).

**Forme Markdown :** `### {id} — {title}` + bloc YAML fenced `entry` + prose.

**Préfixes d'ID :** `FACT-`, `HYP-`, `IDEA-`, `OPEN-`, `DEC-`, `TASK-`, `ISSUE-`, `REF-`. Numérotation monotone par kind ; jamais réassigner un id retiré.

**Kinds adoptés :** `fact`, `hypothesis`, `idea`, `question`, `decision`, `task`, `issue`, `reference`. Hors registre : plans détaillés, notes de session, Inbox. `requirement` / `plan` / `insight` / `note` ne sont pas adoptés.

**Relations :** `supports`, `contradicts`, `supersedes`, `derived_from`, `implements`, `related_to`, `blocks`, `duplicate_of`.

**Cycle de vie :** `proposed` → `accepted` | `rejected` | `deferred` (validation humaine, DEC-003) ; puis selon le kind `active` / `blocked` / `resolved` / `settled` / `superseded`. Contrats : `taxonomy.yaml` et `registry-schema.json` (status `adopted`).

Alias historique : `D-006`. Clôture `OPEN-001` (alias `O-001`).

### DEC-007 — Local source de vérité ; ClickUp projection humaine

```entry
id: DEC-007
kind: decision
status: settled
title: Local source de vérité ; ClickUp projection humaine
summary: Le local porte toutes les infos (y compris tâches). Optimisé pour l'IA. ClickUp est la vue humaine ; le skill lit le local et pousse les mises à jour.
created: 2026-10-29
updated: 2026-10-29
sources:
  - conversation
  - brain-main/integrations/clickup.md
  - brain-main/skills/clickup/modules/sync.md
relations:
  - type: derived_from
    target_id: OPEN-002
  - type: related_to
    target_id: DEC-006
scope: system
```

**Rôles :**

- **Local (`brain/`, registre DEC-006)** : source de vérité de *tous* les champs, y compris tâches et issues. Rédigé pour être lu et mis à jour par une IA.
- **ClickUp** : surface humaine. L'humain suit et agit surtout ici. Ce n'est pas une seconde source canonique.
- **Skill ClickUp** : lit les entrées locales + `.clickup/mapping.yaml`, prépare puis (après approbation) crée/met à jour les tâches ClickUp pour coller au local.
- **Notion** : publication / miroir optionnel ; ne possède aucun champ du registre.
- **GitHub** : code et historique ; une issue GH n'est pas automatiquement une entrée locale.

**Tableau de propriété (tous les champs = local) :**

| Champ / contenu | Propriétaire | ClickUp (si mappé) | Notion |
| --- | --- | --- | --- |
| `id`, `kind`, relations, sources, certainty, scope | Local | Affichage / description si utile | Miroir optionnel |
| Titre, résumé, corps, critères d'acceptation | Local | Titre + description projetés | Miroir optionnel |
| `status` (cycle de vie registre) | Local | Statut opérationnel projeté selon mapping | — |
| Assignés, échéance, priorité, phase / jalon, liste cible | Local | Champs / listes projetés | — |
| Commentaires d'exécution durables à garder | Local (prose ou note dans l'entrée) | Fil ClickUp = bruit opérationnel, pas canon | — |
| Mapping `clickup.task_id` / `list_id` | Local (dans l'entrée ou `.clickup/`) | ID distant | — |
| Décisions / questions / faits / idées / refs | Local seul | Lien ou carte miroir seulement si décidé | Miroir optionnel |

**Flux :**

1. L'IA lit et propose des changements dans `brain/TASKS.md` (et autres collections).
2. Après validation humaine du local (DEC-003), le skill ClickUp lit ces entrées et propose le diff ClickUp.
3. Approbation explicite avant écriture ClickUp (sauf lot déjà autorisé).
4. L'humain voit l'état à jour dans ClickUp.
5. Si ClickUp a divergé (édition manuelle là-bas) : signaler le drift, proposer un patch *local* ou un re-push — **ne jamais écraser le local en silence** pour coller à ClickUp.

**Optimisation IA (local) :** chaque `task` / `issue` utilise le bloc `entry` DEC-006, plus les champs opérationnels optionnels du schéma (`assignees`, `due`, `priority`, `list`, `milestone`, `acceptance`, `clickup`). Pas de prose seule sans métadonnées si la tâche doit être poussée vers ClickUp.

**Sync :** direction principale **local → ClickUp**. Mode défaut `propose_only`. Pas de sync bidirectionnelle automatique. Détail : `brain-main/skills/clickup/modules/sync.md`.

Clôture `OPEN-002` (alias `O-002`).

### DEC-008 — Déploiement du template et mises à jour

```entry
id: DEC-008
kind: decision
status: settled
title: Déploiement du template et mises à jour
summary: Copie scaffold project-owned ; brain-main lié par référence ; sync_shared propose-only sans écraser le projet.
created: 2026-10-29
updated: 2026-10-29
sources:
  - conversation
  - brain-main/templates/README.md
  - DEC-001
relations:
  - type: derived_from
    target_id: OPEN-003
  - type: related_to
    target_id: DEC-001
scope: system
```

**Principe (DEC-001) :** un projet reçoit `templates/project/`, **pas** une copie de tout `brain-main/`.

**Trois politiques de fichier** (déclarées dans `brain-main/templates/project/template-manifest.yaml`) :

| Politique | Sens | Exemples |
| --- | --- | --- |
| `copy_once` | Copié à l'init ; ensuite **project-owned** — une mise à jour template ne l'écrase jamais | `brain/**`, `.clickup/mapping.yaml`, `.notion/mapping.yaml` |
| `sync_shared` | Peut être proposé en mise à jour depuis le template / `brain-main` si le fichier projet n'a pas divergé (ou si l'humain force) | stubs `AGENTS.md` d'entrée courts, règles Cursor génériques, README mapping |
| `link_only` | Jamais copié dans le projet ; l'agent lit via le chemin `brain-main` déclaré | `skills/`, `conventions/`, `integrations/`, `docs/`, `core/`, MCP, CLI |

**Lien `brain-main/` :** le projet déclare un chemin (fichier `.second-brain.yaml` : `brain_main_path`) — sibling, submodule, ou chemin absolu documenté. Pas de vendor complet. Sans chemin résolu : le dire et se limiter aux fichiers locaux du projet.

**Init d'un projet :**

1. Copier les chemins `copy_once` + `sync_shared` du manifeste.
2. Créer `.second-brain.yaml` avec `brain_main_path` et `template_version`.
3. Remplir `brain/STATE.md` pour *ce* projet ; laisser Inbox vide.
4. Renseigner `.clickup/` / `.notion/` (IDs propres — jamais ceux d'un autre projet).
5. Ne pas importer la mémoire (`DECISIONS`, `TASKS`, …) du dépôt Second Brain lui-même.

**Mise à jour contrôlée :**

1. Lire le manifeste + `.second-brain.yaml` du projet.
2. Pour chaque chemin `sync_shared` : comparer empreinte / contenu ; si inchangé côté projet → proposer remplacement ; si divergé → **ne pas écraser**, signaler le diff.
3. `copy_once` / fichiers absents du manifeste mais présents dans le projet : intouchables par la mise à jour auto.
4. Toujours mode `propose_only` + approbation humaine (DEC-003). Aucun script ne force sans accord.
5. Les skills/conventions évoluent dans `brain-main/` ; le projet en bénéficie via le lien, sans recopie.

**Hors décision :** implémentation du script CLI (reste non codée). Contrat = manifeste + cette DEC.

Clôture `OPEN-003` (alias `O-003`).

## Resolved

### OPEN-001 — Modèle de données

```entry
id: OPEN-001
kind: question
status: resolved
title: Modèle de données
summary: Tranché par DEC-006 — Markdown collection, IDs stables, cycle de vie explicite.
created: 2026-10-29
updated: 2026-10-29
sources:
  - conversation
  - brain/STATE.md
relations:
  - type: related_to
    target_id: DEC-006
scope: system
```

Markdown structuré ou JSON atomique, identifiants, relations, métadonnées, et cycle de vie d'une information. Tranché par DEC-006.

Alias historique : `O-001`.

### OPEN-002 — Synchronisation

```entry
id: OPEN-002
kind: question
status: resolved
title: Synchronisation
summary: Tranché par DEC-007 — local SoT complète ; ClickUp projection via skill ; pas de sync silencieuse.
created: 2026-10-29
updated: 2026-10-29
sources:
  - conversation
  - brain/STATE.md
relations:
  - type: related_to
    target_id: DEC-007
scope: system
```

Réconciliation local / ClickUp / Notion et propriété des champs. Tranché par DEC-007.

Alias historique : `O-002`.

### OPEN-003 — Déploiement du template

```entry
id: OPEN-003
kind: question
status: resolved
title: Déploiement du template
summary: Tranché par DEC-008 — copy_once / sync_shared / link_only ; brain-main par référence.
created: 2026-10-29
updated: 2026-10-29
sources:
  - conversation
  - brain/STATE.md
relations:
  - type: related_to
    target_id: DEC-008
scope: system
```

Ce qui est copié, ce qui reste lié à `brain-main/`, et comment une mise à jour préserve les personnalisations. Tranché par DEC-008.

Alias historique : `O-003`.
