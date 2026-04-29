import pandas as pd

def npv_queries(npv: pd.DataFrame, queries: pd.DataFrame) -> pd.DataFrame:
    queries = queries.merge(npv, on = ['id', 'year'], how = 'left')

    queries['npv'] = queries['npv'].fillna(0)
    return queries
    