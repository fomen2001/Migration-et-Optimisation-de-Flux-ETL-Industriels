# Migration-et-Optimisation-de-Flux-ETL-Industriels
🏭 Migration et Optimisation de Flux ETL Industriels (R vers Python)

Ce projet a été conçu dans le cadre de la transformation digitale du département d'amélioration des produits et des technologies d'X-FAB France. L'objectif est de moderniser les pipelines de données critiques pour le suivi de la qualité (Yield Enhancement) en migrant des scripts hérités de R vers une architecture Python robuste et conteneurisée.

🎯 Objectifs du Projet

Modernisation : Migration de scripts statistiques complexes de R vers Python.

Performance : Utilisation de la bibliothèque Polars pour le traitement multithreadé de gros volumes de données capteurs.

Industrialisation : Conteneurisation des flux avec Docker pour garantir la portabilité et la reproductibilité.

Orchestration : Analyse comparative entre les planificateurs CRON et Apache Airflow pour la gestion des dépendances.

Qualité & DevOps : Mise en place d'un pipeline CI/CD pour automatiser les tests et le déploiement.

🛠️ Stack Technique

Langages : Python 3.11 (Polars, NumPy), R (Source).

Conteneurisation : Docker.

Orchestration : Apache Airflow (Cible) vs CRON (Legacy).

DevOps : GitHub Actions / GitLab CI.

Environnement : Linux / Debian-slim.

📂 Structure du Projet

.
├── etl_migration_polars.py  # Script ETL migré et optimisé (Python/Polars)
├── Dockerfile               # Configuration pour l'image Docker industrielle
├── requirements.txt         # Dépendances Python (polars, numpy, etc.)
├── rapport_benchmark.md     # Étude comparative Orchestration vs CRON
└── industrial_yield_metrics.csv # Résultat de l'extraction (Yield)


🚀 Installation et Utilisation

Prérequis

Docker installé sur votre machine.

Python 3.11+ (pour une exécution locale sans Docker).

Exécution avec Docker (Recommandé)

Construction de l'image :

docker build -t xfab-etl-migration .


Lancement du conteneur :

docker run --name etl-instance xfab-etl-migration


Analyse des Performances

Le script utilise l'API Lazy de Polars pour optimiser les requêtes avant exécution. Cela permet d'obtenir des temps de traitement significativement plus rapides que les implémentations standards en R pour des datasets dépassant le million de lignes.

📊 Stratégie DevOps

Le projet suit les standards de sécurité industrielle :

Utilisation d'images de base légères (python-slim).

Exécution sous un utilisateur non-privé (xfab_user) à l'intérieur du conteneur.

Gestion stricte des dépendances pour éviter les vulnérabilités logicielles.

Auteur : Valdes Joel FOMENA TSATSOP

Candidature : Stage Data Engineering - X-FAB France