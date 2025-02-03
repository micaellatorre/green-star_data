import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

# Cargar el CSV
df = pd.read_csv('strains_data_app_v3.csv')

# Analisis de Slug
def analyze_slug_column(df):
    if 'slug' in df.columns:
        print("\nAnálisis de la columna 'slug':")
        
        # Extraer prefijos y sufijos basados en el separador "-"
        df['slug_prefix'] = df['slug'].str.split('-').str[0]
        df['slug_suffix'] = df['slug'].str.split('-').str[-1]
        
        # Análisis de prefijos
        print("\nDistribución de prefijos:")
        print(df['slug_prefix'].value_counts())
        
        # Análisis de sufijos
        print("\nDistribución de sufijos:")
        print(df['slug_suffix'].value_counts())
        
        # Graficar prefijos y sufijos
        for col in ['slug_prefix', 'slug_suffix']:
            plt.figure(figsize=(10, 6))
            sns.countplot(data=df, y=col, order=df[col].value_counts().iloc[:10].index, palette='viridis')
            plt.title(f'Distribución de los {col}')
            plt.ylabel(col)
            plt.xlabel('Frecuencia')
            plt.show()

# Analisis de Name
def analyze_name_column(df):
    if 'name' in df.columns:
        print("\nAnálisis de la columna 'name':")
        
        # Longitud de los nombres
        df['name_length'] = df['name'].str.len()
        print("\nEstadísticas sobre la longitud de los nombres:")
        print(df['name_length'].describe())
        
        # Cantidad de palabras en los nombres
        df['name_word_count'] = df['name'].str.split().str.len()
        print("\nEstadísticas sobre la cantidad de palabras en los nombres:")
        print(df['name_word_count'].describe())
        
        # Frecuencia de palabras
        words = df['name'].str.split(expand=True).stack().value_counts()
        print("\nPalabras más frecuentes en los nombres:")
        print(words.head(10))
        
        # Graficar la distribución de la longitud de los nombres
        plt.figure(figsize=(8, 6))
        sns.histplot(df['name_length'], bins=30, kde=True, color='blue')
        plt.title('Distribución de la longitud de los nombres')
        plt.xlabel('Longitud')
        plt.ylabel('Frecuencia')
        plt.show()

# Analisis de Parents y Children
def analyze_parents_children_columns(df):
    for col in ['parents', 'children']:
        if col in df.columns:
            print(f"\nAnálisis de la columna '{col}':")
            
            # Parsear la columna JSON
            parsed_column = parse_json_column(df[col])
            
            # Extraer la cantidad de elementos en cada lista
            df[f'{col}_count'] = parsed_column.apply(len)
            print(f"\nDistribución de la cantidad de elementos en '{col}':")
            print(df[f'{col}_count'].value_counts())
            
            # Descomponer las listas JSON en DataFrame para analizar propiedades internas
            expanded_df = pd.json_normalize(parsed_column.explode())
            if not expanded_df.empty:
                print(f"\nPropiedades más comunes en los objetos de '{col}':")
                print(expanded_df.columns)
                print(expanded_df.describe(include='all'))
                
                # Graficar las cantidades de elementos
                plt.figure(figsize=(8, 6))
                sns.histplot(df[f'{col}_count'], bins=20, kde=True, color='green')
                plt.title(f'Distribución de la cantidad de elementos en {col}')
                plt.xlabel('Cantidad de elementos')
                plt.ylabel('Frecuencia')
                plt.show()

# Analisis Description Plain
def analyze_description_plain(df):
    if 'descriptionPlain' in df.columns:
        print("\nAnálisis de la columna 'descriptionPlain':")
        
        # Longitud de las descripciones
        df['description_length'] = df['descriptionPlain'].str.len()
        print("\nEstadísticas sobre la longitud de las descripciones:")
        print(df['description_length'].describe())
        
        # Frecuencia de palabras
        words = df['descriptionPlain'].str.split(expand=True).stack().value_counts()
        print("\nPalabras más frecuentes en las descripciones:")
        print(words.head(10))
        
        # Graficar la distribución de la longitud de las descripciones
        plt.figure(figsize=(8, 6))
        sns.histplot(df['description_length'], bins=30, kde=True, color='purple')
        plt.title('Distribución de la longitud de las descripciones')
        plt.xlabel('Longitud')
        plt.ylabel('Frecuencia')
        plt.show()

