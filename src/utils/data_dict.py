## MODULE WITH INFORMATION ABOUT THE FEATURES THAT ARE INCLUDED IN THE DATASET





"------------------------------------------------------------------------------"
##############################
## Data profiling functions ##
##############################


data_dict = {
    "folio": {
        "relevant": False,
        "data_type": "categoric"
    },
    "fecha_creacion": {
        "relevant": False,
        "data_type": "date_and_time"
    },
    "hora_creacion": {
        "relevant": True,
        "data_type": "date_and_time"
    },
    "dia_semana": {
        "relevant": True,
        "data_type": "date_and_time"
    },
    "codigo_cierre": {
        "relevant": True,
        "data_type": "categoric"
    },
    "fecha_cierre": {
        "relevant": False,
        "data_type": "date_and_time"
    },
    "año_cierre": {
        "relevant": False,
        "data_type": "date_and_time"
    },
    "mes_cierre": {
        "relevant": False,
        "data_type": "date_and_time"
    },
    "hora_cierre": {
        "relevant": False,
        "data_type": "date_and_time"
    },
    "delegacion_inicio": {
        "relevant": False,
        "data_type": "categoric"
    },
    "incidente_c4": {
        "relevant": True,
        "data_type": "categoric"
    },
    "latitud": {
        "relevant": False,
        "data_type": "coordenate"
    },
    "longitud": {
        "relevant": False,
        "data_type": "coordenate"
    },
    "clas_con_f_alarma": {
        "relevant": False,
        "data_type": "categoric"
    },
    "tipo_entrada": {
        "relevant": True,
        "data_type": "categoric"
    },
    "delegacion_cierre": {
        "relevant": False,
        "data_type": "categoric"
    },
    "geopoint": {
        "relevant": False,
        "data_type": "coordenate"
    },
    "mes": {
        "relevant": False,
        "data_type": "date_and_time"
    }
}





"------------------------------------------------------------------------------"
#################
## END OF FILE ##
#################
"------------------------------------------------------------------------------"
