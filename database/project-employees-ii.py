import pandas as pd

def project_employees_ii(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    agg_dict = {
        'id_count' : ('employee_id', 'count')
    }
    for new_col, (col, func) in agg_dict.items():
        project[new_col] = project.groupby('project_id')[col].transform(func)
    
    max_emp = project['id_count'].max()
    project = project[project['id_count'] == max_emp]

    return project[['project_id']].drop_duplicates()