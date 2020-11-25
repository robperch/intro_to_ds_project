## MODULE TO PERFORM FEATURE ENGINEERING ON DATA





"------------------------------------------------------------------------------"
#############
## Imports ##
#############


## Python libraries

import sys


## Ancillary modules

from src.utils.utils import (
    load_df,
    save_df
)

from src.utils.params import (
    transformation_pickle_loc,
    fe_pickle_loc
)





"------------------------------------------------------------------------------"
#################################
## Generic ancillary functions ##
#################################


## Loading transformation pickle as dataframe for transformation pipeline.
def load_transformation(path):
    """
    Loading transformation pickle as dataframe for transformation pipeline.
        args:
            path (string): location where the pickle that will be loaded is.
        returns:
            -
    """

    df = load_df(path)

    return df



## Save fe data frame as pickle.
def save_fe(df, path):
    """
    Save fe data frame as pickle.
        args:
            df (dataframe): fe resulting dataframe.
            path (string): location where the pickle object will be stored.
        returns:
            -
    """

    save_df(df, path)





"------------------------------------------------------------------------------"
###################################
## Feature engineering functions ##
###################################


## Creating new features relevant for our model.
def feature_generation(df):
    """
    Creating new features relevant for our model.
        args:
            df (dataframe): df that will be engineered.
        returns:
            df (dataframe): resulting df with new features.
    """

    pass



## Select most relevant features for the model.
def feature_selection(df):
    """
    Select most relevant features for the model.
        args:
            df (dataframe): df whose features will be assesed.
        returns:
            df (dataframe): df with cleaned features.
    """

    pass





"------------------------------------------------------------------------------"
#######################################
## Feature engineering main function ##
#######################################


## Function desigend to execute all fe functions.
def feature_engineering(path):
    """
    Function desigend to execute all fe functions.
        args:
            path (string): path where the picke obtained from the transformation is.
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
