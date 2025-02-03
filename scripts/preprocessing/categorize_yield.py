import pandas as pd

def categorize_yield(data):
    """
    Categoriza la variable `cantidadCosechada` en intervalos y asigna etiquetas.

    Args:
        data (pd.DataFrame): Dataset con la columna `cantidadCosechada`.

    Returns:
        pd.DataFrame: Dataset con la nueva columna `cantidadCosechada_clasificada`.
    """
    """
    Definir bins basados en la distribución observada
    Con la siguiente distribucion
    """
    bins = [0, 20, 40, float("inf")]
    labels = ["Baja", "Media", "Alta"]

    # Crear columna categórica
    data["cantidadCosechada_clasificada"] = pd.cut(data["cantidadCosechada"], bins=bins, labels=labels, right=False)

    # Aplicar one-hot encoding
    data = pd.get_dummies(data, columns=["cantidadCosechada_clasificada"], prefix="yield", dtype=int)

    return data