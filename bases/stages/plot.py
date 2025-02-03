import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "growth_stages.csv"  # Replace with your actual file path
data = pd.read_csv(file_path)

# Define custom colors for each stage
colors = ['#CE9000', '#CE9000', '#EBCF1B', '#BDCE00', '#A4D210', '#76C700']

# Function to add bar values on top
def add_bar_values(bars, values):
    for bar, value in zip(bars, values):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            0.05,
            f'{value:.2f}', 
            ha='center', 
            va='bottom', 
            fontsize=9
        )

# 1. Plot for Photoperiodic stages
plt.figure(figsize=(12, 6))
bars = plt.bar(
    x=data['Stages'],
    height=data['Week_Avg_Photo'],
    yerr=data['Max_Photo'] - data['Min_Photo'],  # Error bars based on Max and Min
    color=colors,
    capsize=5,
    alpha=0.9,
    # label="Fotoperiódicas (Semanas Prom.)"
)
add_bar_values(bars, data['Week_Avg_Photo'])  # Add bar values

# Customize the graph
plt.title("Etapas del Cultivo de Cannabis Fotoperiódicas", fontsize=16)
plt.xlabel("Etapas", fontsize=12)
plt.ylabel("Semanas", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
# plt.legend(loc="upper left")
plt.show()

# 2. Plot for Autoflowering stages
plt.figure(figsize=(12, 6))
bars = plt.bar(
    x=data['Stages'],
    height=data['Week_Avg_Auto'],
    yerr=data['Max_Auto'] - data['Min_Auto'],  # Error bars based on Max and Min
    color=colors,
    capsize=5,
    alpha=0.9,
    # label="Autoflorecientes (Semanas Prom.)"
)
add_bar_values(bars, data['Week_Avg_Auto'])  # Add bar values

# Customize the graph
plt.title("Etapas del Cultivo de Cannabis Autoflorecientes", fontsize=16)
plt.xlabel("Etapas", fontsize=12)
plt.ylabel("Semanas", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
# plt.legend(loc="upper left")
plt.show()
