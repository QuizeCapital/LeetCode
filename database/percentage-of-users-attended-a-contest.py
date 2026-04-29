import pandas as pd

def users_percentage(users,register):
    num_unique_users = users['user_id'].nunique()
    # print(num_unique_users)
    agg_dict = {
        'counted_id' : ('user_id', 'nunique')
    }
    register = register.groupby('contest_id').agg(**agg_dict).reset_index()
    register['percentage'] = round((register['counted_id'] / num_unique_users)*100,2)
    register= register[['contest_id', 'percentage']]
    return register.sort_values(['percentage', 'contest_id'], ascending=[False, True])
    