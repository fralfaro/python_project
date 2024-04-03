# -*- coding: utf-8 -*-
"""
Const: Constants, flags, warnings and error messages.
=====================================================

This module contains all the constants values used in the package.
"""

class LGBMClassifierParams:
    params = {
        'boosting_type': 'gbdt',
        'objective': 'binary',
        'metric': 'binary_logloss',
        'num_leaves': 31,
        'learning_rate': 0.05,
        'feature_fraction': 0.8,
        'bagging_fraction': 0.8,
        'bagging_freq': 5,
        'verbose': 0
    }

class TITANICSchemaCSV:
    """
    Scheme for the columns of the Titanic dataset
    """

    PASSENGER_ID = "PassengerId"
    SURVIVED = "Survived"
    PCLASS = "Pclass"
    NAME = "Name"
    SEX = "Sex"
    AGE = "Age"
    SIBSP = "SibSp"
    PARCH = "Parch"
    TICKET = "Ticket"
    FARE = "Fare"
    CABIN = "Cabin"
    EMBARKED = "Embarked"

    @staticmethod
    def get_features():
        """
        Retorna una lista con todas las columnas del conjunto de datos del Titanic
        """
        return [
            TITANICSchemaCSV.PASSENGER_ID,
            TITANICSchemaCSV.PCLASS,
            TITANICSchemaCSV.NAME,
            TITANICSchemaCSV.SEX,
            TITANICSchemaCSV.AGE,
            TITANICSchemaCSV.SIBSP,
            TITANICSchemaCSV.PARCH,
            TITANICSchemaCSV.TICKET,
            TITANICSchemaCSV.FARE,
            TITANICSchemaCSV.CABIN,
            TITANICSchemaCSV.EMBARKED,
        ]

    @staticmethod
    def get_target():
        """
        Retorna una lista con todas las columnas del conjunto de datos del Titanic
        """
        return [TITANICSchemaCSV.SURVIVED]
