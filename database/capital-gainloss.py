import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    agg_dict = {
        'capital_gain_loss' : ('price_direction', 'sum')    }

    stocks['price_direction'] = np.where(stocks['operation'] == 'Sell', 1 * stocks['price'], -1 * stocks['price'])

    for col_name ,(col, func) in agg_dict.items():
        stocks['capital_gain_loss'] = stocks.groupby('stock_name')[col].transform(func)

    return stocks[['stock_name', 'capital_gain_loss']].drop_duplicates()