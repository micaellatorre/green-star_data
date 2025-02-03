import pickle
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Cargar datos y modelos
DATASET_PATH = "update_direct_path/green-star_data/outputs/oversampled/knn/knn_oversampled_20250131_160127.csv"

# Cargar datos
df = pd.read_csv(DATASET_PATH)
target_columns = ["yield_Baja", "yield_Media", "yield_Alta"]

# Convertir one-hot encoding a etiquetas numéricas
y_test = df[target_columns].values.argmax(axis=1)  # Converts [0,1,0] → 1
X_test = df.drop(columns=target_columns)

# Diccionario de modelos
models = {
    "random_forest": "update_direct_path/green-star_data/outputs/trained/random_forest/random_forest.pkl",
    "svm": "update_direct_path/green-star_data/outputs/trained/svm/svm_model.pkl",
    "xgboost": "update_direct_path/green-star_data/outputs/trained/xgboost/xgboost.pkl"
}

# Evaluación de modelos
results = []
for model_name, model_path in models.items():
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    # Predicción
    y_pred = model.predict(X_test)

    # Convertir predicciones one-hot a etiquetas numéricas si es necesario
    if y_pred.ndim > 1:  
        y_pred = y_pred.argmax(axis=1)  

    # Evaluación de métricas
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average="weighted")
    recall = recall_score(y_test, y_pred, average="weighted")
    f1 = f1_score(y_test, y_pred, average="weighted")
    
    results.append([model_name, accuracy, precision, recall, f1])

    # Matriz de confusión
    cm = confusion_matrix(y_test, y_pred, labels=[0, 1, 2])
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["Baja", "Media", "Alta"], yticklabels=["Baja", "Media", "Alta"])
    plt.title(f"Matriz de Confusión - {model_name}")
    plt.xlabel("Predicción")
    plt.ylabel("Real")
    # plt.savefig(f"outputs/figures/confusion_matrix_{model_name}.png")
    plt.show()

# Guardar resultados en un CSV
df_results = pd.DataFrame(results, columns=["Modelo", "Accuracy", "Precision", "Recall", "F1-Score"])
df_results.to_csv("outputs/metrics/model_evaluation.csv", index=False)
