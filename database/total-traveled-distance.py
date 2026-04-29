import pandas as pd

def get_total_distance(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    agg_dict = {
        'traveled distance' : ('distance', 'sum')
    }
    users = users.merge(rides, on = 'user_id', how = 'left')
    for new_col, (col, func) in agg_dict.items():
        users[new_col] = users.groupby('user_id')[col].transform(func)
    return users[['user_id', 'name', 'traveled distance']].drop_duplicates().sort_values('user_id')
    