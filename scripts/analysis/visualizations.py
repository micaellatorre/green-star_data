import pandas as pd
import matplotlib.pyplot as plt

# Cargar resultados
df_results = pd.read_csv("update_direct_path/green-star_data/outputs/metrics/model_evaluation.csv")

# Gráfico de comparación de métricas
metrics = ["Accuracy", "Precision", "Recall", "F1-Score"]
colors = ["blue", "green", "red", "purple"]

plt.figure(figsize=(10, 5))
for metric, color in zip(metrics, colors):
    plt.plot(df_results["Modelo"], df_results[metric], marker="o", linestyle="-", label=metric, color=color)

plt.xlabel("Modelos")
plt.ylabel("Puntuación")
plt.title("Comparación de Métricas de Modelos")
plt.legend()
plt.savefig("outputs/figures/model_comparison.png")
plt.show()
