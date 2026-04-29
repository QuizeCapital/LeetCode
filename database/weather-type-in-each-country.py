import pandas as pd

def weather_type(countries: pd.DataFrame, weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.merge(countries, on ='country_id' )
    weather = weather[(weather['day'] > '2019-10-31') & (weather['day'] < '2019-12-01')]
    agg_dict = {
        'avg_weather' : ('weather_state', 'mean')
    }
    for new_col, (col, func) in agg_dict.items():
        weather[new_col] = weather.groupby('country_name')[col].transform(func)
    
    weather['day'] = pd.to_datetime(weather['day'])
    
    weather['weather_type'] = np.where(weather['avg_weather'] <= 15, 'Cold',
    np.where( weather['avg_weather'] >= 25 , 'Hot', 'Warm'))
    return weather[['country_name', 'weather_type']].drop_duplicates()