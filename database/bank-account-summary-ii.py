import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    users = users.merge(transactions, on = 'account')
    agg_dict = {
        'balance' : ('amount', 'sum')
    }
    for name, (col, func) in agg_dict.items():
        users[name] = users.groupby('name')[col].transform(func)
    users = users[users['balance'] > 10000][['name', 'balance']].drop_duplicates()
    return users
    