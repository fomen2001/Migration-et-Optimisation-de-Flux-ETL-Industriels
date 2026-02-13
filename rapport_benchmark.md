Projet de Migration ETL : X-FAB France

Ce projet répond aux exigences de transformation digitale du département d'amélioration des produits.

1. Benchmark : Orchestration vs CRON Scheduler

Dans le cadre du transfert vers la nouvelle infrastructure IT, j'ai analysé deux méthodes de déclenchement des flux :

Critère

CRON (Legacy)

Apache Airflow (Cible)

Complexité

Très faible (Configuration système)

Moyenne (Installation de l'infra)

Dépendances

Impossible de lier des scripts entre eux

Gestion native des DAGs (Graphes)

Observabilité

Logs basiques, pas d'interface

Interface UI, monitoring en temps réel

Reprise sur erreur

Manuelle

Automatique (Retries paramétrables)

Conclusion pour X-FAB : Le passage à Airflow est recommandé pour les flux critiques de "Yield Enhancement" afin de garantir la traçabilité des données et la gestion des échecs en cascade.

2. Pipeline CI/CD sous Docker

Pour automatiser le déploiement et garantir que "ce qui tourne en dev tourne en prod", j'ai conçu la stratégie suivante :

Build : À chaque git push, une image Docker est construite via GitHub Actions/GitLab CI.

Test : Exécution de tests unitaires (via pytest) pour vérifier que la migration R -> Python ne dégrade pas la précision des calculs.

Deploy : L'image est poussée sur un registre privé, puis déployée sur l'infrastructure IT.

3. Optimisation des performances

L'utilisation de Polars au lieu de Pandas permet de traiter les données de production (souvent volumineuses) de manière multithreadée, ce qui est crucial pour le temps réel industriel.

Réalisé par Valdes Joel FOMENA TSATSOP - Candidat Data Engineer