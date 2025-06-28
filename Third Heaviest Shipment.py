import pandas as pd

df = amazon_shipment.groupby('shipment_id').agg(total_weight = ('weight','sum')).reset_index()
df['rank'] = df['total_weight'].rank(method = 'dense', ascending = False)
df.query('rank == 3')[['shipment_id','total_weight']]
