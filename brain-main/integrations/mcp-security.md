# Sécurité MCP

Un fichier de règles ne crée pas une connexion. Vérifier que le client expose l'outil avant de l'utiliser. S'il manque, le dire sans simuler l'appel.

- Lecture : respecter l'identité connectée.
- Proposition : décrire le changement externe sans l'appliquer.
- Écriture : approbation humaine de l'action précise.
- Suppression, publication, opération de masse : confirmation distincte et cibles exactes.

Aucun jeton dans Git. Après une action réellement exécutée, rapporter le service, les identifiants retournés et les erreurs, sans secret.

Une synchronisation bidirectionnelle exige un contrat séparé : propriétaire de chaque champ, conflits, suppressions, reprise. Ce contrat n'existe pas encore.
