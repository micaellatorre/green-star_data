import os
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, classification_report

def train_random_forest(X, y, output_dir):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average="weighted")

    os.makedirs(output_dir, exist_ok=True)
    model_path = os.path.join(output_dir, "random_forest.pkl")
    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    print(f"Random Forest - Accuracy: {accuracy:.4f}, F1-score: {f1:.4f}")
    return accuracy, f1
