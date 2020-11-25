## MODULE WITH PROJECT PARAMETERS





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
fe_pickle_loc = "outputs/fe_df.pkl"





"------------------------------------------------------------------------------"
###################
## ML parameters ##
###################


## Grid Search CV - Parameters grid
param_grid = {
        "n_estimators": [400, 600, 800],
        "min_samples_leaf": [9],
        "criterion": ['gini']
    }


## Model parameters
#### Random forest classifier
max_features = 6
max_depth = 10
n_estimators = 10
max_leaf_nodes = 10
cv_rounds = 4
evaluation_metric = "accuracy"





"------------------------------------------------------------------------------"
"------------------------------------------------------------------------------"
#################
## END OF FILE ##
#################
"------------------------------------------------------------------------------"
"------------------------------------------------------------------------------"
