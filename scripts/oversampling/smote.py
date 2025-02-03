import pandas as pd
from imblearn.over_sampling import SMOTE

def smote_oversampling(X, y, random_state=42):
    """
    Aplica SMOTE (Synthetic Minority Over-sampling Technique).
    
    Parameters:
        X (pd.DataFrame): Conjunto de características.
        y (pd.DataFrame): Variable objetivo en formato one-hot.
        random_state (int): Semilla para reproducibilidad.

    Returns:
        X_resampled (pd.DataFrame), y_resampled (pd.DataFrame)
    """
    smote = SMOTE(random_state=random_state)
    y_categorical = y.idxmax(axis=1)
    X_resampled, y_resampled_categorical = smote.fit_resample(X, y_categorical)
    y_resampled = pd.get_dummies(y_resampled_categorical, dtype=int)
    return X_resampled, y_resampled
