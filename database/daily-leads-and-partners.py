import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    agg_dict = {
        'unique_leads' : ('lead_id', 'nunique')
        ,'unique_partners' : ('partner_id', 'nunique')
    }
    
    for new_col, (col, func) in agg_dict.items():
        daily_sales[new_col] = daily_sales.groupby(['date_id', 'make_name'])[col].transform(func)

    return daily_sales[['date_id', 'make_name', 'unique_leads', 'unique_partners']].drop_duplicates()