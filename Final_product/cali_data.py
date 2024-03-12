import pandas as pd

def get(datatable):
    '''
    Give a pandas dataframe created from the
    Data_Tables/VSRR_Provisional_Drug_Overdose_Death_Counts.csv
    path, also can print out table and all columns
    for reference of use.

    :Param: 
    :datatable: data table on which to perform filtering
    :type: Pandas Data Frame
        
    :Returns: Pandas Data Frame
    '''
    assert isinstance(datatable, pd.DataFrame)
    df = datatable
    df['DataValue'] = df['DataValue'].map(lambda x: float(x.replace(',',''))
                                        if isinstance(x, str) 
                                        else x)
    # Grouping Total deaths by Drug Type and Year
    conditions = (df['State'] == 'CA')
    grp = (df[conditions]
           .groupby(['Indicator','Year'])
           ['DataValue'].sum())

    return grp['Number of Deaths'], grp['Number of Drug Overdose Deaths'] 