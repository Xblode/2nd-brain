# AGENTS.md — Instructions communes du dépôt Second Brain

Ce fichier définit les règles durables applicables aux agents qui travaillent dans ce dépôt, quel que soit l'outil utilisé. Il constitue la base commune ; les fichiers propres à Cursor, Claude Code ou GitHub Copilot ne doivent ajouter que des adaptations nécessaires à leur outil.

## 1. Avant de commencer

1. Pour tout travail substantiel, lire `brain/STATE.md` afin de connaître l'état réel du projet.
2. Lire ensuite uniquement les documents pertinents :
   - `README.md` pour l'entrée du dépôt ;
   - `brain/OVERVIEW.md`, `brain/ARCHITECTURE.md`, `brain/DECISIONS.md` et `brain/TASKS.md` selon le besoin ;
   - les documents concernés de `brain-main/docs/`, `brain-main/conventions/`, `brain-main/integrations/` ou `brain-main/skills/second-brain/` ;
   - `brain-main/skills/clickup/SKILL.md` dès que la demande concerne ClickUp.
3. Examiner les fichiers, l'historique et l'état Git concernés avant de modifier quoi que ce soit. Ne pas écraser ni supprimer des changements utilisateur sans autorisation explicite.
4. Distinguer ce qui est réellement implémenté, ce qui est documenté, ce qui est proposé et ce qui reste à décider. La présence d'un dossier ou d'un README ne prouve pas qu'un composant fonctionne.

## 2. Source de vérité et rôle des dossiers

- `brain-main/` contient le système commun : conventions, documentation, contrats, modules et modèles réutilisables. Ne pas en recopier l'intégralité dans les projets clients.
- `brain/` contient la mémoire du dépôt Second Brain lui-même : son état, ses décisions, son architecture et ses tâches.
- `brain-main/templates/project/` est le modèle destiné aux futurs projets. Ses fichiers doivent rester génériques et ne pas contenir les données propres à ce dépôt.
- `AGENTS.md` est la base d'instructions commune. `CLAUDE.md`, `.github/copilot-instructions.md` et les règles Cursor doivent rester courtes, compatibles et ne pas redéfinir en parallèle les mêmes règles.
- Les fichiers canoniques sont la référence pour les connaissances et décisions durables. Une base SQLite éventuelle est un index dérivé et reconstructible, pas l'unique source de données.
- Ne pas créer automatiquement un fichier par idée, message, conversation ou session. Rechercher les documents existants et mettre à jour la bonne source canonique quand cela est autorisé.

## 3. État du projet et décisions ouvertes

Second Brain est actuellement traité comme un squelette documentaire et architectural. Ne présenter ni le registre, ni la recherche, ni l'index, ni la CLI, ni le serveur MCP, ni les scripts de déploiement comme implémentés sans vérifier le code et les validations correspondantes.

Ne pas trancher silencieusement les sujets explicitement ouverts dans `brain/STATE.md` ou `brain/DECISIONS.md`, notamment :

- le format du registre canonique, ses identifiants et ses relations ;
- le cycle de vie d'une information et les transitions de statut ;
- la réconciliation et la synchronisation entre le stockage local, ClickUp et Notion ;
- la façon de déployer et mettre à jour les templates sans écraser les personnalisations.

Quand une décision est nécessaire, présenter les options, compromis, risques et recommandation. Enregistrer une décision uniquement lorsqu'elle est confirmée par un humain.

## 4. Mode de travail : réflexion d'abord, exécution ensuite

- Par défaut, commencer par comprendre l'objectif, le contexte, les contraintes et les angles morts. Ne pas transformer automatiquement chaque idée en tâche de code.
- Si la demande relève du brainstorming, rester en mode réflexion : analyser, poser les questions réellement bloquantes et regrouper les changements potentiels. Ne pas lancer d'agent de code ni modifier les fichiers sans demande explicite de passer à l'exécution.
- Avant un lot de modifications, définir son objectif, son périmètre, ses dépendances et ses critères d'acceptation. Regrouper les changements liés plutôt que lancer plusieurs agents pour des retouches isolées.
- N'utiliser plusieurs agents que lorsque les sous-tâches sont réellement indépendantes et que le bénéfice dépasse le coût de coordination.
- Une validation humaine ne peut pas être remplacée par l'auto-approbation d'un agent ou d'un modèle.
- Une autorisation explicite portant sur un lot permet d'exécuter ce lot dans le périmètre convenu ; elle n'autorise pas des suppressions, publications ou actions externes sans rapport avec celui-ci.

