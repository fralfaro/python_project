# -*- coding: utf-8 -*-
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def evaluate_classification(y_true, y_pred):
    """
    Evalúa la clasificación y muestra varias métricas de evaluación.

    Args:
    - y_true (array-like): Etiquetas verdaderas.
    - y_pred (array-like): Etiquetas predichas.

    Returns:
    - dict: Un diccionario que contiene varias métricas de evaluación.
    """
    # Calcula la matriz de confusión
    cm = confusion_matrix(y_true, y_pred)

    # Calcula las métricas de evaluación
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)

    # Crea un diccionario con las métricas de evaluación
    evaluation_metrics = {
        'Accuracy': accuracy,
        'Precision': precision,
        'Recall': recall,
        'F1 Score': f1,
        'Confusion Matrix': cm
    }

    return evaluation_metrics
