import os
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score

def train_svm(X, y, output_dir):
    print("Entrenando SVM...")

    # Convertir one-hot encoding a etiquetas (si es necesario)
    if y.shape[1] > 1:
        y = np.argmax(y.values, axis=1)  # Convierte one-hot a etiquetas de clase

    # Separar en train y test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

    # Inicializar modelo SVM con kernel lineal
    model = SVC(kernel="linear", random_state=42)

    # Entrenar modelo
    model.fit(X_train, y_train)

    # Evaluación
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average="weighted")

    # Guardar modelo entrenado
    os.makedirs(output_dir, exist_ok=True)
    model_path = os.path.join(output_dir, "svm_model.pkl")
    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    print(f"Modelo SVM guardado en {model_path}")
    print(f"Accuracy: {accuracy:.4f}, F1-score: {f1:.4f}")

    return accuracy, f1
