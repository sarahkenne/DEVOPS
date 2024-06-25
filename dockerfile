# Utiliser une image Python officielle comme image de base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le contenu du répertoire courant dans le répertoire de travail du conteneur
COPY . .

# Exposer le port sur lequel l'application Flask s'exécute
EXPOSE 5000

# Définir la variable d'environnement pour que Flask écoute sur toutes les interfaces
ENV FLASK_RUN_HOST=0.0.0.0

# Commande pour démarrer l'application Flask
CMD ["flask", "run"]
