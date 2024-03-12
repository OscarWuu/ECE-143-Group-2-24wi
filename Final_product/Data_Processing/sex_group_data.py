import pandas as pd

def get(datatable):
    '''
    Gives ints of:
    Number of Male deaths by drugs,
    Number of Female deaths by drugs,
    Number of total deaths by drugs

    :Param: 
    :datatable: data table on which to perform filterign
    :type: Pandas Data Frame

    :Returns: pd.Series, pd.Series
    '''
    assert isinstance(datatable, pd.DataFrame)
    df = datatable
    conditions = ((df['Intent'] == 'All (preventable, intentional, undetermined)')
                & (df['Gender'] != 'Both sexes')
                & (df['DrugType'] != 'All drugs'))
    grp = df[conditions].groupby(['Gender','DrugType'])['AllAges'].sum()
    return grp['Male'], grp['Female']

