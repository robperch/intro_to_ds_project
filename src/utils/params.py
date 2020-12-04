## MODULE WITH PROJECT PARAMETERS





"------------------------------------------------------------------------------"
#############
## Imports ##
#############


## Python libraries.
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import (
    OneHotEncoder,
    StandardScaler
)
from sklearn.pipeline import Pipeline





"------------------------------------------------------------------------------"
####################
## Path locations ##
####################


## Ingestion
data_path = "data/incidentes-viales-c5.csv"
ingestion_pickle_loc = "outputs/ingest/ingest_df.pkl"

## Transformation
transformation_pickle_loc = "outputs/transformation/transformation_df.pkl"

## Feature engineering
fe_pickle_loc_imp_features = "outputs/feature_engineering/fe_df_imp_features.pkl"
fe_pickle_loc_feature_labs = "outputs/feature_engineering/fe_df_feature_labs.pkl"

## Modeling
models_pickle_loc = "outputs/modeling/model_loop.pkl"
X_train_pickle_loc = "outputs/modeling/X_train.pkl"
y_train_pickle_loc = "outputs/modeling/y_train.pkl"
X_test_pickle_loc = "outputs/modeling/X_test.pkl"
y_test_pickle_loc = "outputs/modeling/y_test.pkl"
test_predict_labs_pickle_loc = "outputs/modeling/test_predict_labs.pkl"
test_predict_scores_pickle_loc = "outputs/modeling/test_predict_scores.pkl"




"------------------------------------------------------------------------------"
###################
## ML parameters ##
###################


## Pipelines for processing data.
categoric_pipeline = Pipeline([
    ('hotencode',OneHotEncoder())
])
numeric_pipeline = Pipeline([
    ('std_scaler', StandardScaler())
])


## Models and parameters
models_dict = {

    "random_forest": {
        "model": RandomForestClassifier(
            max_features=6,
            n_estimators=10,
            max_leaf_nodes=10,
            oob_score=True,
            n_jobs=-1,
            random_state=1111
        ),
        "param_grid": {
            "n_estimators": [100, 300, 500, 800],
            "min_samples_leaf": [3, 5, 7],
            "criterion": ['gini']
        }
    },

    "decision_tree": {
        "model": DecisionTreeClassifier(
            random_state=2222
            ),
        "param_grid": {
            'max_depth': [5, 10, 15, None],
            'min_samples_leaf': [3, 5, 7]
        }
    },

}


## Additional parameters for cv_grid
time_series_splits = 8
evaluation_metric = "accuracy"
feature_importance_theshold = 0.15
tag_non_relevant_cats = "other_nr_categories"





"------------------------------------------------------------------------------"
"------------------------------------------------------------------------------"
#################
## END OF FILE ##
#################
"------------------------------------------------------------------------------"
"------------------------------------------------------------------------------"
