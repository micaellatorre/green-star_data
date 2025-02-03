import pandas as pd

def transform_dates(data):
    """
    Convierte las fechas de inicio de cada etapa del cultivo en la duración en días
    (posiblemente con valores decimales) y calcula el total de días del ciclo.
    """

    # Columnas de fechas
    date_columns = [
        "inicioGerminacionClonacion",
        "inicioPlantin",
        "inicioVegetativo",
        "inicioPreFloracion",
        "inicioFloracion",
        "cosecha"
    ]
    
    # Convertir las columnas de fechas a formato datetime
    for col in date_columns:
        data[col] = pd.to_datetime(data[col])

    # Crear columnas para la duración en días de cada etapa
    data["dias_germinacion_clonacion"] = (data["inicioPlantin"] - data["inicioGerminacionClonacion"]).dt.total_seconds() / 86400
    data["dias_plantin"] = (data["inicioVegetativo"] - data["inicioPlantin"]).dt.total_seconds() / 86400
    data["dias_vegetativo"] = (data["inicioPreFloracion"] - data["inicioVegetativo"]).dt.total_seconds() / 86400
    data["dias_prefloracion"] = (data["inicioFloracion"] - data["inicioPreFloracion"]).dt.total_seconds() / 86400
    data["dias_floracion"] = (data["cosecha"] - data["inicioFloracion"]).dt.total_seconds() / 86400

    # Calcular el total de días del cultivo
    data["total_dias_cultivo"] = (
        data["dias_germinacion_clonacion"] +
        data["dias_plantin"] +
        data["dias_vegetativo"] +
        data["dias_prefloracion"] +
        data["dias_floracion"]
    )

    # Eliminar las columnas de fechas originales
    data.drop(columns=date_columns, inplace=True)

    return data
