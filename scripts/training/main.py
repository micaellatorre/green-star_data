import os
import pandas as pd

from scripts.training.random_forest import train_random_forest
from scripts.training.svm import train_svm
from scripts.training.xgboost import train_xgboost

# Definir la ruta de los datos procesados
DATASET_PATH = "update_direct_path/green-star_data/outputs/oversampled/knn/knn_oversampled_20250131_160127.csv"
OUTPUT_BASE_DIR = "update_direct_path/green-star_data/outputs/trained"

# Cargar datos
df = pd.read_csv(DATASET_PATH)
target_columns = ["yield_Baja", "yield_Media", "yield_Alta"]
X = df.drop(columns=target_columns)
y = df[target_columns]

# Ejecutar entrenamientos
results = {}

for model_name, train_func in zip(
    ["random_forest", "svm", "xgboost"],
    [train_random_forest, train_svm, train_xgboost]
):
    print(f"\nEntrenando {model_name}...")
    model_output_dir = os.path.join(OUTPUT_BASE_DIR, model_name)
    accuracy, f1 = train_func(X, y, model_output_dir)
    results[model_name] = {"Accuracy": accuracy, "F1-score": f1}

# Mostrar resultados finales
print("\n📊 Resultados Finales:")
for model, metrics in results.items():
    print(f"{model}: Accuracy: {metrics['Accuracy']:.4f}, F1-score: {metrics['F1-score']:.4f}")
