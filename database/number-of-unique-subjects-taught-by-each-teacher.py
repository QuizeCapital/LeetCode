import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    agg_dict = {
        'cnt' : ('subject_id', 'nunique')
    }
    teacher = teacher.groupby('teacher_id').agg(**agg_dict).reset_index()

    return teacher
    