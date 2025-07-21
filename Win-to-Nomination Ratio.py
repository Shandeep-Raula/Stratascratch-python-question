import pandas as pd

oscar_nominees.groupby('nominee').agg(ratio=('winner','mean')).reset_index().sort_values(by='ratio', ascending=False)
