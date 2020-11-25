## MODULE TO PERFORM FEATURE ENGINEERING ON DATA





"------------------------------------------------------------------------------"
#############
## Imports ##
#############


## Python libraries

import sys

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import (
    train_test_split,
    cross_val_score
)
from sklearn.preprocessing import (
    OneHotEncoder
)
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline



## Ancillary modules

from src.utils.data_dict import (
    data_dict
)

from src.utils.utils import (
    load_df,
    save_df
)

from src.utils.params import (
    param_grid,
    max_features,
    n_estimators,
    cv_rounds,
    evaluation_metric,
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


    ## Separating features from labels
    df_features = df.drop("label", axis=1)
    df_labels = df["label"]


    ## Cleaning features to leave only those relevant for the model.
    nr_features_cols = [key for key in data_dict if
                (data_dict[key]['relevant']==True) &
                (data_dict[key]['model_relevant']==False)
              ]
    df_features.drop(nr_features_cols, axis=1, inplace=True)
    features_cols = list(df_features.columns)
    print("\n++ Complete list of features ({}) that will be fed to the model:".format(len(features_cols)))
    for col in features_cols:
        print("    {}. {}".format(features_cols.index(col) + 1, col))


    ## Generation dummy columns of categoric variables with OneHotEncoder
    #### Creating list of the features that will processed through the pipeline.
    cat_features = [key for key in data_dict if
                    (data_dict[key]['model_relevant']==True) &
                    (data_dict[key]['data_type']=='categoric')
                   ]
    print("\n++ List of categorical features ({}) that will be processed through the pipeline are:".format(len(cat_features)))
    for cat in cat_features:
        print("    {}. {}".format(cat_features.index(cat) + 1, cat))


    #### Building and applying pipeline.
    categoric_pipeline = Pipeline([('hotencode',OneHotEncoder())])
    pipeline = ColumnTransformer([('categoric', categoric_pipeline, cat_features)])
    df_features_prc = pipeline.fit_transform(df_features)


    return df_features_prc, df_labels




## Select most relevant features for the model.
def feature_selection(df_features_prc, df_labels):
    """
    Select most relevant features for the model.
        args:
            df_features_prc (dataframe): Xxx
            df_labels (dataframe): Xxx
        returns:
            Xxx
    """


    ## Selecting and training model - Random Forrest.
    model = RandomForestClassifier(max_features=max_features, n_estimators=n_estimators)
    print("\n++ The model that will be used is: {}\n".format(model))
    model.fit(df_features_prc, df_labels)


    ## Evaluating model performance with cross validation
    # print("\nFeatures feed to the model: {}\n".format(df_features_prc))
    # print("\nLabels feed to the model: {}\n".format(df_labels))
    cv_scores = cross_val_score(
        model,
        df_features_prc,
        df_labels,
        scoring=evaluation_metric,
        cv=cv_rounds
    )

    print("\n++ Model performance metrics:\n")
    print("    ++++ Cross validation scores:")
    i = 1
    for cvs in list(cv_scores):
        print("        Round {} -> {}".format(i, cvs))
        i += 1
    print("\n")
    print("    ++++ Cross validation mean score: {} \n".format(cv_scores.mean()))
    print("    ++++ Cross validation score standard deviation:\n", cv_scores.std())


    # ## Grid search CV to select best possible model.
    # grid_search = GridSearchCV(model,
    #                            param_grid,
    #                            cv=10,
    #                            scoring=evaluation_metric,
    #                            return_train_score=True)
    #
    # grid_search.fit(df_features_prc, df_labels)
    #
    # print(grid_search.best_params_)
    # print(grid_search.best_estimator_)


    return df_features_prc





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
    df_features_prc, df_labels = feature_generation(df)
    df_features_prc = feature_selection(df_features_prc, df_labels)
    save_fe(df_features_prc, fe_pickle_loc)
    print("** Feature engineering module successfully executed **")





"------------------------------------------------------------------------------"
"------------------------------------------------------------------------------"
#################
## END OF FILE ##
#################
"------------------------------------------------------------------------------"
"------------------------------------------------------------------------------"
