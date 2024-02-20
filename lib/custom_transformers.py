import pandas as pd
from typing import Dict
from sklearn.base import BaseEstimator, TransformerMixin

# Custom transformer
class CustomBaseTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return X


class ColumnTransformer(CustomBaseTransformer):
    def __init__(self, col_values: Dict = None):
        self.col_values = col_values

    def transform(self, X):
        # Custom transformation logic
        X_transformed = X.copy()
        
        for column in self.col_values:
            X_transformed.loc[X_transformed[column].isna(), [column]] = self.col_values[column]
        
        return X_transformed