import pickle
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos y modelos
DATASET_PATH = "update_direct_path/green-star_data/outputs/oversampled/knn/knn_oversampled_20250131_160127.csv"

# Cargar datos
df = pd.read_csv(DATASET_PATH)
target_columns = ["yield_Baja", "yield_Media", "yield_Alta"]
X_train = df.drop(columns=target_columns)
features = X_train.columns

models = {
"random_forest": "update_direct_path/green-star_data/outputs/trained/random_forest/random_forest.pkl",
"xgboost": "update_direct_path/green-star_data/outputs/trained/xgboost/xgboost.pkl"
}
    # "svm": "update_direct_path/green-star_data/outputs/trained/svm/svm_model.pkl",

# Graficar importancia de características
for model_name, model_path in models.items():
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    importances = model.feature_importances_
    feature_importance_df = pd.DataFrame({"Feature": features, "Importance": importances})
    feature_importance_df = feature_importance_df.sort_values(by="Importance", ascending=False)

    plt.figure(figsize=(8, 5))
    plt.barh(feature_importance_df["Feature"], feature_importance_df["Importance"], color="skyblue")
    plt.xlabel("Importancia")
    plt.ylabel("Características")
    plt.title(f"Importancia de Características - {model_name}")
    plt.savefig(f"outputs/figures/feature_importance_{model_name}.png")
    plt.show()
