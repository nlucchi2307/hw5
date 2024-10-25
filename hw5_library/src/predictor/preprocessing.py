import os
import pandas as pd

class DataLoader:
    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), 'sample_diabetes_mellitus_data.csv')

    def load_data(self):
        """Load the dataset and return a DataFrame."""
        return pd.read_csv(self.file_path, delimiter=';')

class DataPreprocessor:
    def remove_nan_rows(self, df):
        """Remove rows with NaNs in 'age', 'gender' and 'ethnicity'."""
        return df.dropna(subset=['age', 'gender', 'ethnicity'])

    def fill_nan_values(self, df):
        """Impute NaNs in 'height' and 'weight' with the corresponding mean."""
        df.loc[:, 'height'] = df['height'].fillna(df['height'].mean())
        df.loc[:, 'weight'] = df['weight'].fillna(df['weight'].mean())
        return df

