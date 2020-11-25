## MODULE TO PERFORM FEATURE ENGINEERING ON DATA





"------------------------------------------------------------------------------"
#############
## Imports ##
#############


## Python libraries

import sys

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import (
    GridSearchCV,
    TimeSeriesSplit
)
from sklearn.model_selection import (
    train_test_split,
    cross_val_score
)
from sklearn.preprocessing import (
    OneHotEncoder,
    StandardScaler
)
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline



## Ancillary modules

from src.utils.data_dict import (
    data_created_dict,
    data_dict
)

from src.utils.utils import (
    load_df,
    save_df
)

from src.utils.params import (
    param_grid,
    max_features,
    max_depth,
    n_estimators,
    max_leaf_nodes,
    cv_rounds,
    evaluation_metric,
    transformation_pickle_loc,
    fe_pickle_loc
)

import pandas as pd





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



##
def get_feature_out(estimator, feature_in):
    if hasattr(estimator,'get_feature_names'):
        if isinstance(estimator, _VectorizerMixin):
            # handling all vectorizers
            return [f'vec_{f}' \
                for f in estimator.get_feature_names()]
        else:
            return estimator.get_feature_names(feature_in)
    elif isinstance(estimator, SelectorMixin):
        return np.array(feature_in)[estimator.get_support()]
    else:
        return feature_in



##
def get_ct_feature_names(ct):
    # handles all estimators, pipelines inside ColumnTransfomer
    # doesn't work when remainder =='passthrough'
    # which requires the input column names.
    output_features = []

    for name, estimator, features in ct.transformers_:
        if name!='remainder':
            if isinstance(estimator, Pipeline):
                current_features = features
                for step in estimator:
                    current_features = get_feature_out(step, current_features)
                features_out = current_features
            else:
                features_out = get_feature_out(estimator, features)
            output_features.extend(features_out)
        elif estimator=='passthrough':
            output_features.extend(ct._feature_names_in[features])

    return output_features





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

    #### Creating list of the features that will processed through the pipeline (categoric).
    cat_features_orig = [key for key in data_dict if
                    (data_dict[key]['model_relevant']==True) &
                    (data_dict[key]['data_type']=='categoric')
                   ]

    cat_features_add = [key for key in data_created_dict if
                    (data_created_dict[key]['model_relevant']==True) &
                    (data_created_dict[key]['data_type']=='categoric')
                   ]
    cat_features = cat_features_orig + cat_features_add

    print("\n++ List of categorical features ({}) that will be processed through the categoric pipeline are:".format(len(cat_features)))
    ohe_dict = {}
    for cat in cat_features:
        print("    {}. {}".format(cat_features.index(cat) + 1, cat))
        cat_list = list(df[cat].unique())
        cat_list.sort()
        ohe_dict[cat] = cat_list

    #### Creating list of the features that will processed through the pipeline (numeric).
    num_features_orig = [key for key in data_dict if
                    (data_dict[key]['model_relevant']==True) &
                    (data_dict[key]['data_type']=='numeric')
                   ]
    num_features_add = [key for key in data_created_dict if
                    (data_created_dict[key]['model_relevant']==True) &
                    (data_created_dict[key]['data_type']=='numeric')
                   ]
    num_features = num_features_orig + num_features_add

    print("\n++ List of numeric features ({}) that will be processed through the numeric pipeline are:".format(len(num_features)))
    for num in num_features:
        print("    {}. {}".format(num_features.index(num) + 1, num))


    #### Building and applying pipeline.
    categoric_pipeline = Pipeline([
        ('hotencode',OneHotEncoder())
    ])
    numeric_pipeline = Pipeline([
        ('std_scaler', StandardScaler())
    ])

    pipeline = ColumnTransformer([
        ('categoric', categoric_pipeline, cat_features),
        ('numeric', numeric_pipeline, num_features)
    ])
    # print(df_features.columns)
    df_features_prc = pipeline.fit_transform(df_features)
    print("\n    ++++ Dimensions of matrix after going through pipeline: {}\n".format(df_features_prc.shape))


    ## List of all features that were fed to the model.
    df_features_prc_cols = list(df_features.columns)
    for ohe_key in ohe_dict:
        for i in range(len(ohe_dict[ohe_key])):
            df_features_prc_cols.insert(i + df_features_prc_cols.index(ohe_key), ohe_dict[ohe_key][i])
        df_features_prc_cols.remove(ohe_key)
    # print(list(df_features_prc_cols))
    # print(len(df_features_prc_cols))

    # enc_cat_features = pipeline.named_transformers_['categoric']['hotencode'].get_feature_names()
    # print(enc_cat_features)
    # labels = np.concatenate([numeric_features, enc_cat_features])
    # transformed_df_columns = pd.DataFrame(preprocessor.transform(X_train).toarray(), columns=labels).columns
    # print(transformed_df_columns)


    return df_features_prc, df_labels, df_features_prc_cols




## Select most relevant features for the model.
def feature_selection(df_features_prc, df_labels, df_features_prc_cols):
    """
    Select most relevant features for the model.
        args:
            df_features_prc (dataframe): Xxx
            df_labels (dataframe): Xxx
        returns:
            Xxx
    """


    ## Splitting data in train and test
    X_train, X_test, y_train, y_test = train_test_split(df_features_prc, df_labels, test_size=0.3)


    ## Selecting and training model - Random Forrest.
    model = RandomForestClassifier(
        max_features,
        max_depth,
        n_estimators,
        max_leaf_nodes,
        oob_score=True,
        n_jobs=-1,
    )
    print("\n++ The model that will be used is: {}\n".format(model))


    ## Evaluating model performance with cross validation
    # cv_scores = cross_val_score(
    #     model,
    #     df_features_prc,
    #     df_labels,
    #     scoring=evaluation_metric,
    #     cv=cv_rounds
    # )
    #
    # print("\n++ Model performance metrics:\n")
    # print("    ++++ Cross validation scores:")
    # i = 1
    # for cvs in list(cv_scores):
    #     print("        Round {} -> {}".format(i, cvs))
    #     i += 1
    # print("\n")
    # print("    ++++ Cross validation mean score: {} \n".format(cv_scores.mean()))
    # print("    ++++ Cross validation score standard deviation:\n", cv_scores.std())

    tscv = TimeSeriesSplit(n_splits=2)

    ## Grid search CV to select best possible model.
    grid_search = GridSearchCV(model,
                               param_grid,
                               cv=tscv,
                               scoring=evaluation_metric,
                               return_train_score=True,
                               n_jobs=-1
                               )

    grid_search.fit(X_train, y_train)

    print(grid_search.best_params_)
    print(grid_search.best_estimator_)

    print("\n++ Grid search results:\n")
    print("    ++++ Best estimator: {}".format(grid_search.best_estimator_))
    print("    ++++ Number of features in best estimator: {} \n".format(grid_search.best_estimator_.n_features_))
    print("    ++++ Best estimator oob score: {}\n".format(grid_search.best_estimator_.oob_score_))


    ## Determining model's best estimators
    feature_importance = pd.DataFrame(
        {
            "Importance": grid_search.best_estimator_.feature_importances_,
            "Feature": df_features_prc_cols
        }
    )
    feature_importance.sort_values(by="Importance", ascending=False, inplace=True)
    print(feature_importance) 


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
