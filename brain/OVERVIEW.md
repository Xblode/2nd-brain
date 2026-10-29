# Vision de ce projet

**Finalité :** mémoire de projet locale, lisible et contrôlée, pour passer du brainstorming à l'exécution sans perdre les idées ni les décisions — puis projeter le suivi vers ClickUp.

**Usagers :** humains et agents IA (Cursor, etc.) qui partagent les mêmes contrats.

**Périmètre actuel :** squelette documentaire + skills textuels ; dogfooding sur `brain/` pour valider l’architecture avant le runtime.

**Principes non négociables :** fichiers canoniques = source de vérité ; écriture durable = proposition puis approbation humaine ; Inbox manuelle ; mise à jour sans suppression silencieuse ; aucun secret dans Git ; SQLite dérivé seulement.

**Hors périmètre actuel (post-jalon 1) :** moteur exécutable (parser, index, MCP, CLI), sync automatique, pack web comme cœur du produit.

## Roadmap — Jalon 1 (en cours)

**Objectif :** pouvoir communiquer et conventionner le flux **Chatbot → infos en local (`brain/`) → mise à jour ClickUp**.

**Réussi quand :**

1. L’architecture de dossiers projet (`brain/` de ce dépôt) est **validée et testée** comme modèle.
2. Les skills **comprennent** un message, le **classent**, le **rangent** au bon endroit, **mettent à jour** les docs sans effacer l’existant.
3. On **ne perd plus** d’information ni d’idée entre le chat et le local (toute idée a une destination proposée).
4. Après le local, `/clickup` peut **projeter** le lot approuvé vers ClickUp (sans prendre ClickUp comme SoT).

**Pas dans le jalon 1 :** automatisation runtime complète, Notion comme SoT, multi-agents complexes, pack web obligatoire.
