import pandas as pd

olympics_athletes_events.query("year < 1939 & sex == 'F'")[['name']].drop_duplicates()
