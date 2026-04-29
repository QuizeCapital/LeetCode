import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    df1 = employees[~employees['employee_id'].isin(salaries['employee_id'])]
    df2 = salaries[~salaries['employee_id'].isin(employees['employee_id'])]
    result = pd.concat([df1, df2], ignore_index = True).sort_values('employee_id', ascending = True)[['employee_id']]
    return result
