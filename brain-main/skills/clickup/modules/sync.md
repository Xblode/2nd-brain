# Synchronisation local → ClickUp — conception (DEC-007)

Pas encore implémentée en code. Le skill applique la procédure à la main via les outils disponibles.

## Règle maître

Le **local** est la source de vérité de tous les champs (y compris tâches). ClickUp est une **projection** pour l'humain. Direction principale : **local → ClickUp**.

## Lecture obligatoire avant toute écriture ClickUp

1. `brain/TASKS.md` (et `brain/registry/*.md` si issues/faits liés)
2. Entrées `kind: task` / `issue` au format `entry` (DEC-006 + champs opérationnels)
3. `.clickup/mapping.yaml` (listes, espace, mode)
4. État ClickUp actuel des IDs mappés (si outil disponible)

Ne pas inventer de tâche ClickUp sans entrée locale correspondante (sauf Inbox humaine, hors IA).

## Protocole

1. Construire le payload ClickUp **depuis** le bloc `entry` local (titre, description, statut mappé, assignés, échéance, priorité, liste).
2. Rapport de prévisualisation : crée / met à jour / ignore, champ par champ.
3. Comparer : local, ClickUp distant, dernier `clickup.last_pushed` connu.
4. Drift distant (ClickUp modifié sans local) : signaler ; proposer patch local **ou** re-push local — ne pas écraser le local en silence.
5. Approbation humaine de l'action ClickUp (DEC-003 / AGENTS.md).
6. Exécuter seulement l'approuvé ; vérifier ; reporter succès / ignoré / échec.
7. Mettre à jour le mapping (`clickup.task_id`, `last_pushed`) dans l'entrée ou `.clickup/` après succès.

## Idempotence et suppressions

- Clé stable : `id` local ↔ `clickup.task_id`.
- Une reprise ne crée pas de doublon si l'ID distant est connu.
- Pas de suppression ClickUp si l'identité est incertaine.
- Pas de suppression locale parce qu'une recherche ClickUp est incomplète.

## Conflits

| Situation | Action |
| --- | --- |
| Local changé, ClickUp inchangé depuis last_pushed | Proposer push local → ClickUp |
| ClickUp changé, local inchangé | Proposer import en proposition locale (humain tranche) |
| Les deux changés | Présenter les deux ; revue manuelle ; local reste SoT jusqu'à décision |
| Champ absent du mapping | Ne pas inventer ; rester en lecture / proposition |

Aucune résolution automatique qui ferait de ClickUp la source d'un champ.
