# Duplication et adaptation — nouveau projet ClickUp

Tout le process de création d’un projet à partir de la template est ici. Les rôles d’espaces et la convention des listes restent dans `modules/convention.md`.

Préparer ≠ exécuter. Toute création ClickUp attend une approbation explicite (`AGENTS.md`).

Référence structurelle : dossier **Template** sous **Projets**.  
Les IDs numériques de ce dossier sont un **inventaire observé** uniquement — jamais collés comme IDs du nouveau projet (voir annexe de `convention.md`).

Migration différée : **Modlab**, **FDLM 2027** — ne pas s’en servir comme modèle.

## Contrat maître de la Template

Ordre de lecture obligatoire pour inventaire et duplication :

1. **Description du dossier parent Template** — contrat de référence du système ClickUp (intentions, règles communes, structure attendue). Point d’entrée de l’inventaire.
2. **Descriptions des listes** — rôles, interdits, champs attendus par liste.
3. **Statuts et champs** de chaque liste / de l’espace — workflow opérationnel réel.
4. **Documents associés** sous `docs/` (et pages liées) — socle documentaire ClickUp.
5. **Vues et relations** si présentes.

Ensuite :

- Les **règles communes** stables (socle Inbox + docs, clés `LIST.*`, Inbox sans écriture IA, Roadmap = jalons seulement, etc.) sont enregistrées dans ce dépôt (`convention.md`, ce fichier, `sync.md`).
- Les **identifiants et particularités** du workspace / du projet vont uniquement dans `.clickup/mapping.yaml` du projet.

Si une description de liste contredit le contrat parent, signaler l’écart et faire arbitrer — ne pas inventer une troisième règle.

## Exemple concret Projets — à faire / à éviter

| | Faire | Ne pas faire |
| --- | --- | --- |
| Emplacement | Nouveau dossier sous **Projets** | Mon organisation, ou liste à la racine de Projets sans dossier |
| Base | Caler sur **Template** + contrat parent | Copier **Modlab**, **FDLM**, **Project Starter** ou **Shirel's** tels quels |
| Socle | `LIST.INBOX` + `LIST.DOCS` | Omettre Inbox ou docs |
| Exécution | Ajouter `LIST.TASKS` si suivi ClickUp utile | Imposer Tasks / Decisions / Issues à tous les projets |
| Problèmes | Une seule liste `Bugs` (`LIST.BUGS`) | Créer Bugs **et** Issues |
| Roadmap | Optionnelle ; jalons + critères seulement | Recopier les tâches dedans |
| Phases | Champ / vues filtrées | Listes `Phase 0 — …`, `Phase 1 — …` (Modlab, FDLM) |
| Décisions | Canon local `brain/DECISIONS.md` | Liste Decisions obligatoire « au cas où » |
| Lots | Exceptionnels (dépendances / validation commune) | Liste Batches pour chaque petite modif |
| Statuts | Workflow opérationnel mappé dans `status_map` | Statuts-phases web comme statut de tâche |
| Contenu | Dossier sans tâches étrangères + docs socle | Copier tâches, IDs ou docs métier d’un autre projet |
| Mapping | Nouveaux IDs sous clés `LIST.*` | Réutiliser les IDs Template / Modlab / FDLM |
| Périmètre | Adapter nom, docs, 1–2 listes justifiées | Ajouter Demandes / Lots / Changes « au cas où » |

Rappel observé :

- **Template** / **2nd Brain** — bons exemples de base.
- **Modlab** / **FDLM** — ancien modèle ; migration plus tard.
- **Project Starter** — autre convention.
- **Shirel's** — trop incomplet pour démarrer un agent.

## Procédure

### 1. Cadrer

- Espace : **Projets** uniquement.
- Nom du dossier = nom du projet.
- Lire `AGENTS.md`, `brain/STATE.md`, `modules/convention.md`.
- Lire le **contrat maître** (description parent Template), puis listes / docs.
- Séparer générique (à copier) et spécifique (à adapter / laisser vide).

### 2. Inventaire Template

Suivre l’ordre du contrat maître (§ ci-dessus).  
Noter listes → clés `LIST.*`, `docs/`, statuts, champs, vues, relations, docs socle.  
Ne pas prendre comme modèle : Phase N (Modlab/FDLM), Cadrage/Web/Test (Project Starter).

### 3. Plan d’adaptation (simulation)

Avant écriture :

1. Dossier cible sous Projets + nom
2. Socle : Inbox + docs ; ajouts optionnels justifiés (`Tasks`, `Roadmap`, `Bugs`)
3. Docs socle vides de contenu métier
4. Statuts / champs prévus + esquisse de `status_map` (exclure les phases web comme statut)
5. Ce qui reste absent volontairement (pas de Decisions / Batches par défaut)
6. Entrées prévues pour `.clickup/mapping.yaml` (clés `LIST.*` → IDs à redécouvrir après création)

### 4. Faire approuver

Montrer le plan. Attendre l’accord sur cette opération exacte.

### 5. Créer

- Dossier sous Projets, listes et `docs/` selon le plan.
- Pas d’import de tâches d’un autre projet.
- Pas d’écriture Inbox sauf demande humaine explicite.

### 6. Adapter

- Docs socle pour **ce** projet seulement.
- Roadmap : jalons du projet, pas ceux d’un autre dossier.
- Bugs / Tasks : vides sauf seed demandé.

### 7. Remapper

Redécouvrir les **nouveaux** IDs. Mettre à jour `.clickup/mapping.yaml` sous les clés `LIST.*` + `status_map`.  
Ne jamais coller les IDs Template de l’annexe `convention.md`.

### 8. Rapport de conformité

| Contrôle | OK / écart |
| --- | --- |
| Sous Projets, pas Mon organisation | |
| Socle Inbox + docs présents | |
| Listes = plan (pas Phase 0/1… ; pas Bugs+Issues) | |
| Pas de liste Decisions / Batches sauf justification | |
| docs/ + socle minimal | |
| Aucune tâche étrangère | |
| Statuts ≠ phases web si cible le prévoit ; `status_map` ébauché | |
| Mapping local à jour (clés `LIST.*`, IDs propres) | |
| Modlab/FDLM non utilisés comme source | |
| Contrat parent Template lu et écarts listés | |

Lister les écarts. Corriger ou faire arbitrer avant de déclarer le projet prêt pour les agents.
