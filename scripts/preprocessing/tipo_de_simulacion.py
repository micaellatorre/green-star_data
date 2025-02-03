import pandas as pd

def get_tipo_de_simulacion(data):
    """
    Mapeo de valores para 'tipoDeSimulacion'
    """

    # Mapeo de valores para 'tipoDeSimulacion'
    tipo_de_simulacion_map = {
        'Historia': 1,
        'Alter': 2,
        'Presagio': 3
    }
    data['tipoDeSimulacion'] = data['tipoDeSimulacion'].map(tipo_de_simulacion_map)
    
    return data
