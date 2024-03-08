import pandas as pd

# read csv files
def get(print_out = False) -> pd.DataFrame:
    '''
        Give a pandas dataframe created from the
        Datasets/Drug_Poisoning_deaths_and_rates.csv path,
        also printsout table and all columns for reference of use.
    
        :Param: 
        :print_out: wether or not to print out dataset information
        :type: bool
        
        :Returns: Pandas Data Frame
    '''
    file_path = r'Drug_Poisoning_deaths_and_rates.csv'
    df = pd.read_csv(file_path, 
                    skiprows=[0,1382], 
                    on_bad_lines='skip')

# Standardizing column names 
    df.columns = ['Year',
                'Gender',
                'Intent', 
                'DrugType', 
                '<1year', 
                '1-4year', 
                '5-14year', 
                '15-24year', 
                '25-34year', 
                '35-44year', 
                '45-54year', 
                '55-64year',
                '65-74year', 
                '75-84year',
                '85+year', 
                'NotStated', 
                'AllAges']
    if print_out:
        print('================ Table ================\n',df)
        print('\n================ Columns ================\n',df.columns)
    assert isinstance(df, pd.DataFrame)
    return df
