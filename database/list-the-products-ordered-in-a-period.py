import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    agg_dict = {
        'unit' : ('unit', 'sum')
    }
    products = products.merge(orders, on = 'product_id')
    products['order_date'] = pd.to_datetime(products['order_date'])
    products = products[(products['order_date'] > '2020-01-31') & (products['order_date'] < '2020-03-01')]
    for new_col, (col, func) in agg_dict.items():
        products[new_col] = products.groupby('product_name')[col].transform(func)
    products = products[products['unit'] >= 100]
    products = products[['product_name', 'unit']].drop_duplicates()
    return products
    