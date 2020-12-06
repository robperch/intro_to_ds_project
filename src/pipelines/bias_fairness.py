# MODULE FOR AEQUITAS ANALYSIS SAVE METRICS AS PICKLE
"------------------------------------------------------------------------------"
#############
## Imports ##
#############

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import (
    OneHotEncoder,
    StandardScaler
)
import pandas as pd
import numpy as np
import seaborn as sns
import sys


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
import pickle

## Análisis Aequitas 
from aequitas.group import Group
from aequitas.bias import Bias
from aequitas.fairness import Fairness
from aequitas.plotting import Plot

#################################
## Generic ancillary functions ##
#################################


def load_selected_model(path):
  """
       args:
           path (string): location where the pickle that will be loaded is.
           returns:
           -
   """
  load_df(path)
      pass


  
"------------------------------------------------------------------------------"
##############################
## Aeaquitas Analysis functions ##
##############################


def group(df):  
    """
     args:
         df (dataframe):Recibe el path en donde se encuentra el pickle con el modelo seleccionado en la parte de selección de modelo.
     returns:
         -
      """
      pass
    
    
    
def bias(df): 
    """
     args:
         df (dataframe): Recibe el data frame que tiene los features sobre los que queremos medir la disparidad
     returns:
         -
    """
    pass
    
    

def fairness(df):
    """
     args:
         df (dataframe): Recibe el data frame que tiene los features sobre los que queremos medir la equidad.
     returns:
         -
    """
    pass


"------------------------------------------------------------------------------"


##############################
## Model Evaluation functions ##
##############################

def bias_fairness(df):
    """
     args:
         df (dataframe): dataframes that will be analyzed by Aequitas according to the selected model. 
     returns:
         -
    """
    
    model=load_selected_model(path)
    df=group(df)
    df=bias(df)
    df=fairness(df)
    pass
  