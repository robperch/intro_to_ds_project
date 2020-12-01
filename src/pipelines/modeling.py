## MODULE TO EXECUTE VARIOUS MODELS AND DETERMINE THE BEST POSSIBLE ONE.





"------------------------------------------------------------------------------"
#############
## Imports ##
#############


## Ancillary modules

from src.utils.params import (
    fe_pickle_loc,
    models_pickle_loc,
)





"------------------------------------------------------------------------------"
#################################
## Generic ancillary functions ##
#################################


## Loading transformation pickle as dataframe for transformation pipeline.
def load_features(path):
    """
    Loading fe pickle as dataframe from fe pipeline.
        args:
            path (string): location where the pickle that will be loaded is.
        returns:
            -
    """

    df = load_df(path)

    return df



## Save best model form magic loop as pickle.
def save_models(selected_model, path):
    """
    Save best model form magic loop as pickle.
        args:
            selected_model (dataframe): model that got best performance in magic loop.
            path (string): location where the pickle object will be stored.
        returns:
            -
    """

    save_df(selected_model, path)





"------------------------------------------------------------------------------"
########################
## Modeling functions ##
########################





"------------------------------------------------------------------------------"
############################
## Modeling main function ##
############################


## Function desigend to execute all fe functions.
def model_evaluation(transformation_pickle_loc, fe_pickle_loc):
    """
    Function desigend to execute all fe functions.
        args:
            transformation_pickle_loc (string): path where the picke obtained from the transformation is.
            fe_pickle_loc (string): location where the resulting pickle object will be stored.
        returns:
            -
    """

    ## Executing transformation functions
    df = load_transformation(transformation_pickle_loc)
    df_features_prc, df_labels, df_features_prc_cols = feature_generation(df)
    df_features_prc = feature_selection(df_features_prc, df_labels, df_features_prc_cols)
    save_fe(df_features_prc, fe_pickle_loc)
    print("\n** Feature engineering module successfully executed **\n")





"------------------------------------------------------------------------------"
"------------------------------------------------------------------------------"
#################
## END OF FILE ##
#################
"------------------------------------------------------------------------------"
"------------------------------------------------------------------------------"
