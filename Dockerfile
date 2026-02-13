# Utilisation d'une image légère optimisée pour Python
FROM python:3.11-slim

# Définition du répertoire de travail
WORKDIR /app

# Installation des dépendances système nécessaires (ex: compilateurs si besoin)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copie des fichiers de dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du script ETL
COPY etl_migration_polars.py .

# Création d'un utilisateur non-root pour la sécurité (Standard DevOps)
RUN useradd -m xfab_user
USER xfab_user

# Commande de lancement
CMD ["python", "etl_migration_polars.py"]