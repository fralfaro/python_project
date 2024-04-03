# -*- coding: utf-8 -*-
import sqlite3
import pandas as pd
import pytest
from src.data.data import TitanicData


# Creamos un fixture para cargar un DataFrame de ejemplo desde un archivo CSV
@pytest.fixture
def example_csv(tmp_path):
    data = {"A": [1, 2, 3], "B": [4, 5, 6]}
    path = tmp_path / "example.csv"
    pd.DataFrame(data).to_csv(path, index=False)
    return path


# Creamos un fixture para cargar un DataFrame de ejemplo desde una base de datos SQLite
@pytest.fixture
def example_sql(tmp_path):
    data = {"A": [1, 2, 3], "B": [4, 5, 6]}
    path_db = tmp_path / "example.db"
    conn = sqlite3.connect(path_db)
    pd.DataFrame(data).to_sql("example_table", conn, index=False)
    conn.close()
    return path_db


def test_from_file(example_csv):
    # Probamos el método from_file con un archivo CSV de ejemplo
    df = TitanicData.from_file(example_csv)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 2)


def test_from_sql(example_sql):
    # Probamos el método from_sql con una base de datos SQLite de ejemplo
    df = TitanicData.from_sql(example_sql, "example_table")
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 2)
