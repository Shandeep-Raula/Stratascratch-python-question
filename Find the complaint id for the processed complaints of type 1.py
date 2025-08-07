import pandas as pd

facebook_complaints[(facebook_complaints['type']==1) & (facebook_complaints['processed']==True)][['complaint_id']]
