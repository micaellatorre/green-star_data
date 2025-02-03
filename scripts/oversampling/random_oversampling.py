import pandas as pd
from imblearn.over_sampling import RandomOverSampler

def random_oversampling(X, y, random_state=42):
    """
    Aplica Random Oversampling a los datos.
    
    Parameters:
        X (pd.DataFrame): Conjunto de características.
        y (pd.DataFrame): Variable objetivo en formato one-hot.
        random_state (int): Semilla para reproducibilidad.

    Returns:
        X_resampled (pd.DataFrame), y_resampled (pd.DataFrame) (en formato one-hot)
    """
    ros = RandomOverSampler(random_state=random_state)
    
    # Convertir one-hot encoding a una sola columna categórica
    y_categorical = y.idxmax(axis=1)
    
    # Aplicar oversampling
    X_resampled, y_resampled_categorical = ros.fit_resample(X, y_categorical)

    # Convertir de nuevo a one-hot encoding
    y_resampled = pd.get_dummies(y_resampled_categorical, dtype=int)

    return X_resampled, y_resampled
