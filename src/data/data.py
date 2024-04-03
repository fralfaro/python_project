# -*- coding: utf-8 -*-
import os
import sqlite3
import pandas as pd

class TitanicData:
    @staticmethod
    def from_file(path_layout: os.PathLike) -> pd.DataFrame:
        with open(path_layout, "rb") as csv_file:
            result = pd.read_csv(csv_file, sep=",")
        return result

    @staticmethod
    def from_sql(path_db: os.PathLike, table_name: str) -> pd.DataFrame:
        # Conectar a la base de datos SQLite
        conn = sqlite3.connect(path_db)

        # Leer los datos de la tabla especificada
        query = f"SELECT * FROM {table_name};"
        result = pd.read_sql_query(query, conn)

        # Cerrar la conexión
        conn.close()

        return result