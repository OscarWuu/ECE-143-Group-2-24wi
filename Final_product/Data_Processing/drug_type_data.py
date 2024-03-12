import pandas as pd

def get(datatable):
   '''
   Give a pandas dataframe created from the
   Datasets/Drug_Poisoning_deaths_and_rates.csv
   path, also can print out table and all columns
   for reference of use.
    
   :Param: 
   :datatable: data table on which to perform filterign
   :type: Pandas Data Frame
        
   :Returns: Pandas Data Frame
   '''
   assert isinstance(datatable, pd.DataFrame)
   df = datatable

   # Grouping Total deaths by Drug Type and Year
   conditions = ((df['Intent'] == 'All (preventable, intentional, undetermined)')
              & (df['Gender'] == 'Both sexes'))
   grp = (df[conditions]
         .groupby(['DrugType','Year'])
         ['AllAges'].sum())
   return grp
