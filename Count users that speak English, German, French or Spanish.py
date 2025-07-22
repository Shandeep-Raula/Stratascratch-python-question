import pandas as pd

playbook_users[playbook_users['language'].isin(['english', 'german', 'french', 'spanish'])]['user_id'].nunique()
