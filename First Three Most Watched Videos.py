import pandas as pd

videos_watched['order'] = videos_watched.groupby('user_id')['watched_at'].rank(method='dense',ascending=True)

first_three = videos_watched[videos_watched['order'] <=3]

top = first_three.groupby('video_id').agg(n_in_first_3 = ('user_id' , 'count')).reset_index()

top['rank'] = top['n_in_first_3'].rank(method='dense',ascending=False)

top[top['rank'] <=3][['video_id','n_in_first_3']]
