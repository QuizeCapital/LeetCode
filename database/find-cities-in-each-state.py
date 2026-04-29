import pandas as pd

def find_cities(cities: pd.DataFrame) -> pd.DataFrame:
    agg_dict = {
        'cities' : ('city' , lambda x : ', '.join(x.sort_values()))
    }
    
    for new_col, (col, func) in agg_dict.items():
        cities[new_col] = cities.groupby('state')[col].transform(func)

    cities = cities[['state', 'cities']].drop_duplicates()

    return cities.sort_values('state')