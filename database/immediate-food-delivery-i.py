import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery['immediate_percentage'] = np.where(delivery['order_date'] == 
    delivery['customer_pref_delivery_date'] , 1, 0)
    avg_perc = round(delivery['immediate_percentage'].mean() * 100, 2)

    return pd.DataFrame({'immediate_percentage' : [avg_perc]})
    