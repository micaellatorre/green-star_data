import pandas as pd

def process_user_columns(data):
    """
    Procesa las columnas relacionadas al usuario y las reemplaza con un identificador único.
    
    Args:
        data (pd.DataFrame): Dataset con las columnas `userId`, `userName`, `username`, y `email`.

    Returns:
        pd.DataFrame: Dataset con un nuevo identificador autoincremental para usuarios.
    """
    # Crear una columna única combinando las columnas relacionadas con el usuario
    data['user_combined'] = data[['userId', 'userName', 'username', 'email']].astype(str).agg('-'.join, axis=1)
    
    # Generar un identificador numérico único para cada usuario
    user_mapping = {user: idx for idx, user in enumerate(data['user_combined'].unique())}
    data['user_id'] = data['user_combined'].map(user_mapping)
    
    # Eliminar las columnas originales
    data.drop(columns=['userId', 'userName', 'username', 'email', 'user_combined'], inplace=True)
    
    return data
