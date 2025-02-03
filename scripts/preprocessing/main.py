import pandas as pd
import json
import os
from datetime import datetime

# Import preprocessing functions
from scripts.preprocessing.user_processing import process_user_columns
from scripts.preprocessing.cultivador_rating import calculate_cultivador_rating
from scripts.preprocessing.tipo_de_simulacion import get_tipo_de_simulacion
from scripts.preprocessing.geolocation_processing import process_geolocation_columns
from scripts.preprocessing.dli_calc import calculate_dli
from scripts.preprocessing.var_coding import encode_categorical_vars
from scripts.preprocessing.categorize_yield import categorize_yield
from scripts.preprocessing.dates_transform import transform_dates

def preprocess_data(file_path):
    # Cargar el dataset
    data = pd.read_csv(file_path)

    # 0. Drop not useful columns
    data.drop(columns=['plantasEnRotacion', 'equipo', 'SimulacionId', 'creado', 'modificado', 'GeneticaSeleccionadaId', 'totalCosechado', 'geneticaName', 'cronogramaDeCultivoId'], inplace=True)
    
    # 1. Procesar columnas relacionadas con el usuario
    data = process_user_columns(data)

    # 2. Numerar el tipo de simulación
    data = get_tipo_de_simulacion(data)
 
    # 3. Calcular el puntaje del cultivador
    data = calculate_cultivador_rating(data)

    # 4. Procesar columnas geolocation y placeName
    data = process_geolocation_columns(data)
    
    # 5. Calcular DLI por etapas
    data = calculate_dli(data)

    # 6. Codificar variables categóricas
    data = encode_categorical_vars(data)
    
    # 7. Transformar fechas a características numéricas
    data = transform_dates(data)

    # 8. Categoriazar la variable objetivo
    data = categorize_yield(data)
    
    # 9. Eliminar filas con valores nulos en la variable objetivo
    data.dropna(subset=["cantidadCosechada"], inplace=True)
    
    # 10. Eliminar la columnas que no se usarán
    data.drop(columns=['geneticaSlug', 'ambienteDeCultivo', 'medioDeCultivo', 'metodoDeCultivo', 'tipoDeSimulacion', 'user_id'], inplace=True)
    
    # 11. Eliminar la columna original, ya que ahora usamos one-hot encoding
    data.drop(columns=["cantidadCosechada"], inplace=True)

    # 12. Definir características (X) y nueva variable objetivo (y)
    X = data.drop(columns=["yield_Baja", "yield_Media", "yield_Alta"])
    y = data[["yield_Baja", "yield_Media", "yield_Alta"]]
    
    # Guardar dataset preprocesado
    save_path = "update_direct_path/green-star_data/data/preprocessed/"
    timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M")
    output_file = os.path.join(save_path, f"green-star_preprocessed_{timestamp}.csv")
    os.makedirs(save_path, exist_ok=True)
    data.to_csv(output_file, index=False)
    print(f"Dataset preprocesado guardado en: {output_file}")
    
    return X, y

if __name__ == "__main__":
    file_path = "update_direct_path/green-star_data/data/history/green-star_24_01_2025_15_15.csv"
    X, y = preprocess_data(file_path)
    print("Preprocesamiento completado. X shape:", X.shape, "y shape:", y.shape)
