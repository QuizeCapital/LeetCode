import pandas as pd

def find_latest_salaries(salary: pd.DataFrame) -> pd.DataFrame:
    # salary = salary.rename(columns = {'salary_init' : 'salary'})
    salary['salary_init'] = salary['salary']
    
    agg_dict = {
        'salary' : ('salary_init', 'max')
    }
    for new_col, (col, func) in agg_dict.items():
        salary[new_col] = salary.groupby('emp_id')[col].transform(func)

    salary = salary[['emp_id', 'firstname', 'lastname', 'salary', 'department_id' ]].drop_duplicates().sort_values('emp_id')
    return salary
    