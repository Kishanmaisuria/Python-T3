import pandas as pd


def read_csv(filepath, column):
    dataframe1 = pd.read_csv(filepath,usecols = column)
    return dataframe1

def BBsort(value):
    n = len(value)
        
    for i in range(n):
        
        for Borg in range(0, n-i-1):
            
            if value[Borg] > value[Borg+ 1]:
                value[Borg], value[Borg +1] = value[Borg + 1], value[Borg]
                
                
         
Hamber = [34, 54, 12, 9, 45, 87, -9]
column = [0,4]
filepath = 'C:\\Users\\sskis\\OneDrive\\Desktop\\Python stuff T3\\DiamondValues.csv'
dataframe1 = read_csv(filepath, column)
print(dataframe1)
print("")
sorted_date = dataframe1.sort_values(by='Price')
print("Sorted Data: ")
print(sorted_date)