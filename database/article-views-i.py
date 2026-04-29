import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views = views[views['author_id'] == views['viewer_id']]
    views = views.groupby(['author_id', 'viewer_id']).size().reset_index()
    views = views[['author_id']].rename(columns = {'author_id' : 'id'})
    return views