# Function to parse JSON columns safely
def parse_json_column(column):
    def safe_json_load(x):
        if isinstance(x, str):  # Only process string values
            try:
                # Replace single quotes with double quotes and attempt to parse
                return json.loads(x.replace("'", '"'))
            except json.JSONDecodeError:
                # Return an empty dictionary for invalid JSON
                return {}
        return {}  # Return an empty dictionary for non-strings
    return column.apply(safe_json_load)

def analyze_general_statistics(df):
    print("Estadísticas descriptivas de las columnas numéricas:")
    print(df.describe())
    print("\nDistribución de columnas categóricas:")
    print(df.describe(include=['object']))

# Análisis de distribución de categorías con porcentajes
def analyze_distribution_phenotype(df):
    # Columnas categóricas relevantes para el análisis
    categorical_columns = ['phenotype']
    
    for col in categorical_columns:
        print(f"\nDistribución del Fenotipo Dominante:")
        
        # Calcular valores absolutos y porcentajes
        value_counts = df[col].value_counts()
        percentages = df[col].value_counts(normalize=True) * 100
        
        # Combinar en un solo DataFrame para mayor claridad
        distribution_df = pd.DataFrame({
            'Count': value_counts,
            'Percentage (%)': percentages
        })
        print(distribution_df)
        
        # Graficar la distribución
        plt.figure(figsize=(8, 6))
        ax = sns.barplot(x=distribution_df.index, y=distribution_df['Count'], palette='viridis')
        plt.title(f'Distribución del Fenotipo Dominante')
        plt.xlabel('Fenotipo')
        plt.ylabel('Cantidad de Genéticas')
        plt.xticks(rotation=45)
        
        # Agregar valores encima de las barras
        for i, bar in enumerate(ax.patches):
            value = bar.get_height()
            ax.annotate(f'{int(value)}', 
                        (bar.get_x() + bar.get_width() / 2, value), 
                        ha='center', va='bottom', fontsize=10, color='black')
        
        plt.show()
        
# Análisis de distribución del fotoperiodo
def analyze_distribution_photoperiod(df):
    # Columnas categóricas relevantes para el análisis
    categorical_columns = ['photoperiod']
    
    for col in categorical_columns:
        print(f"\nDistribución del Tipo de Fotoperiodo:")
        
        # Calcular valores absolutos y porcentajes
        value_counts = df[col].value_counts()
        percentages = df[col].value_counts(normalize=True) * 100
        
        # Combinar en un solo DataFrame para mayor claridad
        distribution_df = pd.DataFrame({
            'Count': value_counts,
            'Percentage (%)': percentages
        })
        print(distribution_df)
        
        # Graficar la distribución
        plt.figure(figsize=(8, 6))
        ax = sns.barplot(x=distribution_df.index, y=distribution_df['Count'], palette='viridis')
        plt.title(f'Distribución del Tipo de Fotoperiodo')
        plt.xlabel('Fotoperiodo')
        plt.ylabel('Cantidad de Genéticas')
        plt.xticks(rotation=45)
        
        # Agregar valores encima de las barras
        for i, bar in enumerate(ax.patches):
            value = bar.get_height()
            ax.annotate(f'{int(value)}', 
                        (bar.get_x() + bar.get_width() / 2, value), 
                        ha='center', va='bottom', fontsize=10, color='black')
        
        plt.show()

