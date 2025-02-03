import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.cluster import KMeans

def cluster_based_oversampling(X, y, n_clusters=5, random_state=42):
    """
    Aplica Cluster-Based Oversampling dividiendo los datos en clusters antes de aplicar SMOTE.

    Parameters:
        X (pd.DataFrame): Conjunto de características.
        y (pd.DataFrame): Variable objetivo en formato one-hot.
        n_clusters (int): Número de clusters a crear antes del oversampling.
        random_state (int): Semilla para reproducibilidad.

    Returns:
        X_resampled (pd.DataFrame), y_resampled (pd.DataFrame)
    """
    # Agrupar datos en clusters
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=10)
    clusters = kmeans.fit_predict(X)
    
    X["cluster"] = clusters
    y_categorical = y.idxmax(axis=1)

    smote = SMOTE(random_state=random_state)
    X_resampled, y_resampled_categorical = smote.fit_resample(X, y_categorical)

    X_resampled = X_resampled.drop(columns=["cluster"], errors="ignore")
    y_resampled = pd.get_dummies(y_resampled_categorical, dtype=int)
    
    return X_resampled, y_resampled
