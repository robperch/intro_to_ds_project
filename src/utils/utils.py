## MODULE WITH FUNCTIONS TO SAVE AND LOAD PICKLE, AS WELL AS OTHER USEFULL FUNCTIONS.





"------------------------------------------------------------------------------"
#############
## Imports ##
#############

## Python libraries

import json

import pandas as pd

import sys

import pickle


## Ancillary modules

# sys.path.append("..")

from src.utils.data_dict import (
    data_dict
)





"------------------------------------------------------------------------------"
#################################
## Generic ancillary functions ##
#################################


## Pretty print a dictionary and preserving special characters
def json_dump_dict(dictionary):
    """
    Pretty print a dictionary and preserving special characters
        args:
            dictionary (dictionary): dict that will be pretty printed
        returns:
            -
    """

    print(json.dumps(dictionary, indent=4, ensure_ascii=False).encode("utf8").decode())

    return



## Loading pickle.
def load_df(path):
    """
    Loading pickle.
        args:
            path (string): specific location of pickle that will be loaded.
        returns:
            pickle_load (*various*): loaded pickle object; most likely a dataframe.
    """

    pickle_load = pickle.load(open(path, "rb"))

    return pickle_load



## Dataframe that will be saved as picke object at specified path.
def save_df(df, path):
    """
    Dataframe that will be saved as picke object at specified path.
        args:
            df (dataframe): dataframe that will be converted and saved as pickle.
            path (string): location where the pickle will be placed.
        returns:
            -
    """

    pickle.dump(df, open(path, "wb"))





"------------------------------------------------------------------------------"
##############################
## Data profiling functions ##
##############################


## Counting number of variables in data (¿Cuántas variables tenemos?)
def count_vars(data):
    """
    Counting number of variables in data
        args:
            data (dataframe): data that is being analyzed
        returns:
             res (int): number of variables in the data
    """

    res = data.shape[1]
    print("Número de variables en los datos --> {}".format(res))

    return



## Counting number of observations in data (¿Cuántas observaciones tenemos?)
def count_obs(data):
    """
    Counting number of observations in data
        args:
            data (dataframe): data that is being analyzed
        returns:
            res (int): number of observations in the data

    """

    res = data.shape[0]

    print("Número de observaciones en los datos --> {}".format(res))

    return



## Counting number of unique observations for all variables
def count_unique_obs(data):
    """
    Counting number of unique observations for all variables
        args:
        data (dataframe): data that is being analyzed
        returns:
        (series): number of unique observations for all variables
    """
    return data.nunique()



## Creting table with classification of variables based in definition dictionary.
def vars_classif_by_type():
    """
    Creting table with classification of variables based in definition dictionary.
        args:
            -
        returns:
            -
    """

    ## Creating and populating dictionary with classified variables according to data type.
    data_classif = {}

    for var in data_dict:

        dt = data_dict[var]["data_type"]

        if dt not in data_classif:
            data_classif[dt] = []
            data_classif[dt].append(var)

        else:
            data_classif[dt].append(var)


    ## Converting dictionary to dataframe and displaying results
    data_classif = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data_classif.items()])).fillna("-")

    print(display(data_classif))


    return



## Data profiling for numeric variables
def data_profiling_numeric(data, num_vars):
    """
    Data profiling for numeric variables
        Args:
            data(dataframe): dataframe that will be analyzed.
        num_vars (list): list of variables' names in the dataframe that will be analyzed.
        Retruns:
            Dataframe with the data profiling (type, number of observations, mean, sd, quartiles, max, min, unique observations, top 5 repeated observations, number of null variables)
            of the choosen numeric variables.
    """

    ## Copy of initial dataframe to select only numerical columns
    dfx = data.loc[:, num_vars]


    ## Pipeline to create dataframe with general data description
    print("*********************************")
    print("** General description of data **")
    print("*********************************")

    #### List where the resulting dataframes will be stored for further concatenation
    res_dfs = []

    #### Type of numeric variables
    dfx_dtype = dfx.dtypes.to_frame().T
    dfx_dtype.index = ["dtype"]
    res_dfs.append(dfx_dtype)

    #### Counting unique variables
    dfx_uniqvars = dfx.nunique().to_frame().T
    dfx_uniqvars.index = ["count_unique"]
    res_dfs.append(dfx_uniqvars)

    #### Counting missing values
    dfx_missing = dfx.isnull().sum().to_frame().T
    dfx_missing.index = ["missing_v"]
    res_dfs.append(dfx_missing)

    #### General description of the data and addition of min values
    dfx_desc = dfx.describe()
    dfx_desc.loc["min", :] = dfx.min(axis=0)
    res_dfs.append(dfx_desc)

    #### Concatenating resulting dataframes into one final result
    print(display(pd.concat(res_dfs, axis=0)))
    print("-"*75)
    print("-"*75)
    print("\n\n".format())


    ## Pipeline to obtain top repeated variables per column
    print("****************************")
    print("** Top repeated variables **")
    print("****************************")

    #### Initial variables
    tops = 5 #### Number of tops that will be selected
    i = 0 #### Counter to start joining dataframes

    #### Loop through all variables that will be processed
    for col_sel in dfx:

        #### Creating dataframe with top entries and count
        dfxx = dfx[col_sel].value_counts().iloc[:tops].to_frame()
        dfxx.reset_index(drop=False, inplace=True)
        dfxx["part"] = round(dfxx[col_sel]/dfx[col_sel].count()*100, 2)
        dfxx.columns = pd.MultiIndex.from_tuples([(col_sel, tag) for tag in ["value", "count", "part_notnull"]])

        #### Joining all the variables in one final dataframe
        if i == 0:
            df_tops = dfxx
            i += 1
        else:
            df_tops = df_tops.join(dfxx)

    ## Fill empty spaces of resulting dataframe and renaming index entries
    df_tops.fillna("-", inplace=True)
    df_tops.index = ["top_" + str(i) for i in range(1, df_tops.shape[0] + 1)]
    print(display(df_tops))
    print("-"*75)
    print("-"*75)
    print()


    return



