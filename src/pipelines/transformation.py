## MODULE TO TRANSFORM DATA BASED ON DATA-TYPES AND SAVE RESULTS AS PICKLE





"------------------------------------------------------------------------------"
#############
## Imports ##
#############


## Python libraries

import pickle

import sys


## Ancillary modules

from src.utils.utils import (
    load_df,
    save_df
)

from src.utils.params import (
    ingestion_pickle_loc,
    transformation_pickle_loc
)





"------------------------------------------------------------------------------"
#################################
## Generic ancillary functions ##
#################################


## Loading ingestion pickle as dataframe for transformation pipeline.
def load_ingestion(path):
    """
    Loading ingestion pickle as dataframe for transformation pipeline.
        args:
            path (string): location where the pickle that will be loaded is.
        returns:
            df (dataframe): dataframe obtained from ingestion pickle.
    """

    df = load_df(path)

    return df



## Save transformed data frame as pickle.
def save_transformation(df, path):
    """
    Save transformed data frame as pickle.
        args:
            df (dataframe): transformation resulting dataframe.
            path (string): location where the pickle object will be stored.
        returns:
            -
    """

    save_df(df, path)
    
    
    

def newlabel_tipo_entrada(data):
    """
     Converting observatios for selected columns into new categoric label.
        args:
            col(string):name of column that will be changed.
            data (dataframe): data that is being analyzed.
        returns:
            data(dataframe): dataframe that is being analyzed with the observations (of the selected columns) in lowercase.
    """
    col="tipo_entrada"
    data[col] = data[col].replace(['LLAMADA DEL 911'],'LLAMADA_911_066')
    data[col] = data[col].replace(['LLAMADA DEL 066'],'LLAMADA_911_066')
    return data






"------------------------------------------------------------------------------"
##############################
## Transformation functions ##
##############################


## Conduct relevant transformations to date variables.
def date_transformation(col, df):
    """
    Conduct relevant transformations to date variables.
        args:
            col (string): name of date column that will be transformed.
            df (dataframe): df that will be transformed.
        returns:
            df (dataframe): resulting df with cleaned date column.
    """

    pass



## Conduct relevant transformations to numeric variables.
def numeric_tranformation(col, df):
    """
    Conduct relevant transformations to numeric variables.
        args:
            col (string): name of numeric column that will be transformed.
            df (dataframe): df that will be transformed.
        returns:
            df (dataframe): resulting df with cleaned numeric column.
    """

    pass



## Conduct relevant transformations to categoric variables.
def categoric_trasformation(col, df):
    """
    Conduct relevant transformations to categoric variables.
        args:
            col (string): name of categoric column that will be transformed.
            df (dataframe): df that will be transformed.
        returns:
            df (dataframe): resulting df with cleaned categoric column.
    """
    df=newlabel_tipo_entrada(data)
    return df
    
    
    


"------------------------------------------------------------------------------"
####################################
## Transformation master function ##
####################################


## Function desigend to execute all transformation functions.
def transform(path, ingestion_save):
    """
    Function desigend to execute all transformation functions.
        args:
            path (string): path where the picke obtained from the ingestion is.
            ingestion_save (string): location where the resulting pickle object will be stored.
        returns:
            -
    """

    ## Executing transformation functions
    df = load_ingestion(path)
    df = date_transformation(col, df)
    df = numeric_tranformation(col, df)
    df = categoric_trasformation(col, df)
    df = save_transformation(df, path)





"------------------------------------------------------------------------------"
#################
## END OF FILE ##
#################
"------------------------------------------------------------------------------"
