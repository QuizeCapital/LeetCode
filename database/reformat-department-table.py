import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

    department_pivoted = department.pivot(index = 'id', columns = 'month', values = 'revenue')
    department_pivoted = department_pivoted.reindex(columns = months).rename(columns = lambda prefix: prefix + "_Revenue")
    department_pivoted.reset_index(inplace = True)

    return department_pivoted
