import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    agg_dict = {
        'd_count' : ('department_id', 'count')
    }
    
    for new_col, (col_name, func) in agg_dict.items():
        employee[new_col] = employee.groupby('employee_id')[col_name].transform(func)
    
    employee = employee[(employee['primary_flag']== 'Y') | (employee['d_count']== 1)][['employee_id' , 'department_id']]
    
    return employee


    