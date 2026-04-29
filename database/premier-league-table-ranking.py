import pandas as pd

def calculate_team_standings(team_stats: pd.DataFrame) -> pd.DataFrame:
    team_stats['points'] = (team_stats['wins']*3) + (team_stats['draws']*1)
    team_stats['position'] = team_stats['points'].rank(method='min', ascending = False)

    team_stats = team_stats[['team_id', 'team_name','points', 'position']].sort_values(['points', 'team_name'], ascending = [0,1])

    

    

    return team_stats