import pandas as pd
import unittest

#this checks if the data is empty or not

def test_read_csv():
    columns = [0,4]
    filepath = 'C:\\Users\\sskis\\OneDrive\\Desktop\\Python stuff T3\\Python-T3\\DiamondValues(1000).xlsx'
    dataframe = pd.read_csv(filepath,columns)
    assert not dataframe.empty,"CSV data should not be empty"
    excepted_columns = ['Carat Weight','Price']
    assert all (col in dataframe.columns for col in excepted_columns),"worky"
    
    