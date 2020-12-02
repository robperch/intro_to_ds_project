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
ingestion_pickle_loc = "outputs/ingest_df.pkl"

## Transformation
transformation_pickle_loc = "outputs/transformation_df.pkl"

## Feature engineering
fe_pickle_loc_imp_features = "outputs/fe_df_imp_features.pkl"
fe_pickle_loc_feature_labs = "outputs/fe_df_feature_labs.pkl"

## Modeling
models_pickle_loc = "outputs/model_loop.pkl"





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

    "rf": {
        "model": RandomForestClassifier(
            max_features=6,
            n_estimators=10,
            max_leaf_nodes=10,
            oob_score=True,
            n_jobs=-1,
            random_state=1111
        ),
        "param_grid": {
            "n_estimators": [400],
            "min_samples_leaf": [9],
            "criterion": ['gini']
        }
    },

    "dt": {
        "model": DecisionTreeClassifier(
            random_state=2222
            ),
        "param_grid": {
            'n_estimators': [500],
            'max_depth': [15],
            'min_samples_leaf': [7]
        }
    },

}


## Additional parameters for cv_grid
cv_rounds = 1
evaluation_metric = "accuracy"
feature_importance_theshold = 0.005#0.07
tag_non_relevant_cats = "other_nr_categories"





"------------------------------------------------------------------------------"
"------------------------------------------------------------------------------"
#################
## END OF FILE ##
#################
"------------------------------------------------------------------------------"
"------------------------------------------------------------------------------"
