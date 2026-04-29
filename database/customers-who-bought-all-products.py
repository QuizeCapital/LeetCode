import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    len_products = len(product)
    agg_dict = {
        'num_of_unique_prods' : ('product_key', 'nunique')
    }
    for col_name, (col, func) in agg_dict.items():
        customer[col_name] = customer.groupby('customer_id')[col].transform(func)
    customer = customer[customer['num_of_unique_prods'] == len_products][['customer_id']]
    return customer.drop_duplicates()