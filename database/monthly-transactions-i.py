import pandas as pd
from datetime import datetime

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['month'] = pd.to_datetime(transactions['trans_date']).dt.strftime('%Y-%m')
    transactions['approved_flag'] = np.where(transactions['state']== 'approved', 1, 0)
    transactions['approved_total'] = np.where(transactions['approved_flag']== 1, transactions['amount'] * transactions['approved_flag'], 0)
    agg_dict = {
        'trans_count' : ('state', 'size')
        ,'approved_count' : ('approved_flag', 'sum')
        ,'trans_total_amount' : ('amount', 'sum')
        ,'approved_total_amount' : ('approved_total', 'sum')
    }
    for new_col, (col, func) in agg_dict.items():
        transactions[new_col] = transactions.groupby(['month', 'country'], dropna=False)[col].transform(func)
    return transactions[['month', 'country','trans_count', 'approved_count', 'trans_total_amount','approved_total_amount'
]].drop_duplicates()