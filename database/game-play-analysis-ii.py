import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    agg_dict = {
        'rank' : ('event_date', 'min')
    }
    for new_col, (col, func) in agg_dict.items():
        activity[new_col] = activity.groupby('player_id')[col].transform(func)
    
    activity = activity[activity['event_date'] == activity['rank']]
    return activity[['player_id', 'device_id']]