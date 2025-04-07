# Projet-IA : Prédiction des arrêts de production du robot industriel Cobot UR3 - Maintenance Prédictive 
## Informations du Projet 
- **Etudiante 1** : CHAHO TANON Sarah Léthycia, Nom d'utilisateur: [Jesus-flower](https://github.com/Jesus-flower) \\
- **Etudiante 2** : SOUNOUVOU Ranti Jawu-Jésuton Maôz, Nom d'utilisateur: [jawu28](https://github.com/jawu28) \\

## Introduction
Ce projet vise à développer une solution d'intelligence artificielle capable de prédire les arrêts de protection d'un cobot UR3 à partir des données de ses capteurs. L'objectif est d'anticiper les problèmes potentiels et d'améliorer la maintenance prédictive dans un environnement industriel. 

## Dataset
Les données utilisées proviennent du dataset UR3 CobotOps, disponible sur le UCI Machine Learning Repository : https://archive.ics.uci.edu/dataset/963/ur3+cobotops
 

## Méthodologie

### 1. Exploration et prétraitement des données
- Analyse statistique des données et visualisation des distributions
- Étude des corrélations entre les variables et la cible "Protective Stops"
- Traitement des valeurs manquantes et normalisation des données
- Création de séquences temporelles de taille 10 pour l'entraînement des modèles

### 2. Développement et entraînement des modèles
Plusieurs modèles ont été développés et comparés :
- **Modèles Machine Learning** : Random Forest, XGBoost
- **Modèles Deep Learning** : LSTM, Bidirectional LSTM, CNN-LSTM

### 3. Optimisation des hyperparamètres
Une recherche exhaustive des hyperparamètres a été effectuée sur le modèle le plus performant, en testant différentes configurations :
- Nombre d'unités LSTM
- Nombre de neurones dans les couches denses
- Taux de dropout
- Taux d'apprentissage

### 4. Évaluation des modèles
Les modèles ont été évalués selon plusieurs métriques :
- Accuracy
- Precision
- Recall
- F1-score
- Courbe ROC et AUC

### 5. Optimisation des hyperparametres
Plusieurs modèles temporaires ont été créés pour tester différentes configurations, puis un modèle final avec les meilleurs paramètres a été retenu. Le but est de trouver la meilleure configuration avant d'implémenter l'API Flask.

### 6. Implémentation de l'API
Une API REST a été développée avec Flask pour déployer le modèle :
- Endpoint `/predict` pour prédire à partir d'une séquence unique
- Endpoint `/predict_sequence` pour analyser des séquences multiples
- Endpoint `/health` pour le monitoring de l'API

### 6. Conteneurisation
L'application a été conteneurisée avec Docker pour faciliter son déploiement et assurer sa portabilité.

## Comparaison des modèles

| Modèle               | Accuracy | Precision | Recall | F1-score |
|----------------------|----------|-----------|--------|----------|
| LSTM                 | x.xx     | x.xx      | x.xx   | x.xx     |
| Modèle finaloptimisé | x.xx     | x.xx      | x.xx   | x.xx     |

## Meilleurs hyperparamètres trouvés

- **LSTM units** : xxx
- **Dense units** : xxx
- **Dropout rate** : x.xx
- **Learning rate** : x.xxx


## Installation et Utilisation

### Prérequis
- Python 3.9+
- Docker (pour l'exécution conteneurisée)

### Requirements
- flask==2.0.1
- numpy==1.21.3
- pandas==1.3.4
- scikit-learn==1.0
- tensorflow==2.8.0
- joblib==1.1.0
- xgboost==1.5.0
- gunicorn==20.1.0
### Installation directe
1. Cloner le dépôt
```
git clone https://github.com/jawu28/Projet-IA.git
cd [ProjetIA]
```

2. Installer les dépendances
```
pip install -r requirements.txt
```

3. Lancer l'API
```
python app.py
```

### Utilisation avec Docker
1. Construire l'image Docker
```
docker build -t ur3-predictive-maintenance .
```

2. Lancer le conteneur
```
docker run -p 5000:5000 ur3-predictive-maintenance
```

### Utilisation de l'API

#### Prédiction à partir d'une séquence
```python
import requests
import json

# Exemple de données (séquence de 10 points temporels)
data = [
    {
        "J0_C": 0.1, "J1_C": 0.2, ..., "Grip Losses": 0
    },
    # ... autres points temporels
]

response = requests.post(
    "http://localhost:5000/predict",
    json=data
)

result = response.json()
print(result)
```

## Conclusion

Ce projet démontre l'efficacité des techniques d'apprentissage automatique et profond pour la prédiction des arrêts de protection dans un environnement robotique industriel. Le modèle développé permet d'anticiper les problèmes potentiels avec une précision satisfaisante, offrant ainsi une solution viable pour la maintenance prédictive.

Les futurs travaux pourraient inclure l'amélioration du modèle avec des architectures plus avancées, l'intégration de données supplémentaires ou l'extension de l'API pour une intégration plus poussée dans un système de production.






