from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import numpy as np

def train_model(X_smote, y_smote):
    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X_smote, y_smote, test_size=0.2, random_state=42)

    # Instanciar y entrenar el modelo
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Realizar predicciones
    y_pred = model.predict(X_test)

    # Calcular métricas de evaluación
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Error Cuadrático Medio (MSE): {mse:.2f}")
    print(f"R²: {r2:.2f}")

    # Usar validación cruzada para evaluar el modelo
    cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='r2')
    print(f"R² promedio (validación cruzada): {np.mean(cv_scores):.2f}")

if __name__ == "__main__":
    # Cargar los datos balanceados desde archivos (generados por smote_augmentation.py)
    X_smote = pd.read_csv("balanced_X.csv").values
    y_smote = pd.read_csv("balanced_y.csv")["target"].values

    train_model(X_smote, y_smote)
