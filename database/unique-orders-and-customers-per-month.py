import pandas as pd

def unique_orders_and_customers(orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders[orders['invoice'] > 20]
    orders['month'] = pd.to_datetime(orders['order_date']).dt.strftime('%Y-%m')
    agg_dict = {
        'order_count' : ('order_id', 'count')
        ,'customer_count' : ('customer_id', 'nunique')
    }
    for new_col, (col, func) in agg_dict.items():
        orders[new_col] = orders.groupby('month')[col].transform(func)
    return orders[['month','order_count', 'customer_count']].drop_duplicates()
    