import pandas as pd

#require_cols = [0,3]
#require_df =pd.read_excel('Book2.xlsx' , usecols=require_cols)
def read_csv(filepath, column):
    dataframe1 = pd.read_csv(filepath,usecols = column)
    return dataframe1

column = [0,4]
filepath = 'C:\\Users\\sskis\\OneDrive\\Desktop\\Python stuff T3\\DiamondValues.csv'
dataframe1 = read_csv(filepath, column)
print(dataframe1)
print("")
sorted_date = dataframe1.sort_values(by='Price')
print("Sorted Data: ")
print(sorted_date)
#dataframe1 = pd.read_excel('Book2.xlsx')
