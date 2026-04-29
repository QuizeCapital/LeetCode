import pandas as pd

def loan_types(loans: pd.DataFrame) -> pd.DataFrame:
    loans['type_flag'] = np.where(
        loans['loan_type'] == 'Mortgage' 
        ,1 
        ,np.where(loans['loan_type'] == 'Refinance', 2, np.nan))

    agg_dict = {
        'count_type' : ('type_flag', 'nunique')
    }

    for new_col, (col, func) in agg_dict.items():
        loans[new_col] = loans.groupby('user_id')[col].transform(func)
    print(loans)
    loans = loans[['user_id', 'count_type']][loans['count_type'] >= 2].drop_duplicates()
    return loans[['user_id']].sort_values('user_id')
    