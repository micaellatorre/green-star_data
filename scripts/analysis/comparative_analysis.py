import os
import pandas as pd
import numpy as np
import glob
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report

# Ruta base donde están los datasets sobremuestreados
BASE_PATH = "update_direct_path/green-star_data/outputs/oversampled"

# Métodos de oversampling usados
methods = ["random", "smote", "adasyn", "cluster", "knn"]

# Almacenar resultados de cada método
results = []

for method in methods:
    print(f"\nEvaluando {method}...")

    # Buscar archivo más reciente para cada método
    files = glob.glob(os.path.join(BASE_PATH, method, f"{method}_oversampled_*.csv"))
    if not files:
        print(f"No se encontraron archivos para {method}")
        continue
    latest_file = max(files, key=os.path.getctime)  # Selecciona el más reciente

    # Cargar dataset
    df = pd.read_csv(latest_file)
    
    # Separar características (X) y variable objetivo (y) en formato one-hot
    target_columns = ["yield_Baja", "yield_Media", "yield_Alta"]
    X = df.drop(columns=target_columns)  
    y = df[target_columns]

    # Dividir en train y test (80-20)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

    # Entrenar modelo multi-clase con OneVsRest
    model = OneVsRestClassifier(RandomForestClassifier(n_estimators=100, random_state=42))
    model.fit(X_train, y_train)

    # Predicciones en train y test
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    # Evaluar desempeño
    train_acc = accuracy_score(y_train, y_train_pred)
    test_acc = accuracy_score(y_test, y_test_pred)
    f1 = f1_score(y_test, y_test_pred, average="weighted")
    overfit_ratio = train_acc / test_acc  # Medida de sobreajuste

    # Guardar resultados
    results.append({
        "Método": method,
        "Accuracy (Test)": round(test_acc, 4),
        "F1-score": round(f1, 4),
        "Overfitting Ratio": round(overfit_ratio, 4)
    })

    # Imprimir reporte de clasificación
    print(f"\nReporte para {method}:\n")
    print(classification_report(y_test, y_test_pred, target_names=target_columns))

# Crear DataFrame con resultados
df_results = pd.DataFrame(results)
print("\n📊 Resumen Comparativo de Oversampling:")
print(df_results.sort_values(by="F1-score", ascending=False))
