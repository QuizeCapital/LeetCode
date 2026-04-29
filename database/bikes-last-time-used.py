import pandas as pd

def last_used_time(bikes: pd.DataFrame) -> pd.DataFrame:
    bikes = bikes.rename(columns ={'end_time' : 'end_time_initial'})
    agg_dict = {
        'end_time' : ('end_time_initial', 'max')
    }
    for new_col, (col, func) in agg_dict.items():
        bikes[new_col] = bikes.groupby('bike_number')[col].transform(func)
    print(bikes)
    return bikes[['bike_number', 'end_time']].drop_duplicates().sort_values(['end_time'], ascending = False)