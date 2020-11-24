## MODULE TO PERFORM FEATURE ENGINEERING ON DATA





"------------------------------------------------------------------------------"
#############
## Imports ##
#############


## Python libraries

import sys

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import (
    train_test_split,
    cross_val_score
)


## Ancillary modules

from src.utils.utils import (
    load_df,
    save_df
)

from src.utils.params import (
    param_grid,
    max_features,
    n_estimators,
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


    ## Selecting and training model - Random Forrest.
    model = RandomForestRegressor(max_features=max_features, n_estimators=n_estimators)
    print("The model that will be used is: ", model)
    model.fit(housingc_prp, housingc_labs)


    ## Evaluating model performance with cross validation
    cv_scores = cross_val_score(
        model,
        housingc_prp,
        housingc_labs,
        scoring="precision",
        cv=cv_rounds
    )

    print("Scores:", cv_scores)
    print("Mean:", cv_scores.mean())
    print("Standard deviation:", cv_scores.std())


    ## Grid search CV to select best possible model.
    grid_search = GridSearchCV(model,
                               param_grid,
                               cv=10,
                               scoring="precision",
                               return_train_score=True)

    grid_search.fit(housing_prepared, housing_labels)

    print(grid_search.best_params_)
    print(grid_search.best_estimator_)


    return df





"------------------------------------------------------------------------------"
#######################################
## Feature engineering main function ##
#######################################


## Function desigend to execute all fe functions.
def feature_engineering(transformation_pickle_loc, fe_pickle_loc):
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
    df = feature_generation(df)
    df = feature_selection(df)
    save_fe(df, fe_pickle_loc)





"------------------------------------------------------------------------------"
#################
## END OF FILE ##
#################
"------------------------------------------------------------------------------"