## Create the data profiling of categorical variables.
def data_profiling_categ(data, cat_vars):
    """
    Create the data profiling of categorical variables.
        args:
            data (Data Frame): data set into Dataframe.
            cat_vars (list): list with categorical variables names.
        returns:
           display(): display the Dataframes with info.
    """

    print("*************************************")
    print("** Conteo y proporción de entradas **")
    print("*************************************")

    df_catVar_list = []

    for val in cat_vars:

        print("Variable categorica -> {}".format(val))

        catego  = data[val].value_counts()
        totalOb = len(data[val])
        can_Cat = len(catego)
        moda    = data[val].mode().values[0]
        valFal  = data[val].isnull().sum()
        top1    = [catego[0:1].index[0],catego[0:1].values[0]] if can_Cat >= 1 else 0
        top2    = [catego[1:2].index[0],catego[1:2].values[0]] if can_Cat >= 2 else 0
        top3    = [catego[2:3].index[0],catego[2:3].values[0]] if can_Cat >= 3 else 0

        elemVarCat = {
            "Info":val,
            "Num_Registros":[totalOb],
            "Num_de_categorias":[can_Cat],
            "Moda":[moda],
            "Valores_faltantes":[valFal],
            "Top1":[top1],
            "Top2":[top2],
            "Top3":[top3]
            }

        #primerdataframe
        df_catVar_list.append(pd.DataFrame(elemVarCat).set_index("Info").T)
        # print(display(pd.DataFrame(elemVarCat).set_index("Info").T))

        # print("Valores de las categorias y sus proporciones")
        #segundodataframe donde se muestra los valores de las categorias su cantidad y su proporción.
        pro = proporcion(catego, totalOb)
        dfProp = pd.DataFrame(pro, columns=['Categoría', 'Observaciones', 'Proporción']).set_index("Categoría")
        #mostrar primer data frame
        print(display(dfProp))
        print("\n\n".format())


    print("***************************************")
    print("** Impresión de resumen de variables **")
    print("***************************************")

    ## Print summary dataframe with results from categoric variables
    print(display(pd.concat(df_catVar_list, axis=1)))


    return



