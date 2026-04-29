import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee = employee.merge(department, left_on = 'departmentId', right_on = 'id')
    agg_dict = {
        'Salary' : ('salary', 'max')
    }
    for col_name, (col, func) in agg_dict.items():
        employee[col_name] = employee.groupby('name_y')[col].transform(func)
    
    employee = employee[employee['salary'] == employee['Salary']]
    employee = employee.rename(columns= {'name_y':'Department', 'name_x' : 'Employee' })

    return employee[['Department','Employee' , 'Salary']]