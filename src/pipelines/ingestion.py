## MODULE TO PERFORM INITIAL DATA TRANSFORMATIONS AND SAVE RESULTS AS PICKE





"------------------------------------------------------------------------------"
#############
## Imports ##
#############

## Python libraries

import pandas as pd

import sys

import pickle


## Ancillary modules

from src.utils.data_dict import (
    data_dict
)

from src.utils.params import (
    data_path,
    ingestion_pickle_loc
)

from src.utils.utils import (
    load_df,
    save_df
)





"------------------------------------------------------------------------------"
##############################
## Data ingestion functions ##
##############################


## Converting data into pandas dataframe by providing the data's location.
def ingest_file(data_path):
    """
    Converting data into pandas dataframe by providing the data's location.
        args:
            filename (string): path relative to the repo's root where the data (.csv file) is located
        returns:
            df_c5 (dataframe): .csv file converted to pandas dataframe
    """

    ## Reading file in specified path
    df = pd.read_csv(data_path)

    return df



## Saving dataframe as pickle object in specified location.
def save_ingestion(df, path):
    """
    Saving dataframe as pickle object in specified location.
        args:
            df (dataframe): df that will be converted and saved as pickle.
            path (string): location where the pickle will be stored.
    """

    ## Converting and saving dataframe.
    save_df(df, path)





"------------------------------------------------------------------------------"
#############################
## Data cleaning functions ##
#############################


## Set the unique call identifier as index
def set_index(df):
    """
    Set the unique call identifier as index
        args:
            df (dataframe): df whose index will be asigned.
        returns:
            df (dataframe): df with correct index.
    """

    ## Selection the if feature based on data dict and setting it as index.
    id_feature = [key for key in data_dict if "id_feature" in data_dict[key]][0]
    df.set_index(id_feature, inplace=True, drop=False)

    return df



## Eliminating unused columns from dataframe.
def drop_cols(df):
    """
    Eliminating unused columns from dataframe.
        args:
            df (dataframe): df that will be cleaned.
        returns:
            -
    """

    ## Obtainig list of columns that are relevant
    nrel_col = [col for col in data_dict if data_dict[col]["relevant"] == False]

    ## Dropping non relevant columns
    df.drop(nrel_col, inplace=True, axis=1)


    return df



## Create new column on working dataframe to discriminate false from true calls.
def generate_label(df):
    """
    Create new column on working dataframe to discriminate false from true calls.
        args:
            df (dataframe): df where the new column will be added.
        returns:
            -
    """

    ## Crating new label column,
    df["label"] = df["codigo_cierre"].apply(lambda x: 1.0 if
                                            ("(F) " in x) |
                                            ("(N) " in x)
                                            else 0.0
                                           )


    return df





"------------------------------------------------------------------------------"
###############################
## Ingestion master function ##
###############################


## Function desigend to execute all ingestion functions.
def ingest(data_path, ingestion_pickle_loc):
    """
    Function desigend to execute all ingestion functions.
        args:
            path (string): path where the project's data is stored.
            ingestion_save (string): location where the resulting pickle object will be stored.
        returns:
            -
    """

    ## Executing ingestion functions
    df = ingest_file(data_path)
    df = set_index(df)
    df = drop_cols(df)
    df = generate_label(df)
    save_ingestion(df, ingestion_pickle_loc)
    print("\n** Ingestion module successfully executed **\n")





"------------------------------------------------------------------------------"
"------------------------------------------------------------------------------"
#################
## END OF FILE ##
#################
"------------------------------------------------------------------------------"
"------------------------------------------------------------------------------"
