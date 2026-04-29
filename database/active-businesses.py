import pandas as pd

def active_businesses(events: pd.DataFrame) -> pd.DataFrame:
    agg_dict = {
        'event_avg' : ('occurrences', 'mean')
    }
    for new_col, (col, func) in agg_dict.items():
        events[new_col] = events.groupby('event_type')[col].transform(func)
    
    events['diff_occ'] = events['occurrences'] - events['event_avg']
    events = events[events['diff_occ'] > 0]
    agg_dict = {
        'coun' : ('business_id', 'count')
    }
    for new_col, (col, func) in agg_dict.items():
        events[new_col] = events.groupby('business_id')[col].transform(func)
    events = events.drop_duplicates(['business_id', 'coun'])

    events = events[events['coun'] >= 2]

    return events[['business_id']]