import pandas as pd
import json

def process_geolocation_columns(data):
    """
    Procesa la columna geolocation para extraer latitud y longitud, y elimina columnas innecesarias.
    
    Args:
        data (pd.DataFrame): Dataset con la columna `geolocation` y `placeName`.

    Returns:
        pd.DataFrame: Dataset con nuevas columnas `lat` y `lon`, sin `geolocation` y `placeName`.
    """
    # Extraer latitud y longitud de la columna geolocation
    data['lat'] = data['geolocation'].apply(lambda x: json.loads(x)['lat'] if pd.notna(x) else None)
    data['lon'] = data['geolocation'].apply(lambda x: json.loads(x)['lon'] if pd.notna(x) else None)
    
    # Eliminar columnas geolocation y placeName
    data.drop(columns=['geolocation', 'placeName'], inplace=True)
    
    return data
