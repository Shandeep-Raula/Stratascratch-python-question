import pandas as pd

df = playbook_events.merge(playbook_users, on='user_id', how='inner').query("location == 'Argentina' & language != 'spanish' & device == 'macbook pro'")
df.groupby(['company_id','language']).agg(n_events = ('company_id', 'count')).reset_index()
