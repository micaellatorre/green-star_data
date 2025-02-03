import pandas as pd

def encode_categorical_vars(data):
    """
    Codifica variables categóricas usando one-hot encoding.

    """
    categorical_columns = ["haceGerminacion","geneticaPheno", "geneticaPhoto"]
    data = pd.get_dummies(data, columns=categorical_columns, dtype=int)
    return data
