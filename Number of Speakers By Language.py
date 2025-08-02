import pandas as pd

df = playbook_events.merge(playbook_users, on='user_id', how='left')[['location','language',"user_id"]]

df.groupby(['location','language']).agg(n_users=('user_id','count')).reset_index().sort_values(by='location')
