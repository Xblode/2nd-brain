# Gouvernance

Niveaux prévus, pas encore appliqués par du code :

- `READ` : lire fichiers, registre ou index.
- `PROPOSE` : préparer un changement sans l'appliquer.
- `APPLY_APPROVED` : appliquer une proposition approuvée par un humain.
- `INDEX` : reconstruire l'index dérivé.
- `DIAGNOSTIC` : inspecter et rapporter.

La lecture n'autorise pas l'écriture. Une proposition ne s'approuve pas elle-même. L'Inbox est exclue de toute écriture automatisée. Une suppression demande une confirmation distincte.

Le journal d'une application approuvée devra noter la date, la cible, l'opération et le résultat, sans secret. Sa forme exacte reste à préciser avec le cycle de vie de l'information.
