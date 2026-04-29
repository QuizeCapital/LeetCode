import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    agg_dict = {
        'count_no_trans' : ('customer_id', 'count')
    }
    visits = visits.merge(transactions, on = 'visit_id', how = 'left')
    visits = visits[visits['transaction_id'].isna()]
    for new_col, (col, func) in agg_dict.items():
        visits[new_col] = visits.groupby('customer_id')[col].transform(func)

    return visits[['customer_id', 'count_no_trans']].drop_duplicates('customer_id')
    