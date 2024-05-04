#####################################
#    TEST OF PROJECT'S FUNCTIONS ####
##################################### 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import eda
import os
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV, GroupKFold
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
os.chdir(os.getcwd()) 

def series_to_supervised(df, n_in=1, n_out=1, dropnan=True, target_vars=None):
    """
    Cette fonction prend un DataFrame, crée des séquences d'entrées et de sorties en fonction des décalages spécifiés par n_in et n_out, 
    et retourne un nouveau DataFrame qui peut être utilisé pour entraîner des modèles de machine learning comme le Random Forest.

    Le Dataframe original sera transformé ajoutant plusiueurs nouvelles colonnes :

        La première colonne sera un décalage de 1 pas de temps (t-1)
        La deuxième colonne sera un décalage de 2 pas de temps (t-2), et ainsi de suite jusqu'à 3 pas de temps dans le passé (t-3).
        ...
        La N-ieme colonne sera un décalage de i pas de temps (t-i) et ainsi de suite. 

        La dernière colonne (t+0 ou simplement t) sera la valeur actuelle (valeur cible pour les prédictions basées sur les valeurs i pas de temps précédents)
    args : 
            => n_in : nb de valeusr passées souhaités
            => n_out : nb de valeurs futures souhaités - 1

    """
    if target_vars is None:
        print ('Aucune variable cible selectionée !! ')
        return df  # Si aucune cible spécifique n'est donnée, rien changer

    n_vars = 1 if type(df) is list else df.shape[1]
    df = pd.DataFrame(df)
    cols, names = list(), list()
    
    # Ajout des valeurs passés : 
    for var in target_vars:
        for i in range(n_in, 0, -1):
            cols.append(df[var].shift(i))
            names += [(f'{df.columns[j]}_t-{i}') for j in range(n_vars)]
    
    # Valeurs futures :
    for var in target_vars:
        for i in range(0, n_out):
            cols.append(df[var].shift(-i))
            if i == 0:
                names += [(f'{df.columns[j]}_t') for j in range(n_vars)]
            else:
                names += [(f'{df.columns[j]}_t+{i}') for j in range(n_vars)]
    
    # on rassemble toutes les colo,nnes crées : 
    agg = pd.concat(cols, axis=1)
    agg.columns = names
    
    # drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)
    
    #Ajout des autres varaibles qui ne sont pas des décalage de notre cible 
    final_df = df.join(agg)
    final_columns = list(df.columns) + names
    final_df = final_df[final_columns]
    
    return final_df


    ########################################### TEST //
np.random.seed(0)
dates = pd.date_range('20230101', periods=10)
data = np.random.randn(10)  # données aléatoires
test = pd.DataFrame(data, index=dates, columns=['data'])

print("DataFrame original:")
print(test)

# Transformons ce DataFrame pour inclure 3 lags
transformed_df = series_to_supervised(test, n_in=3, n_out=3, dropnan=True, target_vars= ['data'])

print("DataFrame transformé pour l'apprentissage supervisé:")
transformed_df