## Create the data profiling of date variables.
def data_profiling_date(data, date_vars):
    """
    Create the data profiling of categorical variables.
        args:
            data (Data Frame): project data set.
            date_vars (list): list with date variables names.
        returns:
            -
    """


    ## Craeting new dataframe with date columns and adjusting contents for profiling

    #### Working dataframe
    dfx = data.loc[:, date_vars]

    #### Filtering only hour in time data
    time_cols = ["hora_creacion"]
    for tc in time_cols:
        dfx[tc] = dfx[tc].apply(lambda x: x[:2] if x[2]==":" else "xx")

    #### Extracting date data from date column
    dfx["fecha_creacion_sep"] = dfx["fecha_creacion"].str.split(pat="/")

    date_desc = ["dia", "mes", "año"]
    for dd in date_desc:
        dfx[dd + "_creacion"] = dfx["fecha_creacion_sep"].apply(lambda x: x[date_desc.index(dd)])

    ###### Correcting years with length two
    dfx["año_creacion"] = dfx["año_creacion"].apply(lambda x: "20" + x if len(x)==2 else x)

    ###### Deleting acillary column
    dfx.drop("fecha_creacion_sep", axis=1, inplace=True)


    ## Conducting data profiling for date features - general description
    print("*********************************")
    print("** General description of data **")
    print("*********************************")

    #### List where the resulting dataframes will be stored for further concatenation
    res_dfs = []

    #### Type of numeric variables
    dfx_dtype = dfx.dtypes.to_frame().T
    dfx_dtype.index = ["dtype"]
    res_dfs.append(dfx_dtype)

    #### Counting missing values
    dfx_notnull = dfx.count().to_frame().T
    dfx_notnull.index = ["notnull_v"]
    res_dfs.append(dfx_notnull)

    #### Counting missing values
    dfx_missing = dfx.isnull().sum().to_frame().T
    dfx_missing.index = ["missing_v"]
    res_dfs.append(dfx_missing)

    #### Counting unique variables
    dfx_uniqvars = dfx.nunique().to_frame().T
    dfx_uniqvars.index = ["count_unique"]
    res_dfs.append(dfx_uniqvars)

    #### Concatenating resulting dataframes into one final result
    print(display(pd.concat(res_dfs, axis=0)))
    print("-"*75)
    print("-"*75)
    print("\n\n".format())


    ## Conducting data profiling for date features - top repeated features
    print("****************************")
    print("** Top repeated variables **")
    print("****************************")

    #### Initial variables
    tops = 5 #### Number of tops that will be selected
    i = 0 #### Counter to start joining dataframes

    #### Loop through all variables that will be processed
    for col_sel in dfx:

        #### Creating dataframe with top entries and count
        dfxx = dfx[col_sel].value_counts().iloc[:tops].to_frame()
        dfxx.reset_index(drop=False, inplace=True)
        dfxx["part"] = round(dfxx[col_sel]/dfx[col_sel].count()*100, 2)
        dfxx.columns = pd.MultiIndex.from_tuples([(col_sel, tag) for tag in ["value", "count", "part_notnull"]])

        #### Joining all the variables in one final dataframe
        if i == 0:
            df_tops = dfxx
            i += 1
        else:
            df_tops = df_tops.join(dfxx)

    ## Fill empty spaces of resulting dataframe and renaming index entries
    df_tops.fillna("-", inplace=True)
    df_tops.index = ["top_" + str(i) for i in range(1, df_tops.shape[0] + 1)]
    print(display(df_tops))
    print("-"*75)
    print("-"*75)
    print()

    return dfx



## Create the data profiling of location/coordinate variables.
def data_profiling_loc(data, loc_vars):
    """
    Create the data profiling of categorical variables.
        args:
            data (Data Frame): project data set.
            date_vars (list): list with date variables names.
        returns:
            -
    """


    ## Craeting new dataframe with date columns and adjusting contents for profiling

    #### Working dataframe
    dfx = data.loc[:, loc_vars]


    ## Conducting data profiling for location features - general description
    print("*********************************")
    print("** General description of data **")
    print("*********************************")

    #### List where the resulting dataframes will be stored for further concatenation
    res_dfs = []

    #### Type of numeric variables
    dfx_dtype = dfx.dtypes.to_frame().T
    dfx_dtype.index = ["dtype"]
    res_dfs.append(dfx_dtype)

    #### Counting missing values
    dfx_notnull = dfx.count().to_frame().T
    dfx_notnull.index = ["notnull_v"]
    res_dfs.append(dfx_notnull)

    #### Counting missing values
    dfx_missing = dfx.isnull().sum().to_frame().T
    dfx_missing.index = ["missing_v"]
    res_dfs.append(dfx_missing)

    #### Concatenating resulting dataframes into one final result
    print(display(pd.concat(res_dfs, axis=0)))


    ## Conducting data profiling for location features - coordinates precision
    print("***************************")
    print("** Coordinates precision **")
    print("***************************")

    #### Initial variables
    tops = 5 #### Number of tops that will be selected
    i = 0 #### Counter to start joining dataframes

    #### Creating new columns with the number of decimals in each coordinate
    coord_cols = ["latitud", "longitud"]

    for cc in coord_cols:
        dfx[cc + "_nd"] = dfx[cc].astype("str").str.split(pat=".")
        dfx[cc + "_nd"] = dfx[cc + "_nd"].apply(lambda x: len(x[1]) if len(x)==2 else None)

        #### Creating dataframe with top entries and count
        dfxx = dfx[cc + "_nd"].value_counts().iloc[:tops].to_frame()
        dfxx.reset_index(drop=False, inplace=True)
        dfxx["part"] = round(dfxx[cc + "_nd"]/dfx[cc + "_nd"].count()*100, 2)
        dfxx.columns = pd.MultiIndex.from_tuples([(cc + "_nd", tag) for tag in ["value", "count", "part_notnull"]])

        #### Joining all the variables in one final dataframe
        if i == 0:
            df_tops = dfxx
            i += 1
        else:
            df_tops = df_tops.join(dfxx)

    ## Fill empty spaces of resulting dataframe and renaming index entries
    df_tops.fillna("-", inplace=True)
    df_tops.index = ["top_" + str(i) for i in range(1, df_tops.shape[0] + 1)]
    print(display(df_tops))
    print("-"*75)
    print("-"*75)
    print()


    return





"------------------------------------------------------------------------------"
#################
## END OF FILE ##
#################
"------------------------------------------------------------------------------"