def analyze_cannabinoids(df):
    print("\nCannabinoides:")
    cannabinoids_df = parse_json_column(df['cannabinoids'])
    cannabinoids_df = pd.json_normalize(cannabinoids_df)
    print(cannabinoids_df.describe())

    # Columnas para el cálculo de la media
    columns_to_avg = ['thc.percentile50', 'cbg.percentile50', 'cbd.percentile50', 'cbc.percentile50', 'thcv.percentile50']
    
    # Filtrar columnas que existen en el DataFrame
    available_columns = [col for col in columns_to_avg if col in cannabinoids_df.columns]

    # Calcular la media de las columnas disponibles
    mean_values = cannabinoids_df[available_columns].mean()

    # Mapeo de las columnas a los nombres de los cannabinoides
    cannabinoid_names = ['thc', 'cbg', 'cbd', 'cbc', 'thcv']
    
    # Graficar las medias
    plt.figure(figsize=(10, 6))
    bars = mean_values.plot(kind='bar', color='lightcoral', edgecolor='black')

    # Ajustar las etiquetas del eje x
    plt.xticks(range(len(cannabinoid_names)), cannabinoid_names, rotation=45)

    # Agregar los valores por encima de cada barra
    for i, v in enumerate(mean_values):
        plt.text(i, v + 0.05, round(v, 2), ha='center', va='bottom', fontsize=12)

    plt.title('Principales Cannabinoides', fontsize=16)
    plt.xlabel('Cannabinoide')
    plt.ylabel('Medición Promedio (%)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def analyze_terpenes(df):
    print("\nTerpenos:")
    terps_df = parse_json_column(df['terps'])
    terps_df = pd.json_normalize(terps_df)
    print(terps_df.describe())

    # Columnas para el cálculo de la media
    columns_to_avg = ['myrcene.score', 'caryophyllene.score', 'limonene.score', 'pinene.score', 'humulene.score', 'linalool.score', 'terpinolene.score', 'ocimene.score']
    
    # Filtrar columnas que existen en el DataFrame
    available_columns = [col for col in columns_to_avg if col in terps_df.columns]

    # Calcular la media de las columnas disponibles
    mean_values = terps_df[available_columns].mean()

    # Mapeo de las columnas a los nombres de los terpenos (excluyendo "score")
    terpenes_names = ['myrcene', 'caryophyllene', 'limonene', 'pinene', 'humulene', 'linalool', 'terpinolene', 'ocimene']
    
    # Graficar las medias
    plt.figure(figsize=(12, 6))
    bars = mean_values.plot(kind='bar', color='lightcoral', edgecolor='black')

    # Ajustar las etiquetas del eje x
    plt.xticks(range(len(terpenes_names)), terpenes_names, rotation=45)

    # Agregar los valores por encima de cada barra
    for i, v in enumerate(mean_values):
        plt.text(i, v + 0.005, round(v, 2), ha='center', va='bottom', fontsize=12)

    plt.title('Principales Terpenos', fontsize=16)
    plt.xlabel('Terpeno')
    plt.ylabel('Medición Promedio (%)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def analyze_grow_info(df):
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    print("\nGrowInfo:")
    growInfo_df = parse_json_column(df['growInfo'])
    growInfo_df = pd.json_normalize(growInfo_df)
    print(growInfo_df.describe())

    # Ploteo de GrowInfo (excluyendo valores de 0)
    for column in growInfo_df.select_dtypes(include=['float64', 'int64']).columns:
        filtered_data = growInfo_df[growInfo_df[column] > 0]  # Excluir valores de 0
        if not filtered_data.empty:  # Verificar si hay datos para graficar
            plt.figure(figsize=(8, 6))
            sns.histplot(filtered_data[column], kde=True, bins=20)
            plt.title(f'Distribución de {column} (excluyendo 0)', fontsize=14)
            plt.xlabel(column)
            plt.ylabel('Frecuencia')
            plt.grid(True)
            plt.show()

# Ejecutar el análisis
analyze_distribution_phenotype(df)
analyze_distribution_photoperiod(df)
# analyze_slug_column(df)
# analyze_name_column(df)
# analyze_parents_children_columns(df)
# analyze_description_plain(df)
# analyze_general_statistics(df)
# analyze_cannabinoids(df)
# analyze_terpenes(df)
# analyze_grow_info(df)