import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    agg_dict = {
        'total_amount' : ('price', 'sum')
    }
    for new_col, (col, func) in agg_dict.items():
        sales[new_col] = sales.groupby('seller_id')[col].transform(func)
    
    sales['rank'] = sales['total_amount'].rank(method = 'dense', ascending = False)
    sales =  sales[['seller_id', 'rank']].drop_duplicates()
    return sales[sales['rank'] == 1][['seller_id']]
    