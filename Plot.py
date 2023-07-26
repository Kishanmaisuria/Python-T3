from matplotlib import pyplot as plt
#VR == variables 
import pandas as pd
#read_csv read_excel can be changed depending on da file 
def BBsort(value):
    n = len(value)
        
    for i in range(n):
        
        for Obama in range(0, n-i-1):
            
            if value[Obama]['Price'] > value[Obama+ 1]['Price']:
                value[Obama], value[Obama +1] = value[Obama + 1], value[Obama]
                
                
def read_excel(filepath, column):
    dataframe1 = pd.read_excel(filepath,usecols = column)
    return dataframe1


         
column = [0,4]
filepath = 'C:\\Users\\sskis\\OneDrive\\Desktop\\Python stuff T3\\Python-T3\\DiamondValues(1000).xlsx'
dataframe1 = read_excel(filepath, column)

print("Original Data:")
print(dataframe1)
plt.plot(dataframe1)
print("")
plt.ylabel('Original Data')
plt.show


data_list = dataframe1.to_dict('records')


BBsort(data_list)


sorted_dataframe = pd.DataFrame(data_list)
plt.plot(sorted_dataframe)


print("Sorted Data:")
print(sorted_dataframe)
plt.ylabel('Sorted data Bubblesort')
plt.show

#VR_X =[]
#VR_Y =[]

plt.title("Median Prices")
#plt.xlabel("Amount of data")
#plt.ylabel("Price")

#plt.plot(VR_X,VR_Y)
#plt.show()