# Scripts

Emplacement cible. Aucun script de génération ou de sync n'est fourni pour l'instant.

Le déploiement du template est tranché par **DEC-008** et `templates/project/template-manifest.yaml` :
copie `copy_once` / `sync_shared`, lien `brain-main` via `.second-brain.yaml`, mises à jour en `propose_only` sans écraser le project-owned.

Ne pas écrire de script qui écrase un projet tant qu'il ne respecte pas ce contrat et l'approbation humaine (DEC-003).
