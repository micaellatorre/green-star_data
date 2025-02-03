import pandas as pd
import json

# Configuración para mostrar todas las columnas al imprimir
pd.set_option('display.max_columns', None)

# Cargar el archivo CSV
csv_file = 'strains_data_v5.csv'
df = pd.read_csv(csv_file)

# Mostrar información general sobre las columnas específicas
columns_of_interest = ["growInfo"]

print("Información General de las Columnas Seleccionadas:")
print(df[columns_of_interest].info())

# Mostrar estadísticas resumidas para cada columna seleccionada
print("\nEstadísticas Resumidas de las Columnas Seleccionadas:")
print(df[columns_of_interest].describe(include='all'))

# Mostrar los primeros 10 registros de las columnas seleccionadas
print("\nPrimeros 10 Registros de las Columnas Seleaccionadas:")
print(df[columns_of_interest].head(10))

# Mostrar la distribución de la columna 'growInfo'
print("\nDistribución de la Columna 'growInfo':")
growInfo_distribution = df['growInfo'].value_counts(normalize=True)  # Proporciones de cada categoría
print(growInfo_distribution)

# Contar cuántos valores faltan en la columna 'growInfo'
missing_values = df['growInfo'].isnull().sum()
print(f"\nValores Faltantes en 'growInfo': {missing_values}")

# Opcional: Mostrar porcentaje de valores faltantes
missing_percentage = (missing_values / len(df)) * 100
print(f"\nPorcentaje de Valores Faltantes en 'growInfo': {missing_percentage:.2f}%")
