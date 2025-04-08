# Utiliser une image de base Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .
COPY app.py .
COPY lstm_optimized_model.h5 .
COPY scaler.pkl .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 5002 (port utilisé par Flask)
EXPOSE 5002

# Commande pour lancer l'application
CMD ["python", "app.py"]