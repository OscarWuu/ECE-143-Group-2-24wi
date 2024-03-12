import pandas as pd

# read csv files
def get() -> pd.DataFrame:
    '''
    Give a pandas dataframe created from the
    Data_Tables/Drug_Poisoning_deaths_and_rates.csv
    and Data_Tables/VSRR_Provisional_Drug_Overdose_Death_Counts.csv
    path, also can print out table and all columns
    for reference of use.
    
    :Returns: Pandas Data Frame
    '''
    main_file_path = r'Data_Tables/Drug_Poisoning_deaths_and_rates.csv'
    bonus_file_path = r'Data_Tables/VSRR_Provisional_Drug_Overdose_Death_Counts.csv'
    main_df = pd.read_csv(main_file_path, 
                    skiprows=[0,1382], 
                    on_bad_lines='skip')
    bonus_df = pd.read_csv(bonus_file_path,
                           on_bad_lines='skip')
# Standardizing column names 
    main_df.columns = ['Year',
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
    bonus_df.columns = ['State',
                        'Year',
                        'Month', 
                        'Period', 
                        'Indicator', 
                        'DataValue',
                        'PercCompl',
                        'PercPendInvest',
                        'StateName',
                        'Footnote',
                        'FootnoteSymbol',
                        'PredictedValue']
                    
    assert isinstance(bonus_df, pd.DataFrame)
    assert isinstance(main_df, pd.DataFrame)
    return main_df, bonus_df
