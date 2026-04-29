import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:

    agg_dict = {
        'followers_count' : ('follower_id', 'count')
    }
    followers = followers.groupby('user_id').agg(**agg_dict).reset_index()
    followers = followers.sort_values('user_id')
    return followers
    