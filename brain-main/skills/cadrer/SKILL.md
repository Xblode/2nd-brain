---
name: cadrer
description: >-
  Mène le cadrage dans le chat en s'appuyant sur brain/ (STATE, OVERVIEW,
  ARCHITECTURE, DECISIONS, TASKS). Met à jour ces fichiers ; s'arrête avant
  /build. À utiliser avec /cadrer.
disable-model-invocation: true
---

# /cadrer — Cadrage

## Objectif

Remplir ou reprendre le cadrage **dans `brain/`**. Pas d’installation de stack, pas de code applicatif, pas de pack `web-starter` par défaut.

## Mémoire canonique (structure à utiliser)

Référence pratique : le dossier `brain/` de ce dépôt Second Brain (exemple de test / dogfooding).

| Fichier / zone | Rôle |
| --- | --- |
| `brain/STATE.md` | **État maître** — phase, focus, next_action, blockers, open_questions |
| `brain/OVERVIEW.md` | Vision / brief (finalité, usagers, périmètre, hors périmètre) |
| `brain/ARCHITECTURE.md` | Responsabilités et relations des zones |
| `brain/DECISIONS.md` | Décisions et questions (JSONL, DEC-006 / DEC-009) |
| `brain/TASKS.md` | Tâches (JSONL) |
| `brain/registry/` | Autres kinds, seulement au besoin |
| `brain/references/` | Pointeurs externes |
| `brain/inbox/` | Capture **manuelle uniquement** — jamais d’écriture IA |
| `brain/runtime/` | Index dérivé (hors cadrage) |

Les docs `docs/…` d’un pack web (ex. `templates/web-starter/`) sont **optionnels** et n’existent que si le projet a choisi un profil web via `/build`. Ils ne remplacent jamais `brain/STATE.md`.

## Dogfooding Second Brain

Quand le dépôt courant **est** Second Brain (`STATE` / `OVERVIEW` le décrivent) :

1. Lire d’abord tout le contexte utile déjà présent dans `brain/` (ne pas repartir d’un brief vide).
2. Le cadrage porte sur **construire / faire évoluer `brain-main/`** (skills, conventions, docs système, futurs runtime) en s’appuyant sur cette mémoire.
3. Ne pas demander un « produit client » générique sauf si l’utilisateur change explicitement de cible.
4. Toute proposition structurante touche `brain/` (mémoire) et, après accord + éventuel `/build` ou `/faire`, le code/docs sous `brain-main/`.

## Lancement

1. Lire `AGENTS.md`, puis dans l’ordre utile : `brain/STATE.md`, `brain/OVERVIEW.md`, `brain/ARCHITECTURE.md`, `brain/DECISIONS.md`, `brain/TASKS.md` (et `brain/README.md` si besoin de navigation).
2. **Reprise** : si `OVERVIEW` / `DECISIONS` / `STATE` ont déjà de la matière — résumer en ≤5 lignes, signaler contradictions, poser les prochaines questions. Ne pas réafficher tout le modèle de brief.
3. Si le dépôt a déjà du code ou un `brain-main/` substantiel : le décrire dans `STATE` / `ARCHITECTURE`, le préserver.
4. **Premier lancement** (mémoire quasi vide) : afficher le modèle de brief ci-dessous. « Je ne sais pas » est valide.
5. S’arrêter si le message de lancement ne contient pas encore de matière **et** que `brain/` n’a pas non plus de brief réutilisable — ne pas inventer le produit.

### Modèle de brief (premier lancement seulement)

```text
Produit / finalité : [pour qui, quel problème, en une ou deux phrases]
Réussi quand : [ce qu'on peut constater]
À faire maintenant : [2 à 5 capacités ou lots]
Plus tard : [ou "je ne sais pas"]
Pas dans ce projet : [ou "je ne sais pas"]
Parcours / usage principal : [qui fait quoi]
Contraintes : [date, langue, outils, ou "aucune"]
Données personnelles ou paiement : [oui / non / je ne sais pas]
Références : [ou "aucune"]
Je n'ai pas tranché : [points flous]
```

## Après chaque message

1. Classer faits, hypothèses, idées, inconnues — **rien de pertinent n’est omis** (idée → proposer `registry/ideas` ou note dans `STATE` / `DECISIONS`).
2. Mettre à jour **`brain/STATE.md`** (court, `patch`) : phase, focus, next_action, open_questions (≤5).
3. Proposer des patches **ciblés** seulement sur les fichiers `brain/` que le message remplit :
   - vision / périmètre → `OVERVIEW.md`
   - zones / relations → `ARCHITECTURE.md`
   - décision ou question → `DECISIONS.md` (`add_entry` ; appliquer après oui)
   - lot vérifiable → `TASKS.md`
4. Opérations : `append` / `patch` / `add_entry` / `supersede` — pas de remplacement silencieux de fichier entier.
5. Ne pas créer une usine `docs/` web ni de second fichier d’état.
6. Profil stack web : seulement si l’utilisateur vise un produit web ; rester `À VALIDER` jusqu’à `/build`.
7. Sans réponse / « je ne sais pas » → hypothèse notée comme ouverte, ne pas reposer.

## Fin de phase cadrage

Quand un **dossier de décision** est prêt (périmètre clair dans `OVERVIEW` + hypothèses listées + prochaine action dans `STATE`) :

- le noter dans `STATE.md` ;
- proposer la suite adaptée :
  - **Second Brain / système** → lots dans `TASKS.md` puis `/faire` (ou `/build` seulement si installation de template/pack est vraiment requise) ;
  - **projet web neuf** → `/build` (pack optionnel).
- Ne pas lancer `/build` ni `/faire` sans accord.

## Interdit

- Écrire dans `brain/inbox/` ou Inbox ClickUp.
- Installer des dépendances ou générer une app.
- Prendre `web-starter` ou `docs/01-product/…` comme mémoire par défaut.
- Utiliser une convention ClickUp autre que `skills/clickup/`.
- Créer un second fichier d’état concurrent à `brain/STATE.md`.
