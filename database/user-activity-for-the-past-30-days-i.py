import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.drop_duplicates()
    agg_dict ={
        'active_users' : ('user_id', 'nunique')
    }
    activity['activity_date'] = pd.to_datetime(activity['activity_date'])
    activity = activity[(activity['activity_date'] > '2019-06-27') & (activity['activity_date'] <= '2019-07-27')]
    for col_name , (col, func) in agg_dict.items():
        activity[col_name] = activity.groupby('activity_date')[col].transform(func)
    activity = activity.rename(columns = {'activity_date': 'day'})
    return activity[['day', 'active_users']].drop_duplicates()