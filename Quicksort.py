from matplotlib import pyplot as plt
import pandas as pd 

def Qsort (value):
    if len(value)<= 1:
        return
    else:
        pivot = value[0]
        left = [x for x in value[1:]if x < pivot]
        right = [x for x in value[1:]if x > pivot]
        return Qsort(left) + [pivot] + Qsort(right)
    
#def read_excel(filepath, column):
 #   dataframe1 = pd.read_excel(filepath)
  #  return dataframe1



         
column = 'Price'
filepath = 'C:\\Users\\sskis\\OneDrive\\Desktop\\Python stuff T3\\Python-T3\\DiamondValues(1000).xlsx'
dataframe1 = pd.read_excel(filepath)

print("Original Data:")
print(dataframe1)



data_list = dataframe1[column].tolist()


Qsort(data_list)


sorted_dataframe = pd.DataFrame(data_list)
plt.plot(sorted_dataframe)


print("Sorted Data:")
print(sorted_dataframe)


plt.subplot(1,2,1)
plt.plot(dataframe1)
plt.ylabel("YES!")

plt.subplot(1,2,2)
plt.plot(sorted_dataframe)
plt.ylabel("NO!")

plt.show()
