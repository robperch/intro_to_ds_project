# MODULE FOR MODEL EVALUATION  SAVE METRICS AS PICKLE
"------------------------------------------------------------------------------"
#############
## Imports ##
#############

from src.utils.utils import (
    load_df,
    save_df
)

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import (
    OneHotEncoder,
    StandardScaler
)
import pandas as pd
import numpy as np
## separando en train, test 
from sklearn.model_selection import train_test_split
## Configuración del RF
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
import time
from sklearn.preprocessing import StandardScaler, OneHotEncoder, KBinsDiscretizer
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
import matplotlib.pyplot as plt
import random

#################################
## Generic ancillary functions ##
#################################


def load_model(path):
  """
       args:
           path (string): location where the pickle that will be loaded is.
           returns:
           -
   """
  load_df(path)
      pass

def metrics(models):
  """
     args:
         models: selected best model.
     returns:
         -
  """
    pass

def save_metrics(df, path):
  """
       args:
           df(dataframe): dataframe with the metrics' table of the selected model.
           path (string): location where the pickle object will be stored.
       returns:
           -
  """
  save_df(df, path)
    pass

  
"------------------------------------------------------------------------------"
##############################
## Model Evaluation functions ##
##############################


def model_evaluation(path):
  models=load_model(path)
  df = metrics(models)
  save_metrics(df,path)
  pass
  
  