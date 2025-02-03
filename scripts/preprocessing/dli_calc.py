import pandas as pd
from datetime import datetime, timedelta

def calculate_dli(data):
    """
    Calcula el DLI (Daily Light Integral) acumulado para cada etapa del ciclo de cultivo,
    basado en las fechas de inicio y las tablas de fotoperiodo.

    Parameters:
        data (DataFrame): DataFrame con la información del ciclo de cultivo.

    Returns:
        DataFrame: DataFrame con los valores de DLI acumulados por etapa y totales.
    """

    # Paths de las tablas de fotoperiodo
    photoperiod_path = "update_direct_path/green-star_data/bases/photoperiod/photoperiod.csv"
    auto_path = "update_direct_path/green-star_data/bases/photoperiod/auto.csv"
    hybrid_path = "update_direct_path/green-star_data/bases/photoperiod/hybrid.csv"

    # Cargar tablas de fotoperiodo
    photoperiod_data = pd.read_csv(photoperiod_path)
    auto_data = pd.read_csv(auto_path)
    hybrid_data = pd.read_csv(hybrid_path)

    # Mapeo para seleccionar la tabla según "geneticaPhoto"
    genetica_map = {
        "Photoperiod": photoperiod_data,
        "Auto": auto_data,
        "Hybrid": hybrid_data
    }

    def get_photo_range(date, cultivation_dates):
        """
        Determina el rango de fotoperiodo correspondiente para una fecha y ciclo de cultivo.

        Parameters:
            date (datetime): Fecha actual a evaluar.
            cultivation_dates (list): Lista de fechas de inicio y fin de cada etapa del ciclo.

        Returns:
            str: Rango de fotoperiodo correspondiente (de 1 a 15).
        """
        # Calcular duraciones y divisiones de las etapas Vegetativo, Prefloración y Floración
        vegetativo_duration = (cultivation_dates[2]["endDate"] - cultivation_dates[2]["startDate"]).days
        vegetativo_5th = vegetativo_duration / 5
        vegetativo_limits = [
            cultivation_dates[2]["startDate"] + timedelta(days=i * vegetativo_5th)
            for i in range(1, 5)
        ]

        preflora_duration = (cultivation_dates[3]["endDate"] - cultivation_dates[3]["startDate"]).days
        preflora_3rd = preflora_duration / 3
        preflora_limits = [
            cultivation_dates[3]["startDate"] + timedelta(days=i * preflora_3rd)
            for i in range(1, 3)
        ]

        floracion_duration = (cultivation_dates[4]["endDate"] - cultivation_dates[4]["startDate"]).days
        floracion_5th = floracion_duration / 5
        floracion_limits = [
            cultivation_dates[4]["startDate"] + timedelta(days=i * floracion_5th)
            for i in range(1, 5)
        ]

        # Determinar el rango basado en las fechas
        if date < cultivation_dates[1]["startDate"]:
            return "1"  # Germinación
        if date < cultivation_dates[2]["startDate"]:
            return "2"  # Plantín
        for i, limit in enumerate(vegetativo_limits):
            if date < limit:
                return str(3 + i)
        if date < cultivation_dates[2]["endDate"]:
            return "7"
        for i, limit in enumerate(preflora_limits):
            if date < limit:
                return str(8 + i)
        if date < cultivation_dates[3]["endDate"]:
            return "10"
        for i, limit in enumerate(floracion_limits):
            if date < limit:
                return str(11 + i)
        if date < cultivation_dates[4]["endDate"]:
            return "15"
        return ""

    # Iterar sobre cada fila del DataFrame
    for index, row in data.iterrows():
        # Obtener la tabla de fotoperiodo correspondiente
        photoperiod_table = genetica_map[row["geneticaPhoto"]]

        # Preparar las fechas de cultivo
        cultivation_dates = [
            {"startDate": datetime.strptime(row["inicioGerminacionClonacion"], "%Y-%m-%dT%H:%M:%S.%fZ"),
            "endDate": datetime.strptime(row["inicioPlantin"], "%Y-%m-%dT%H:%M:%S.%fZ")},
            {"startDate": datetime.strptime(row["inicioPlantin"], "%Y-%m-%dT%H:%M:%S.%fZ"),
            "endDate": datetime.strptime(row["inicioVegetativo"], "%Y-%m-%dT%H:%M:%S.%fZ")},
            {"startDate": datetime.strptime(row["inicioVegetativo"], "%Y-%m-%dT%H:%M:%S.%fZ"),
            "endDate": datetime.strptime(row["inicioPreFloracion"], "%Y-%m-%dT%H:%M:%S.%fZ")},
            {"startDate": datetime.strptime(row["inicioPreFloracion"], "%Y-%m-%dT%H:%M:%S.%fZ"),
            "endDate": datetime.strptime(row["inicioFloracion"], "%Y-%m-%dT%H:%M:%S.%fZ")},
            {"startDate": datetime.strptime(row["inicioFloracion"], "%Y-%m-%dT%H:%M:%S.%fZ"),
            "endDate": datetime.strptime(row["cosecha"], "%Y-%m-%dT%H:%M:%S.%fZ")}
        ]

        # Inicializar acumuladores de DLI por etapa
        dli_etapas = {
            "DLIGerminacionClonacion": 0,
            "DLIPlantin": 0,
            "DLIVegetativo": 0,
            "DLIPreFloracion": 0,
            "DLIFloracion": 0,
        }

        # Calcular DLI acumulado para cada etapa
        for etapa, fechas in enumerate(cultivation_dates):
            dias_etapa = (fechas["endDate"] - fechas["startDate"]).days

            for dia in range(dias_etapa):
                fecha_actual = fechas["startDate"] + timedelta(days=dia)

                # Determinar el rango de fotoperiodo
                range_index = get_photo_range(fecha_actual, cultivation_dates)

                # Obtener DLI diario de la tabla
                dli_diario = photoperiod_table.loc[int(range_index) - 1, "DLI"]

                # Asignar al acumulador correspondiente
                etapa_nombre = list(dli_etapas.keys())[etapa]
                dli_etapas[etapa_nombre] += dli_diario

        # Agregar resultados al DataFrame
        data.loc[index, "DLITotal"] = sum(dli_etapas.values())
        for etapa, valor in dli_etapas.items():
            data.loc[index, etapa] = valor

    return data

