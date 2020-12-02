

def date_transformation(col, df):
    """
    Conduct relevant transformations to date variables.
        args:
            col (string): name of date column that will be transformed.
            df (dataframe): df that will be transformed.
        returns:
            df (dataframe): resulting df with cleaned date column.
    """
    fechas_inicio = df[col].str.split("/", n=2,expand=True)
    df['dia_inicio'] = fechas_inicio[0]
    df['mes_inicio'] = fechas_inicio[1]
    df['anio_inicio'] = fechas_inicio[2]

    df['anio_inicio'] = df['anio_inicio'].replace(['19'],'2019')
    df['anio_inicio'] = df['anio_inicio'].replace(['18'],'2018')

    cyc_lst = ["dia_inicio", "mes_inicio"]
    for val in cyc_lst:
        cyclic_trasformation(df, val)

    df.drop(['dia_inicio','mes_inicio'], axis=1, inplace=True)

    update_data_created_dict("anio_inicio", relevant=True, data_type="categoric", model_relevant=True)

    return df


def categoric_trasformation(col, df):
    """
    Conduct relevant transformations to categoric variables.
        args:
            col (string): name of categoric column that will be transformed.
            df (dataframe): df that will be transformed.
        returns:
            df (dataframe): resulting df with cleaned categoric column.
    """

    df[col] = df[col].replace(['LLAMADA DEL 911'],'LLAMADA_911_066')
    df[col] = df[col].replace(['LLAMADA DEL 066'],'LLAMADA_911_066')

    return df

def date_transformation(col, df):
    """
    Conduct relevant transformations to date variables.
        args:
            col (string): name of date column that will be transformed.
            df (dataframe): df that will be transformed.
        returns:
            df (dataframe): resulting df with cleaned date column.
    """
    fechas_inicio = df[col].str.split("/", n=2,expand=True)
    df['dia_inicio'] = fechas_inicio[0]
    df['mes_inicio'] = fechas_inicio[1]
    df['anio_inicio'] = fechas_inicio[2]

    df['anio_inicio'] = df['anio_inicio'].replace(['19'],'2019')
    df['anio_inicio'] = df['anio_inicio'].replace(['18'],'2018')

    cyc_lst = ["dia_inicio", "mes_inicio"]
    for val in cyc_lst:
        cyclic_trasformation(df, val)

    df.drop(['dia_inicio','mes_inicio'], axis=1, inplace=True)

    update_data_created_dict("anio_inicio", relevant=True, data_type="categoric", model_relevant=True)

    return df

def hour_transformation(col, df):
    """
    """

    df[col] = pd.to_timedelta(df[col],errors='ignore')
    hora_inicio = df[col].str.split(":", n=2,expand=True)
    df['hora_inicio'] = hora_inicio[0]
    df['min_inicio'] = hora_inicio[1]
    df['hora_inicio'] = round(df['hora_inicio'].apply(lambda x: float(x)),0)

    cyc_lst = ["hora_inicio"]
    for val in cyc_lst:
        cyclic_trasformation(df, val)

    df.drop(['hora_inicio','min_inicio'], axis=1, inplace=True)

    return df


def cyclic_trasformation(df, col):
    """
    Conduct relevant cyclical hour transformations to cos and sin coordinates.
        args:
            col (string): name of  column that will be transformed into cyclical hr.
            df (dataframe): df that will be transformed.
        returns:
            df (dataframe): resulting df with cyclical column.
    """


    ## Specifying divisors related to time.
    if "hora" in col:
        div=24
    elif "dia" in col:
        div= 30.4
    elif "mes" in col:
        div=12

    ## Creating cyclical variables.
    df[col + '_sin'] = np.sin(2*np.pi*df[col].apply(lambda x: float(x))/div)
    df[col + '_cos'] = np.cos(2*np.pi*df[col].apply(lambda x: float(x))/div)


    ## Updating data creation dictionary to include cyclical features.
    update_data_created_dict(col + "_sin", relevant=True, data_type="numeric", model_relevant=True)
    update_data_created_dict(col + "_cos", relevant=True, data_type="numeric", model_relevant=True)



    return df