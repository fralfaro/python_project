import numpy as np
import pytest
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from src.models.models import apply_random_forest


# Fixture para cargar los datos de ejemplo
@pytest.fixture
def iris_data():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

# Test para la función apply_random_forest
def test_apply_random_forest(iris_data):
    X_train, X_test, y_train, y_test = iris_data

    # Llama a la función que quieres probar
    y_pred = apply_random_forest(X_train, y_train, X_test)

    # Asegúrate de que la salida sea la esperada
    assert isinstance(y_pred, np.ndarray)
    assert y_pred.shape == y_test.shape

    # Calcula la precisión de las predicciones
    accuracy = accuracy_score(y_test, y_pred)

    # Asegúrate de que la precisión sea razonable
    assert accuracy >= 0.0 and accuracy <= 1.0
