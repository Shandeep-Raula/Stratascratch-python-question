import pandas as pd

playbook_users.query("language == 'chinese'").groupby('company_id').\
                                            agg(num = ('user_id','count')).\
                                            reset_index().query("num > 1")[['company_id']]
