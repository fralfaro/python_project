# -*- coding: utf-8 -*-
from src.metrics.metrics import evaluate_classification


# Define una función de test
def test_evaluate_classification():
    # Datos de ejemplo para el test
    y_true = [0, 1, 1, 0, 1, 0, 1]
    y_pred = [0, 1, 0, 0, 1, 1, 1]

    # Llama a la función que quieres probar
    evaluation_metrics = evaluate_classification(y_true, y_pred)

    # Asegúrate de que la salida sea la esperada
    assert isinstance(evaluation_metrics, dict)
    assert "Accuracy" in evaluation_metrics
    assert "Precision" in evaluation_metrics
    assert "Recall" in evaluation_metrics
    assert "F1 Score" in evaluation_metrics
    assert "Confusion Matrix" in evaluation_metrics
