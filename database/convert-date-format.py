import pandas as pd

def convert_date_format(days: pd.DataFrame) -> pd.DataFrame:
    days['day'] = pd.to_datetime(days['day']).dt.strftime('%A, %B %-d, %Y')
    return days
    