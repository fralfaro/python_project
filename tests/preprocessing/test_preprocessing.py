# -*- coding: utf-8 -*-
import pandas as pd
import pytest
from src.preprocessing.preprocessing import preprocess_data_01, preprocess_data_02, preprocess_data_03

# Fixture para crear un DataFrame de ejemplo
@pytest.fixture
def example_dataframe():
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    }
    return pd.DataFrame(data)

def test_preprocess_data_01(example_dataframe):
    # Prueba para preprocess_data_01
    result = preprocess_data_01(example_dataframe)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (3, 2)

def test_preprocess_data_02(example_dataframe):
    # Prueba para preprocess_data_02
    result = preprocess_data_02(example_dataframe)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (3, 2)

def test_preprocess_data_03(example_dataframe):
    # Prueba para preprocess_data_03
    result = preprocess_data_03(example_dataframe)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (3, 2)
