## MODULE TO TRANSFORM DATA BASED ON DATA-TYPES AND SAVE RESULTS AS PICKLE





"------------------------------------------------------------------------------"
#############
## Imports ##
#############


## Python libraries





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
            -
    """

    pass



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

    pass





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

    pass
