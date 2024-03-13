# Ce fichier contient un ensemble de fonctions permettant l'exploration des données

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def create_unique(df):
    """
    This function aims to explore the dataframe's composition. It's a usful function to show how many missing values each variable counts. 
    It is a general function adaptative with any panda dataframe. 

    args : 
        => df (pd.Dataframe) : the input data base
    return : 
        => df_unique (pd.Dataframe) : a data frame of all the input variables and their composition in term of missing values. \n

                                     'Column_name'  'Data_type'  'Number_of_unique'  'Number_of_missing'  'Unique_values' \n

                            Var1        ---             ---             ---                 ----                ---\n
                            Var2        ---             ---             ---                 ---                 ---\n
                            ...\n
                            Varn        ---             ---             ---                 ---                 ---\n
    """
    df_unique_list = []

    for col in df.columns:
        num_unique = df[col].nunique()

        if num_unique <= 15:
            unique_vals = list(df[col].unique())
        else:
            unique_vals = "More than 15 unique values"

        data_type = df[col].dtype
        num_missing = df[col].isnull().sum()
        percent_missing = num_missing / df.shape[0]

        df_unique_list.append({
            'Column_name': col,
            'Data_type': data_type,
            'Number_of_unique': num_unique,
            'Number_of_missing': num_missing,
            'Percentage_of_missing': percent_missing,
            'Unique_values': unique_vals
        })

    df_unique = pd.DataFrame(df_unique_list)

    return df_unique




def clean_na (df) : 
    """
    This function aims to clean our working dataframe from variable that we considere not useful for our exploration and duplicates. 
    For instance because of a large number of missing value. Moreover, we convert non numeric variable to encoded.
    
    args : 
        > df (pandas dataframe) : original datframe
    output :
        > df_clean (pandas dataframe) 

    """
    df_unique = create_unique(df)
    drop_list = []
    for index, row in df_unique.iterrows():

        label_encoder = LabelEncoder()
        colname = str(row['Column_name'])

        # Suppression des colonnes avec plus de 60% des valeurs manquantes
        if row['Percentage_of_missing'] > 0.6 : 
            try:
                df.drop(colname, axis=1, inplace=True)
                drop_list.append(colname)

            except KeyError:
                print(f"Column '{colname}' not found in DataFrame.")

        elif df[colname].dtype == 'O':  # Check if the dtype is 'object' (non-numeric)
            colname = str(row['Column_name'])
            df[str(colname) + '_encoded'] = label_encoder.fit_transform(df[colname].astype(str))

    print ('The list of variables deleted is : ' + str(drop_list))
    
    df = df.drop_duplicates(subset='N°DPE')

    return df