## 5. Mémoire et écritures durables

- Ne jamais écrire, déplacer, renommer ou supprimer de contenu dans `brain/inbox/` ou dans l'Inbox d'un autre projet via une IA ou un outil automatisé. L'Inbox est une zone de capture manuelle.
- Une modification du contenu canonique de mémoire doit d'abord être présentée comme une proposition et attendre l'approbation humaine avant application.
- Préserver la provenance, le statut et le niveau de certitude des informations. Distinguer faits vérifiés, hypothèses, idées, décisions et questions ouvertes.
- Ne pas effacer silencieusement une contradiction. La signaler et proposer une réconciliation.
- Ne pas réindexer, générer ou synchroniser une donnée dérivée avant de connaître sa source canonique et les règles de reconstruction prévues.

## 6. Intégrations et sécurité

- Les contrats communs des services et outils sont documentés dans `brain-main/integrations/` ; les correspondances propres à un projet résident dans sa configuration locale prévue à cet effet.
- `.clickup/` et `.notion/` sont des conventions de documentation et de mapping. Leur présence ne configure ni n'authentifie un serveur MCP.
- Toute demande ClickUp passe par `brain-main/skills/clickup/SKILL.md`. Cette skill n'établit pas la connexion : elle dit comment l'utiliser si l'outil est réellement disponible.
- Avant une action externe affectant GitHub, ClickUp, Notion ou une autre plateforme, préciser l'opération, la cible et ses effets, puis demander une approbation explicite, sauf si cette opération exacte a déjà été autorisée.
- Ne jamais ajouter de jeton, clé API, mot de passe, cookie, fichier d'authentification ou secret à Git, aux logs ou aux exemples. Utiliser la configuration sécurisée prévue par l'outil.
- Respecter le principe du moindre privilège. Ne pas créer de mécanisme d'écriture ou d'exécution arbitraire lorsqu'une opération spécifique suffit.
- Ne jamais lancer une réinstallation destructive ou une suppression massive sans annoncer précisément le périmètre, prévoir une sauvegarde vérifiable et obtenir une confirmation explicite.

## 7. Modifications techniques et validation

- Inspecter les conventions et fichiers existants avant d'ajouter une nouvelle structure, dépendance, abstraction ou fichier de règles.
- Privilégier des changements minimaux, cohérents et réversibles. Éviter les duplications entre documentation, instructions d'agents et configurations d'outils.
- Ne pas inventer de commandes de build, de test, de lint ou de déploiement. Découvrir les commandes réellement définies dans le dépôt et signaler celles qui n'existent pas.
- Exécuter les contrôles pertinents disponibles après une modification. Si un contrôle ne peut pas être exécuté, l'indiquer clairement et ne pas prétendre qu'il a réussi.
- Mettre à jour la documentation concernée lorsque le comportement ou l'architecture change. Ne pas modifier `brain/STATE.md` ou `brain/DECISIONS.md` pour donner l'impression qu'un travail non terminé est achevé.
- Ne pas introduire de dépendance ou de technologie structurante avant d'en avoir expliqué le besoin et obtenu la décision requise.

## 8. Critères de fin de tâche

Avant de déclarer un lot terminé :

1. Vérifier que le résultat correspond au périmètre et aux critères convenus.
2. Contrôler les changements réels (`git diff`, statut Git et fichiers affectés lorsque disponibles).
3. Rapporter ce qui a été fait, ce qui a été vérifié, les contrôles non exécutés, les décisions restant ouvertes et les risques connus.
4. Ne jamais annoncer un commit, un push, une synchronisation ou une création de fichier sans confirmation observable de son succès.

## 9. Maintenance de ce fichier

Garder ce fichier stable, portable et concis. Il contient les invariants communs qui doivent survivre aux changements de modèle, de conversation et d'éditeur ; il ne sert ni de journal de progression, ni de backlog, ni de documentation technique exhaustive.

Avant de le modifier, vérifier qu'il s'agit d'une règle durable, commune à plusieurs outils, et non d'une décision ponctuelle ou d'un détail d'implémentation. Les procédures détaillées vont dans les documents ou modules dédiés ; l'état courant va dans `brain/STATE.md` ; les décisions confirmées vont dans `brain/DECISIONS.md`.
