from importlib import reload
import pandas as pd
import data_frame
reload(data_frame)


def get():

   df = data_frame.get()

   # Grouping Total deaths by Drug Type and Year
   conditions = ((df['Intent'] == 'All (preventable, intentional, undetermined)')
              & (df['Gender'] == 'Both sexes'))
   grp = (df[conditions].groupby('Year'))
   return grp

