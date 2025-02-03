import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Ruta del dataset y modelo entrenado
DATASET_PATH = "update_direct_path/green-star_data/outputs/oversampled/knn/knn_oversampled_20250131_160127.csv"
SVM_MODEL_PATH = "update_direct_path/green-star_data/outputs/trained/svm/svm_model.pkl"

# Cargar datos
df = pd.read_csv(DATASET_PATH)

# Definir columnas objetivo
target_columns = ["yield_Baja", "yield_Media", "yield_Alta"]
X_train = df.drop(columns=target_columns)
features = X_train.columns

# Cargar modelo SVM entrenado
with open(SVM_MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# Verificar si el modelo tiene coeficientes (solo aplica para kernel lineal)
if hasattr(model, "coef_"):
    importances = np.abs(model.coef_).mean(axis=0)  # Tomar el valor absoluto promedio en caso de multiclase
    feature_importance_df = pd.DataFrame({"Feature": features, "Importance": importances})
    feature_importance_df = feature_importance_df.sort_values(by="Importance", ascending=False)

    # Graficar importancia de características
    plt.figure(figsize=(8, 5))
    plt.barh(feature_importance_df["Feature"], feature_importance_df["Importance"], color="skyblue")
    plt.xlabel("Importancia")
    plt.ylabel("Características")
    plt.title("Importancia de Características - SVM (Kernel Lineal)")
    # plt.gca().invert_yaxis()  # Invertir para que la más importante esté arriba
    plt.savefig(f"outputs/figures/feature_importance_svm.png")
    plt.show()

else:
    print("El modelo SVM no tiene coeficientes disponibles. Esto puede deberse a que no se usó un kernel lineal.")
