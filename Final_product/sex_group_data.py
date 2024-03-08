import pandas as pd
import data_frame
import importlib
importlib.reload(data_frame)

def get(print_out= False):
    '''
    Gives ints of:
    Number of Male deaths by drugs,
    Number of Female deaths by drugs,
    Number of total deaths by drugs

    :Param: 
    :print_out: wether or not print out dataset values
    :type: bool

    :Returns: pd.Series, pd.Series
    '''
    df = data_frame.get(print_out)
    conditions = ((df['Intent'] == 'All (preventable, intentional, undetermined)')
                & (df['Gender'] != 'Both sexes'))
    grp = df[conditions].groupby(['Gender','Year','DrugType'])['AllAges'].sum()
    if print_out: print(grp)
    return grp['Male'], grp['Female']

