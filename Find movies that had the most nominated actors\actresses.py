import pandas as pd

oscar_nominees.groupby(['year','movie']).agg(n_occurences=('id','count')).reset_index().sort_values(by='n_occurences',ascending=False)[['movie','n_occurences']]
