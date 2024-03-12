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
        
   :Returns: Pandas Series
   '''
   assert isinstance(datatable, pd.DataFrame)
   df = datatable
   # Filtering all death types, all sex, 
   # and all drugs.
   # Then extracting only  the columns
   # that have values for age.
   conditions = ((df['Intent'] == 'All (preventable, intentional, undetermined)')
              & (df['Gender'] == 'Both sexes')
              & (df['DrugType'] == 'All drugs'))
   age_columns = df.columns.map(lambda x: x[-4:] == ('year'))
   return df[conditions].iloc[:,age_columns].sum()
   

