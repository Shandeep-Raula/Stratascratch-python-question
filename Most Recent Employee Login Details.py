import pandas as pd

worker_logins['rank'] = worker_logins.groupby('worker_id')['login_timestamp'].rank(method ='dense',ascending = True)
first = worker_logins.query('rank == 1').drop(columns=['rank'])
