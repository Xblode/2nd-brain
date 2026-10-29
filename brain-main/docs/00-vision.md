# 00 — Vision

Les agents perdent le contexte entre les sessions, mélangent idées et décisions, et peuvent coder avant que le besoin soit cadré.

Second Brain est une mémoire locale, portable et inspectable. Le chat sert d’abord à réfléchir : questions, angles morts, contradictions. Les idées s’accumulent dans un registre (`proposed`). Une commande globale `/build` les organise en local après validation, puis projette vers ClickUp.

## Résultat attendu

- Reprendre un projet sans reconstituer tout l’historique.
- Distinguer fait, hypothèse, idée, question et décision.
- Garder la mémoire dans des fichiers lisibles (docs cadrage + registres).
- Traiter un volume d’idées sans les transformer automatiquement en tâches.

## Hors périmètre V1

- Écriture durable sans validation humaine.
- Base opaque à la place des fichiers (SQLite SoT).
- Un document Markdown par conversation.
- MCP / CLI / parser comme prérequis.

## Critère de réussite du squelette V1

Un nouvel agent identifie l’état, les objectifs, le process pipeline, et ce qui n’est pas encore décidé — via `brain/STATE.md` et les docs cadrage obligatoires.
