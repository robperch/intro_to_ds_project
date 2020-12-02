## MODULE TO EXECUTE VARIOUS MODELS AND DETERMINE THE BEST POSSIBLE ONE.





"------------------------------------------------------------------------------"
#############
## Imports ##
#############


## Python libraries

from sklearn.model_selection import (
    GridSearchCV,
    TimeSeriesSplit
)

from sklearn.model_selection import (
    train_test_split
)


## Ancillary modules

from src.utils.utils import (
    load_df,
    save_df
)

from src.utils.params import (
    fe_pickle_loc_imp_features,
    fe_pickle_loc_feature_labs,
    models_pickle_loc,
    models_dict,
    evaluation_metric,
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



##
def select_best_model(models_mloop):
    """
    """

    res = "nothing_"
    bench = 0

    for mdl in models_mloop:
        if models_mloop[mdl]["best_estimator_score"] > bench:
            res = mdl
            bench = models_mloop[mdl]["best_estimator_score"]

    print("\n++The model with the best performance is: {} (score: {})".format(res, round(bench, 6)))

    return res





"------------------------------------------------------------------------------"
########################
## Modeling functions ##
########################


##
def magic_loop(models_dict, df_imp_features_prc, df_labels):
    """
    """


    ## Splitting data in train and test
    X_train, X_test, y_train, y_test = train_test_split(df_imp_features_prc, df_labels, test_size=0.3)


    ##
    models_mloop = {}
    for mdl in models_dict:

        model = models_dict[mdl]["model"]

        grid_search = GridSearchCV(model,
                               models_dict[mdl]["param_grid"],
                               cv=TimeSeriesSplit(n_splits=2),
                               scoring=evaluation_metric,
                               return_train_score=True,
                               n_jobs=-1
                               )
        grid_search.fit(X_train, y_train)

        models_mloop[mdl] = {
            "best_estimator": grid_search.best_estimator_,
            "best_estimator_score": grid_search.best_score_
        }

    sel_model = models_mloop[select_best_model(models_mloop)]["best_estimator"]

    return sel_model





"------------------------------------------------------------------------------"
############################
## Modeling main function ##
############################


## Function desigend to execute all fe functions.
def modeling(fe_pickle_loc_imp_features, fe_pickle_loc_feature_labs):
    """
    Function desigend to execute all modeling functions.
        args:
            fe_pickle_loc (string): path where the picke obtained from the feature engineering is.
            models_pickle_loc (string): location where the resulting pickle object (best model) will be stored.
        returns:
            -
    """

    ## Executing modeling functions
    df_imp_features_prc = load_features(fe_pickle_loc_imp_features)
    df_labels = load_features(fe_pickle_loc_feature_labs)
    sel_model = magic_loop(models_dict, df_imp_features_prc, df_labels)
    save_models(sel_model, models_pickle_loc)
    print("\n** Modeling module successfully executed **\n")





"------------------------------------------------------------------------------"
"------------------------------------------------------------------------------"
#################
## END OF FILE ##
#################
"------------------------------------------------------------------------------"
"------------------------------------------------------------------------------"
