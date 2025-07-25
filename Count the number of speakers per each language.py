import pandas as pd

playbook_users.groupby('language').agg(size = ('user_id','count')).reset_index().sort_values(by='size', ascending=False)
