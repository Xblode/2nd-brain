# Synchronisation local → ClickUp — conception (DEC-007)

Pas encore implémentée en code. Le skill applique la procédure à la main via les outils disponibles.

## Règle maître

Le **local** est la source de vérité de tous les champs (y compris tâches). ClickUp est une **projection** pour l’humain. Direction principale : **local → ClickUp**.

## Mode par défaut : `propose_only`

Tant que l’humain n’a pas approuvé **l’action externe précise**, le comportement est :

- lire local + mapping + ClickUp distant ;
- construire et présenter le diff ;
- **ne pas écrire** dans ClickUp.

`propose_only` reste le défaut dans `.clickup/mapping.yaml`. Passer en exécution n’autorise que le lot ou l’opération explicitement approuvée (`AGENTS.md`).

## Lecture obligatoire avant toute écriture ClickUp

1. `brain/TASKS.md` (et `brain/registry/*.md` si issues/faits liés)
2. Entrées `kind: task` / `issue` en JSONL (DEC-006 / DEC-009 + champs opérationnels)
3. `.clickup/mapping.yaml` (clés `LIST.*`, IDs, `status_map`, mode)
4. État ClickUp actuel des IDs mappés (si outil disponible)

Ne pas inventer de tâche ClickUp sans entrée locale correspondante (sauf Inbox humaine, hors IA).

## Mapping des listes

Le champ local `list` porte une clé logique (`LIST.TASKS`, `LIST.BUGS`, …).  
Résolution : clé → ID via `resources.lists` dans le mapping projet.  
Détail des clés : `modules/convention.md`.

## Mapping des statuts

Le statut **registre** local est canonique. Chaque projet définit `sync.status_map` :

```yaml
status_map:
  # local_status: clickup_status_name
  proposed: "à faire"
  accepted: "à faire"
  active: "en cours"
  blocked: "bloquée"
  resolved: "terminée"
  # deferred / rejected / superseded : à renseigner ou laisser non mappés
```

Règles :

- La table est **par projet** ; ne pas supposer les mêmes libellés partout.
- Statut local sans entrée dans `status_map` → **signaler l’écart**, ne pas approximer.
- Statut ClickUp inconnu au retour de lecture → drift à signaler, pas d’import silencieux comme canon.

## Contrat `last_pushed`

Après chaque push réussi d’une entrée, enregistrer un instantané minimal utilisé pour détecter les modifications concurrentes.

### Où le conserver

1. **Par entrée (obligatoire si mappée)** — dans le bloc local `clickup` :

   ```yaml
   clickup:
     task_id: "..."
     list_id: "..."   # ID résolu au moment du push
     last_pushed: "2026-10-29T12:00:00Z"
     last_pushed_hash: "..."   # optionnel : empreinte des champs projetés
   ```

2. **Journal de sync (recommandé quand le runtime existera)** — append-only sous `.clickup/sync-log.md` (ou `.clickup/sync-log.jsonl`). Pas encore automatisé ; le skill peut noter à la main si utile.

### Contenu utile de `last_pushed`

| Élément | Rôle |
| --- | --- |
| Horodatage ISO du push réussi | Comparer « depuis quand » |
| `task_id` / `list_id` | Identité distante stable |
| Empreinte optionnelle des champs poussés (titre, statut mappé, due, priority, assignees) | Détecter si le distant a bougé hors sync |

### Utilisation à la comparaison (3 voies)

Comparer **local actuel**, **ClickUp distant**, **dernier état poussé** (`last_pushed` + empreinte si présente) :

| Situation | Action |
| --- | --- |
| Local changé, distant aligné avec last_pushed | Proposer push local → ClickUp |
| Distant changé, local inchangé depuis last_pushed | Proposer import en proposition locale (humain tranche) |
| Local et distant changés tous les deux | Présenter les deux ; revue manuelle ; local reste SoT jusqu’à décision |
| Champ absent du mapping / statut non mappé | Ne pas inventer ; rester en lecture / proposition |
| Pas de `last_pushed` (premier push) | Traiter comme création ou liaison initiale ; prudence anti-doublon |

Aucune résolution automatique qui ferait de ClickUp la source d’un champ.

## Protocole

1. Construire le payload ClickUp **depuis** l'objet JSONL local (titre, description, statut via `status_map`, assignés, échéance, priorité, liste via clé `LIST.*`).
2. Rapport de prévisualisation : crée / met à jour / ignore, champ par champ.
3. Comparer local, distant, last_pushed (§ ci-dessus).
4. Drift distant : signaler ; proposer patch local **ou** re-push local — ne pas écraser le local en silence.
5. Approbation humaine de l’action ClickUp (DEC-003 / `AGENTS.md`).
6. Exécuter seulement l’approuvé ; vérifier en relisant l’objet distant ; reporter succès / ignoré / échec.
7. Mettre à jour `clickup.task_id`, `list_id`, `last_pushed` (et journal si utilisé) après succès.

## Idempotence et suppressions

- Clé stable : `id` local ↔ `clickup.task_id`.
- Une reprise ne crée pas de doublon si l’ID distant est connu.
- Pas de suppression ClickUp si l’identité est incertaine.
- Pas de suppression locale parce qu’une recherche ClickUp est incomplète.

## Journal de synchronisation (cible runtime)

Quand un runtime existera, chaque tentative (même en `propose_only`) pourra consigner :

- horodatage, mode (`propose_only` / exécution), entrée locale `id`, clé `LIST.*`, action proposée, résultat, message d’écart statut éventuel.

Emplacement prévu : `.clickup/sync-log.md` (lisible) ou `.clickup/sync-log.jsonl` (machine).  
Hors scope tant que le squelette documentaire n’a pas de script — la procédure manuelle du skill suffit.
