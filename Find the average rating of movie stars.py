import pandas as pd

rating =  nominee_filmography.groupby('name').agg(avg_rating = ('rating','mean')).reset_index()
rating.merge(nominee_information, on ='name', how='left')[['birthday','name','avg_rating']]
