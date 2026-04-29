import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.sort_values('salary', ascending = False)
    employee = employee.drop_duplicates(['salary'])
    employee = employee.rename(columns = {'salary' : 'SecondHighestSalary'})
    if len(employee) < 2:
        return pd.DataFrame({'SecondHighestSalary' : [None]})
    return employee.iloc[[1]][['SecondHighestSalary']]
