import pandas as pd

def find_students_who_improved(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores.sort_values(['student_id', 'subject', 'exam_date'])
    agg_dict = {
        # 'subject' : ('subject', 'nunique')
        'latest_score' : ('score', 'last')
        ,'first_score' : ('score', 'first')
        # ,'exam_date_min' : ('exam_date', 'min')
        # ,'exam_date_max' : ('exam_date', 'max')
    }
    for new_col, (col, func) in agg_dict.items():
        scores[new_col] = scores.groupby(['student_id', 'subject'])[col].transform(func)
    scores = scores[scores['first_score'] < scores['latest_score']]
    return scores[['student_id' , 'subject'  , 'first_score' , 'latest_score' ]].sort_values(['student_id', 'subject']).drop_duplicates()
