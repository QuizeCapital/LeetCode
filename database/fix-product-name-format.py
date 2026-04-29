import pandas as pd

def fix_name_format(sales: pd.DataFrame) -> pd.DataFrame:
    sales['cleaned_name'] = sales['product_name'].str.strip().str.lower()
    sales['clean_date'] = pd.to_datetime(sales['sale_date']).dt.strftime("%Y-%m")

    agg_dict = {
        'sum_prods' : ('sale_id', 'nunique')
    }

    for new_col, (col, func) in agg_dict.items():
        sales[new_col] = sales.groupby(['cleaned_name', 'clean_date'])[col].transform(func)
    
    sales = sales[['cleaned_name', 'clean_date', 'sum_prods']]
    sales = sales.rename(columns = {'cleaned_name':'product_name', 'clean_date' : 'sale_date'
    ,'sum_prods': 'total' })
    return sales.drop_duplicates().sort_values(['product_name', 'sale_date'])