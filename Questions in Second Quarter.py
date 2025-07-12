import pandas as pd

fb_searches['year'] = fb_searches['date'].dt.year
fb_searches['quarter'] = fb_searches['date'].dt.quarter
fb_searches[(fb_searches['year']==2021) & (fb_searches['quarter']==2)]['search_id'].count()
