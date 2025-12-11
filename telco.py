"""
================================================================================
PROJET DATA SCIENCE - PRÉDICTION DU CHURN TÉLÉCOM
Partie I : Exploration et Préparation des Données
================================================================================

CONTEXTE :
Une entreprise de télécommunications fait face à un taux d'attrition élevé.
L'objectif est d'identifier les clients à risque pour mettre en place des
actions de rétention ciblées.

OBJECTIFS :
- Atteindre une précision de prédiction d'au moins 80%
- Identifier correctement 75% des clients qui vont partir
- Réduire le taux d'attrition de 15%
================================================================================
"""

# ============================================================================
# ÉTAPE 0 : INSTALLATION ET IMPORTS
# ============================================================================

# Si vous n'avez pas les bibliothèques, décommentez ces lignes :
# !pip install pandas numpy matplotlib seaborn scikit-learn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import warnings

warnings.filterwarnings('ignore')

# Configuration de l'affichage
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
pd.set_option('display.max_columns', None)

print("✅ Bibliothèques importées avec succès!")

# ============================================================================
# ÉTAPE 1 : CHARGEMENT DES DONNÉES
# ============================================================================

print("\n" + "=" * 80)
print("ÉTAPE 1 : CHARGEMENT DES DONNÉES")
print("=" * 80)

# IMPORTANT : Téléchargez d'abord le dataset depuis Kaggle
# https://www.kaggle.com/datasets/blastchar/telco-customer-churn
# Puis placez le fichier 'WA_Fn-UseC_-Telco-Customer-Churn.csv' dans le même dossier

try:
    data = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
    print("✅ Données chargées avec succès!")
except FileNotFoundError:
    print("❌ ERREUR : Fichier non trouvé!")
    print("\n📋 INSTRUCTIONS :")
    print("1. Allez sur : https://www.kaggle.com/datasets/blastchar/telco-customer-churn")
    print("2. Téléchargez le fichier CSV")
    print("3. Placez-le dans le même dossier que ce script")
    print("4. Relancez le script")
    exit()

