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

from src.utils.utils import (
    save_df
)





"------------------------------------------------------------------------------"
##############################
## Data ingestion functions ##
##############################


## Converting data into pandas dataframe by providing the data's location.
def ingest_file(filename):
    """
    Converting data into pandas dataframe by providing the data's location.
        args:
            filename (string): path relative to the repo's root where the data (.csv file) is located
        returns:
            df_c5 (dataframe): .csv file converted to pandas dataframe
    """

    ## Reading file in specified path
    df_c5 = pd.read_csv(filename)

    return df_c5



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





"------------------------------------------------------------------------------"
###############################
## Ingestion master function ##
###############################


## Function desigend to execute all ingestion functions.
def ingest(data_path, ingestion_pickle_loc):
    """
    Function desigend to execute all ingestion functions.
        args:
            data_path (string): path where the project's data is stored.
            ingestion_pickle_loc (string): location where the resulting pickle object will be stored.
        returns:
            -
    """

    ## Executing ingestion functions
    df = ingest_file(data_path)
    drop_cols(df)
    generate_label(df)
    save_ingestion(df, ingestion_pickle_loc)





"------------------------------------------------------------------------------"
#################
## END OF FILE ##
#################
"------------------------------------------------------------------------------"
