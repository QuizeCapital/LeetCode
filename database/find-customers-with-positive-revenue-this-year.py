import pandas as pd

def find_customers(customers: pd.DataFrame) -> pd.DataFrame:
    customers['year_flag'] = np.where((customers['revenue'] > 0) & (customers['year'] == 2021), 1, 0)
    print(customers)

    customers = customers[customers['year_flag'] == 1][['customer_id']]
    return customers.drop_duplicates()

    