# Processus — pipeline Second Brain

Comment traiter une idée ou une fonctionnalité de bout en bout.

## Pipeline

```text
Prompt
  → Brainstorming (agents / skills / /note)
  → Résultats stockés dans le registre (status: proposed)
  → /build (organisation globale)
       → analyser + trier
       → valider les choix structurants avec l’humain
       → organiser en local (tâches, décisions, docs cadrage)
       → projeter ClickUp (/clickup) sur le lot local validé
```

## 1. Brainstorming / capture

- Clarifier le besoin ; ne pas lancer d’agent de code par défaut.
- Accumuler des entrées registre en `proposed` (idées, hypothèses, questions, faits candidats).
- Mise à jour régulière autorisée ; **ne pas** promouvoir automatiquement en tâches.
- Outils typiques : `/note`, skill second-brain (module brainstorming), agents en réflexion.
- Relire `OBJECTIVES.md` et `ROADMAP.md` pour filtrer hors périmètre.

## 2. Stockage registre

- Collections versionnées (DEC-006 / DEC-009) : `DECISIONS.md`, `TASKS.md`, `registry/*`.
- Contrats : `taxonomy.yaml`, `registry-schema.json`.
- Opérations : `append`, `patch`, `add_entry`, `supersede` — jamais remplacer un fichier entier sans accord.

## 3. `/build` — organisation globale

Mode principal (DEC-011) :

1. Lire `STATE.md`, registres pending (`proposed` / à trier), docs cadrage.
2. Analyser : doublons, contradictions, alignement objectifs/roadmap.
3. Proposer un plan de tri par entrée ou groupe : garder, fusionner, promouvoir tâche, promouvoir décision, patcher un doc cadrage, différer, rejeter.
4. **Validation humaine sélective** : lot global pour le triage évident ; questions explicites pour conflits, priorités, suppressions de sens, création/modification de docs cadrage.
5. Appliquer uniquement l’approuvé en local.
6. Proposer ensuite le lot ClickUp (`/clickup`) — local d’abord, projection ensuite.

Sous-mode scaffold : construction template / dogfood `brain-main` (ancien `/build`) — seulement si l’utilisateur demande explicitement un scaffold ou un lot de construction système.

## 4. Exécution code

- `/faire` (ou équivalent) sur un **lot déjà approuvé** avec critères d’acceptation.
- Hors réflexion : pas de multi-agents pour chaque message.

## 5. Consolidation

- Mettre à jour `STATE.md` et les docs cadrage concernés.
- Décisions confirmées seulement dans le registre décisions.
- Déclarer terminé seulement avec preuves (`/done`).

## Références

- Principes et autorité : `PRINCIPLES.md`
- Vocabulaire : `GLOSSARY.md`
- Skills : `brain-main/skills/COMMANDS.md`
