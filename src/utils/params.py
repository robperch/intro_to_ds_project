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
param_grid = [
    {
        "n_estimators": [50, 100, 150, 500],
        "max_features": [2, 4, 6, 8]
    },
    {
        "bootstrap": [False],
        "n_estimators": [3, 10],
        "max_features": [2, 3, 4]
    }
]


## Model parameters
#### Random forest regressor
max_features = 6
n_estimators = 100
cv_rounds = 10
evaluation_metric = "accuracy"





"------------------------------------------------------------------------------"
"------------------------------------------------------------------------------"
#################
## END OF FILE ##
#################
"------------------------------------------------------------------------------"
"------------------------------------------------------------------------------"
