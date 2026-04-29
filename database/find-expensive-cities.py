import pandas as pd

def find_expensive_cities(listings: pd.DataFrame) -> pd.DataFrame:
    mean_price = listings['price'].mean()
    agg_dict = {
        'avg_price' : ('price', 'mean')
    }
    for new_col, (col, func) in agg_dict.items():
        listings[new_col] = listings.groupby('city')[col].transform(func)
    listings['pass_flag'] = np.where(listings['avg_price'] > mean_price, 1, 0)
    
    listings = listings[listings['pass_flag'] == 1]
    listings = listings[['city']].drop_duplicates()
    listings = listings.sort_values('city')
    return listings