## MODULE TO PERFORM FEATURE ENGINEERING ON DATA





"------------------------------------------------------------------------------"
#############
## Imports ##
#############


## Python libraries





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

    pass



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

    pass





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
