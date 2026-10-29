---
name: cadrer
description: >-
  Mène le cadrage dans le chat en s'appuyant sur brain/ (STATE, OBJECTIVES,
  ROADMAP, PRINCIPLES, PROCESS, ARCHITECTURE, DECISIONS, TASKS). Met à jour
  ces fichiers ; s'arrête avant exécution code. À utiliser avec /cadrer.
disable-model-invocation: true
---

# /cadrer — Cadrage

## Objectif

Remplir ou reprendre le cadrage **dans `brain/`**. Pas d’installation de stack, pas de code applicatif, pas de pack `web-starter` par défaut.

## Mémoire canonique

| Fichier / zone | Rôle |
| --- | --- |
| `brain/STATE.md` | État maître |
| `brain/OBJECTIVES.md` | Vision / usagers / périmètre |
| `brain/ROADMAP.md` | Jalons |
| `brain/PRINCIPLES.md` | Non négociables + autorité |
| `brain/PROCESS.md` | Pipeline |
| `brain/ARCHITECTURE.md` | Zones et modes |
| `brain/GLOSSARY.md` | Vocabulaire |
| `brain/DECISIONS.md` | Décisions et questions (JSONL) |
| `brain/TASKS.md` | Tâches (JSONL) |
| `brain/registry/` | Autres kinds au besoin |
| `brain/inbox/` | Capture manuelle uniquement |

Les docs `docs/…` d’un pack web sont **optionnels**. Ils ne remplacent jamais `brain/STATE.md`.  
`OVERVIEW.md` n’est plus SoT (pointeur seulement).

## Dogfooding Second Brain

Quand le dépôt courant **est** Second Brain :

1. Lire le contexte utile déjà présent dans `brain/`.
2. Le cadrage porte sur **construire / faire évoluer `brain-main/`** en s’appuyant sur cette mémoire.
3. Toute proposition structurante touche `brain/` ; après accord, `/build` (organisation ou scaffold) ou `/faire` selon le cas.

## Lancement

1. Lire `AGENTS.md`, puis `STATE`, `OBJECTIVES`, `ROADMAP`, `PRINCIPLES`, `PROCESS`, `ARCHITECTURE`, `DECISIONS`, `TASKS` selon besoin.
2. **Reprise** : résumer en ≤5 lignes, signaler contradictions, poser les prochaines questions.
3. **Premier lancement** (mémoire quasi vide) : afficher le modèle de brief ci-dessous.
4. S’arrêter si aucune matière — ne pas inventer le produit.

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

1. Classer faits, hypothèses, idées, inconnues — rien de pertinent omis (idée → `registry/ideas` en `proposed`).
2. Mettre à jour **`brain/STATE.md`** (court, `patch`).
3. Proposer des patches ciblés :
   - vision / périmètre → `OBJECTIVES.md`
   - jalons → `ROADMAP.md`
   - process / principes → `PROCESS.md` / `PRINCIPLES.md`
   - zones → `ARCHITECTURE.md`
   - décision / question → `DECISIONS.md`
   - lot vérifiable → `TASKS.md` (ou idée `proposed` si encore flou)
4. Opérations : `append` / `patch` / `add_entry` / `supersede`.
5. Si le registre `proposed` grossit : proposer `/build` (organisation).
6. Sans réponse / « je ne sais pas » → hypothèse ouverte.

## Fin de phase cadrage

Quand un dossier de décision est prêt :

- le noter dans `STATE.md` ;
- suite typique : lots dans `TASKS` / registre → `/build` (organisation) → éventuellement `/faire` ;
- scaffold `/build` mode B seulement si install template/pack requise ;
- ne pas lancer exécution sans accord.

## Interdit

- Écrire dans `brain/inbox/` ou Inbox ClickUp.
- Installer des dépendances ou générer une app.
- Prendre `web-starter` comme mémoire par défaut.
- Créer un second fichier d’état concurrent à `brain/STATE.md`.
