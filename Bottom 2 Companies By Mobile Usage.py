import pandas as pd

mobile = fact_events[fact_events['client_id'] == 'mobile'].groupby('customer_id').\
                                                        agg(n_events = ('event_id','count')).\
                                                        reset_index()
mobile['rank'] = mobile['n_events'].rank(method='min',ascending=True)
mobile.query('rank <=2')[['customer_id','n_events']]
