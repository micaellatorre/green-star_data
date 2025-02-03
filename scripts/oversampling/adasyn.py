import pandas as pd
from imblearn.over_sampling import ADASYN

def adasyn_oversampling(X, y, random_state=42):
    """
    Aplica ADASYN para generar nuevas muestras de clases minoritarias.
    
    Parameters:
        X (pd.DataFrame): Conjunto de características.
        y (pd.DataFrame): Variable objetivo en formato one-hot.
        random_state (int): Semilla para reproducibilidad.

    Returns:
        X_resampled (pd.DataFrame), y_resampled (pd.DataFrame)
    """
    adasyn = ADASYN(random_state=random_state)
    y_categorical = y.idxmax(axis=1)
    X_resampled, y_resampled_categorical = adasyn.fit_resample(X, y_categorical)
    y_resampled = pd.get_dummies(y_resampled_categorical, dtype=int)
    return X_resampled, y_resampled
