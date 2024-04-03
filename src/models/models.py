# -*- coding: utf-8 -*-
from sklearn.ensemble import RandomForestClassifier


def apply_random_forest(X_train, y_train, X_test):
    """
    Aplica un modelo de Random Forest entrenado a un conjunto de datos de prueba.

    Args:
    - X_train (array-like): Matriz de características de entrenamiento.
    - y_train (array-like): Vector de etiquetas de clase de entrenamiento.
    - X_test (array-like): Matriz de características de prueba.

    Returns:
    - array-like: Vector de etiquetas de clase predichas para los datos de prueba.
    """
    # Inicializa el clasificador de Random Forest
    rf_classifier = RandomForestClassifier(random_state=42)

    # Entrena el clasificador de Random Forest con los datos de entrenamiento
    rf_classifier.fit(X_train, y_train)

    # Predice las etiquetas de clase para los datos de prueba
    y_pred = rf_classifier.predict(X_test)

    return y_pred
