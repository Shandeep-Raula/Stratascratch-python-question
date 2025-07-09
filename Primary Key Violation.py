import pandas as pd

dim_customer.groupby('cust_id').agg(no_of_accurance = ('cust_id' , 'count')).\
                                reset_index().query('no_of_accurance > 1')
