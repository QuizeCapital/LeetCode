import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    logins = logins[
            (logins['time_stamp'] >= '2020-01-01') &
            (logins['time_stamp'] < '2021-01-01')
    ]

    agg_dict = {
        'last_stamp' : ('time_stamp', 'max')
    }

    for new_col, (col, func) in agg_dict.items():
        logins[new_col] = logins.groupby('user_id')[col].transform(func)
    
    logins = logins.drop_duplicates(['user_id', 'last_stamp'])
    return logins[['user_id', 'last_stamp']]