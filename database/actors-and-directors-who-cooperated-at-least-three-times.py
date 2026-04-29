import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    # Aggregate: count how many times each actor-director pair appears
    agg_dict = {
        'count': ('director_id', 'count')  # new column name 'director_id' here
    }
    
    actor_director = actor_director.groupby(['actor_id', 'director_id']).agg(**agg_dict).reset_index()
    
    # Filter pairs that cooperated at least 3 times
    actor_director = actor_director[actor_director['count'] >= 3]
    
    # Return only actor_id and director_id
    return actor_director[['actor_id', 'director_id']]
    