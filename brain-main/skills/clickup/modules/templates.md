# Duplication et adaptation — nouveau projet ClickUp

Tout le process de création d'un projet à partir de la template est ici. Les rôles d'espaces et la convention des listes restent dans `modules/convention.md`.

Préparer ≠ exécuter. Toute création ClickUp attend une approbation explicite (`AGENTS.md`).

Référence : dossier **Template** sous **Projets** (`1201110000005983`).  
Migration différée : **Modlab**, **FDLM 2027** — ne pas s'en servir comme modèle.

## Exemple concret Projets — à faire / à éviter

| | Faire | Ne pas faire |
| --- | --- | --- |
| Emplacement | Nouveau dossier sous **Projets** | Mon organisation, ou liste à la racine de Projets sans dossier |
| Base | Caler sur **Template** | Copier **Modlab**, **FDLM**, **Project Starter** ou **Shirel's** tels quels |
| Listes | Peu de listes à un mot : Inbox, Roadmap, Bugs (+ Phase ou champ Phase) | Listes `Phase 0 — …`, `Phase 1 — …` (Modlab, FDLM) |
| Structure | Une liste d'exécution + champ/vue Phase | Une liste par discipline (`Cadrage` / `Web` / `Test` comme Project Starter) |
| Docs | `docs/` + contrat / état projet | Projet quasi vide hors Inbox (Shirel's) |
| Statuts | Workflow opérationnel : à faire → en cours → bloquée → terminée | Statuts-phases web (découverte, brief, wireframes…) comme statut de tâche |
| Contenu | Dossier sans tâches étrangères + docs socle | Copier tâches, IDs ou docs métier d'un autre projet |
| Mapping | Nouveaux IDs dans `.clickup/mapping.yaml` | Réutiliser les IDs Template / Modlab / FDLM |
| Périmètre | Adapter nom, docs, éventuellement 1–2 listes justifiées | Ajouter Demandes / Lots / Changes « au cas où » |

Rappel observé :

- **Template** / **2nd Brain** — bons exemples de base.
- **Modlab** / **FDLM** — ancien modèle ; migration plus tard.
- **Project Starter** — autre convention.
- **Shirel's** — trop incomplet pour démarrer un agent.

IDs Template (inventaire seulement, jamais coller comme IDs du nouveau projet) : Inbox `1201110000007774`, Phase `1201110000007777`, Bugs `1201110000007775`, Roadmap `1201110000007776`, docs `1201110000005984`.

## Procédure

### 1. Cadrer

- Espace : **Projets** uniquement.
- Nom du dossier = nom du projet.
- Lire `AGENTS.md`, `brain/STATE.md`, `modules/convention.md`, et le contrat maître s'il existe dans Template `docs/`.
- Séparer générique (à copier) et spécifique (à adapter / laisser vide).

### 2. Inventaire Template

Noter listes, `docs/`, statuts, champs, vues, relations, docs socle.  
Ne pas prendre comme modèle : Phase N (Modlab/FDLM), Cadrage/Web/Test (Project Starter).

### 3. Plan d'adaptation (simulation)

Avant écriture :

1. Dossier cible sous Projets + nom
2. Listes à créer (noms exacts, un mot)
3. Docs socle vides de contenu métier
4. Statuts / champs prévus (exclure les phases web comme statut)
5. Ce qui reste absent volontairement
6. Entrées prévues pour `.clickup/mapping.yaml`

### 4. Faire approuver

Montrer le plan. Attendre l'accord sur cette opération exacte.

### 5. Créer

- Dossier sous Projets, listes et `docs/` selon le plan.
- Pas d'import de tâches d'un autre projet.
- Pas d'écriture Inbox sauf demande humaine explicite.

### 6. Adapter

- Docs socle pour **ce** projet seulement.
- Roadmap : jalons du projet, pas ceux d'un autre dossier.
- Bugs / Tasks : vides sauf seed demandé.

### 7. Remapper

Redécouvrir les **nouveaux** IDs. Mettre à jour `.clickup/mapping.yaml`.  
Ne jamais coller les IDs Template ci-dessus.

### 8. Rapport de conformité

| Contrôle | OK / écart |
| --- | --- |
| Sous Projets, pas Mon organisation | |
| Listes = plan (pas Phase 0/1…) | |
| docs/ + socle minimal | |
| Aucune tâche étrangère | |
| Statuts ≠ phases web si cible le prévoit | |
| Mapping local à jour | |
| Modlab/FDLM non utilisés comme source | |

Lister les écarts. Corriger ou faire arbitrer avant de déclarer le projet prêt pour les agents.
