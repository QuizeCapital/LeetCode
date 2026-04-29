import pandas as pd

def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    def odd_sum(values):
        return sum(x for x in values if x % 2 == 1)
    def even_sum(values):
        return sum(x for x in values if x % 2 == 0)

    agg_dict = {
        'odd_sum' : ('amount', odd_sum)
        ,'even_sum' : ('amount', even_sum)
    }

    for new_col, (col, func) in agg_dict.items():
        transactions[new_col] = transactions.groupby('transaction_date')[col].transform(func)
    
    return transactions[['transaction_date', 'odd_sum', 'even_sum']].drop_duplicates().sort_values('transaction_date')