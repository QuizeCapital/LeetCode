import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    store['rich_flag'] = np.where(store['amount'] > 500, 1, 0)
    agg_dict = {
        'rich_flag_count' : ('rich_flag', 'count')
    }
    for new_col, (col, func) in agg_dict.items():
        store[new_col] = store.groupby('customer_id')[col].transform(func)
    
    store = store[store['rich_flag'] != 0].drop_duplicates(['customer_id', 'rich_flag_count'])

    rich_count = pd.DataFrame({'rich_count' : [len(store)]})

    return rich_count
    