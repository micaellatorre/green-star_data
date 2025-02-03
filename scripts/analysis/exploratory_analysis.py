import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar datos procesados
data = pd.read_csv("data/processed_dataset.csv")  # Ajusta la ruta según corresponda

# Mapa de calor de correlaciones
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Mapa de Calor de Correlaciones")
plt.savefig("outputs/analysis/correlation_heatmap.png")
plt.show()

# Distribuciones de las variables más relevantes
features_to_plot = ['feature1', 'feature2', 'feature3']  # Ajusta según tu dataset

for feature in features_to_plot:
    plt.figure(figsize=(6, 4))
    sns.histplot(data[feature], kde=True, bins=20)
    plt.title(f"Distribución de {feature}")
    plt.savefig(f"outputs/analysis/distribution_{feature}.png")
    plt.show()
