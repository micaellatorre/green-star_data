import os
import pandas as pd
from datetime import datetime
import numpy as np

# Import functions from oversampling modules
from scripts.oversampling.random_oversampling import random_oversampling
from scripts.oversampling.smote import smote_oversampling
from scripts.oversampling.adasyn import adasyn_oversampling
from scripts.oversampling.cluster_based import cluster_based_oversampling
from scripts.oversampling.knn_interpolation import knn_interpolation_oversampling

# Import preprocess_data function from preprocessing/main.py
from scripts.preprocessing.main import preprocess_data

def guardar_resultados(X_resampled, y_resampled, output_dir, technique_name):
    """
    Guarda los resultados del oversampling en un archivo CSV.

    Parameters:
        X_resampled (pd.DataFrame): Conjunto de características sobremuestreadas.
        y_resampled (pd.Series): Variable objetivo sobremuestreada.
        output_dir (str): Ruta del directorio de salida.
        technique_name (str): Nombre de la técnica de oversampling utilizada.
    """
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(output_dir, f"{technique_name}_oversampled_{timestamp}.csv")

    # Crear DataFrame y guardar
    # result_df = pd.concat([pd.DataFrame(X_resampled), pd.Series(y_resampled, name="target")], axis=1)
    result_df = pd.concat([pd.DataFrame(X_resampled), y_resampled], axis=1)
    result_df.to_csv(output_path, index=False)
    print(f"Resultados guardados con {technique_name} en: {output_path}")


if __name__ == "__main__":
    preprocessed = True

    # Ruta del dataset preprocesado (Actualizar según corresponda)
    file_path = ".../green-star_data/data/preprocessed/green-star_preprocessed_example.csv"

    # Ruta del dataset original
    # file_path = ".../green-star_data/data/history/green-star_example.csv"

    # Paso 1: Preprocesar los datos si no se han preprocesado

    if not preprocessed:
        # Preprocesar los datos
        print("Iniciando preprocesamiento...")
        X, y = preprocess_data(file_path)
        print(f"Preprocesamiento completado. X shape: {X.shape}, y shape: {y.shape}")
    else:
        # Cargar dataset preprocesado
        data = pd.read_csv(file_path)
        X = data.drop(columns=["yield_Baja", "yield_Media", "yield_Alta"])
        y = data[["yield_Baja", "yield_Media", "yield_Alta"]]

    # Semilla para reproducibilidad
    seed_value = 420
    np.random.seed(seed_value)

    # Definir directorio base de salida
    output_base_dir = "update_direct_path/green-star_data/outputs/oversampled"

    # Paso 2: Aplicar técnicas de oversampling

    # 1. Random Oversampling
    print("Ejecutando Random Oversampling...")
    X_res_rand, y_res_rand = random_oversampling(X, y, random_state=seed_value)
    guardar_resultados(X_res_rand, y_res_rand, os.path.join(output_base_dir, "random"), "random")

    # 2. SMOTE Tradicional
    print("Ejecutando SMOTE...")
    X_res, y_res = smote_oversampling(X, y, random_state=seed_value)
    guardar_resultados(X_res, y_res, os.path.join(output_base_dir, "smote"), "smote")

    # 3. ADASYN
    print("Ejecutando ADASYN...")
    X_res, y_res = adasyn_oversampling(X, y, random_state=seed_value)
    guardar_resultados(X_res, y_res, os.path.join(output_base_dir, "adasyn"), "adasyn")

    # 4. Cluster-Based Oversampling
    print("Ejecutando Cluster-Based Oversampling...")
    X_res, y_res = cluster_based_oversampling(X, y, n_clusters=5, random_state=seed_value)
    guardar_resultados(X_res, y_res, os.path.join(output_base_dir, "cluster"), "cluster")

    # 5. KNN Interpolation
    print("Ejecutando KNN Interpolation...")
    X_res, y_res = knn_interpolation_oversampling(X, y, n_neighbors=3)
    guardar_resultados(X_res, y_res, os.path.join(output_base_dir, "knn"), "knn")


    print("Todas las técnicas de sobremuestreo se han ejecutado y guardado correctamente.")
