import pandas as pd

def salaries_difference(salaries: pd.DataFrame) -> pd.DataFrame:
    agg_dict = {
        'salary_differences' : ('salary', 'max')
    }
    for new_col, (col, func) in agg_dict.items():
        salaries[new_col] = salaries.groupby('department')[col].transform(func)
    
    salaries['salary_difference'] = abs(salaries.loc[salaries['department'] == 'Engineering', 'salary_differences'].values[0] - salaries.loc[salaries['department'] == 'Marketing','salary_differences'].values[0])
    return salaries[['salary_difference']].drop_duplicates()
    