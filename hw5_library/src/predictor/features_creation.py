import pandas as pd
from abc import ABC, abstractmethod

class FeatureTransformer(ABC):
    @abstractmethod
    def transform(self, df):
        pass

class EthnicityEncoder(FeatureTransformer):
    def transform(self, df):
        """Generate dummies for 'ethnicity'."""
        return pd.get_dummies(df, columns=['ethnicity'], prefix='ethnicity')

class GenderBinaryEncoder(FeatureTransformer):
    def transform(self, df):
        """Create a binary variable for 'gender' and remove the original 'gender' column."""
        df['gender_binary'] = df['gender'].map({'M': 1, 'F': 0})
        df = df.drop(columns=['gender'])  # Rimuove la colonna 'gender'
        return df

class CategoricalEncoder(FeatureTransformer):
    def transform(self, df):
        """Transform categorical columns into dummy variables."""
        # Aggiunge variabili dummy per le colonne categoriche rimanenti
        return pd.get_dummies(df, columns=['hospital_admit_source', 'icu_admit_source', 'icu_stay_type', 'icu_type'], drop_first=True)
