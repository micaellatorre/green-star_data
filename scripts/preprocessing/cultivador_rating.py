import pandas as pd

def calculate_cultivador_rating(data):
    """
    Calcula un puntaje para cada cultivador basado en experiencia, número de plantas,
    tipo de cultivador y nivel de educación respecto al cultivo.
    """

    # Mapeo de valores para 'tipoDeCultivador'
    tipo_de_cultivador_map = {
        'Autocultivador': 1,
        'CultivadorSolidario': 2,
        'CultivadorIndustrial': 3
    }
    data['tipoDeCultivador'] = data['tipoDeCultivador'].map(tipo_de_cultivador_map)

    # Mapeo de valores para 'educacionAlRespecto'
    educacion_al_respecto_map = {
        'Ninguna': 0,
        'Autodidacta': 1,
        'Cursos': 2,
        'NivelDeGrado': 3
    }
    data['educacionAlRespecto'] = data['educacionAlRespecto'].map(educacion_al_respecto_map)

    # Normalizamos las variables de entrada
    data['experiencia_normalizada'] = data['experiencia'] / data['experiencia'].max()
    data['plantas_normalizadas'] = data['plantasEnRotacionNro'] / data['plantasEnRotacionNro'].max()
    data['tipo_cultivador_normalizado'] = data['tipoDeCultivador'] / data['tipoDeCultivador'].max()
    data['educacion_normalizada'] = data['educacionAlRespecto'] / data['educacionAlRespecto'].max()
    
    # Asignamos un peso para cada variable (puedes ajustar estos valores)
    experiencia_weight = 0.4
    plantas_weight = 0.2
    tipo_cultivador_weight = 0.2
    educacion_weight = 0.2
    
    # Calculamos el puntaje
    data['cultivador_rating'] = (
        experiencia_weight * data['experiencia_normalizada'] +
        plantas_weight * data['plantas_normalizadas'] +
        tipo_cultivador_weight * data['tipo_cultivador_normalizado'] +
        educacion_weight * data['educacion_normalizada']
    )
    
    # Eliminamos columnas auxiliares utilizadas para el cálculo
    data.drop(
        ['experiencia_normalizada', 'plantas_normalizadas', 'tipo_cultivador_normalizado', 'educacion_normalizada'],
        axis=1,
        inplace=True
    )
    
    return data
