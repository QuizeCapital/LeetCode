import pandas as pd

def low_quality_problems(problems: pd.DataFrame) -> pd.DataFrame:
    problems['perc'] = problems['likes'] / (problems['likes'] + problems['dislikes'])
    problems = problems[problems['perc'] < 0.6]
    problems = problems[['problem_id']]
    return problems.sort_values('problem_id')