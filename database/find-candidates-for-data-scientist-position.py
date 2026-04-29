import pandas as pd

def find_candidates(candidates: pd.DataFrame) -> pd.DataFrame:
    candidates = candidates[candidates['skill'].isin(
                            ['Python', 'Tableau', 'PostgreSQL'])]
    agg_dict = {'count_skill' : ('skill', 'nunique')}

    for new_col, (col, func) in agg_dict.items():
        candidates[new_col] = candidates.groupby('candidate_id')[col].transform(func)
    return candidates[candidates['count_skill'] == 3][['candidate_id' ]].drop_duplicates().sort_values('candidate_id')
    