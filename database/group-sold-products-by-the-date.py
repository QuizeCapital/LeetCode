import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    agg_dict = {
        'num_sold' : ('product', 'nunique')
        ,'products' : ('product', lambda x: ','.join(sorted(x.drop_duplicates())))
    }
    for col, (col_name, func) in agg_dict.items():
        activities[col] = activities.groupby('sell_date')[col_name].transform(func)

    return activities[['sell_date', 'num_sold', 'products']].drop_duplicates().sort_values(['sell_date'])