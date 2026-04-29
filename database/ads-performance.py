import pandas as pd

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    ads['clicks'] = np.where(ads['action'] == 'Clicked', 1,0)
    ads['views'] = np.where(ads['action'] == 'Viewed', 1,0)
    agg_dict = {
        'clicks_sum' : ('clicks', 'sum')
        ,'views_sum' : ('views', 'sum')
    }
    for new_col, (col, func) in agg_dict.items():
        ads[new_col] = ads.groupby('ad_id')[col].transform(func)
    ads['ctr'] = np.where(
        ads['clicks_sum'] + ads['views_sum'] == 0, 
        0, 
        round((ads['clicks_sum']/ (ads['clicks_sum'] + ads['views_sum']))*100, 2)
        )
    return ads[['ad_id', 'ctr']].drop_duplicates().sort_values(['ctr', 'ad_id'], ascending = [False, True])
    