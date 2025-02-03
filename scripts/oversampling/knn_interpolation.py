import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors

def knn_interpolation_oversampling(X: pd.DataFrame, y: pd.DataFrame, n_neighbors: int = 5):
    """
    Aplica interpolación con KNN para generar nuevas muestras sintéticas.

    Parameters:
        X (pd.DataFrame): Conjunto de características.
        y (pd.DataFrame): Variable objetivo en formato one-hot.
        n_neighbors (int): Número de vecinos a considerar.

    Returns:
        X_resampled (pd.DataFrame), y_resampled (pd.DataFrame)
    """
    if X.empty or y.empty:
        raise ValueError("X e y no pueden estar vacíos.")

    if len(X) != len(y):
        raise ValueError("X e y deben tener el mismo número de filas.")

    # Convertir a NumPy para eficiencia
    X_np = X.to_numpy()
    y_np = y.to_numpy()

    nn = NearestNeighbors(n_neighbors=min(n_neighbors + 1, len(X)))
    nn.fit(X_np)

    # Generar nuevas muestras interpoladas
    new_samples = []
    new_labels = []

    for i in range(len(X_np)):
        neighbors = nn.kneighbors([X_np[i]], return_distance=False)[0][1:]  # Omitimos el propio punto
        for neighbor in neighbors:
            interpolated_sample = (X_np[i] + X_np[neighbor]) / 2
            new_samples.append(interpolated_sample)
            new_labels.append(y_np[i])  # Mantiene la misma clase

    # Convertir nuevamente a DataFrame
    X_resampled = pd.concat([X, pd.DataFrame(new_samples, columns=X.columns)], ignore_index=True)
    y_resampled = pd.concat([y, pd.DataFrame(new_labels, columns=y.columns)], ignore_index=True)
    
    return X_resampled, y_resampled
