def insertionSort(value):

    for step in range(1, len(value)):
        key = value[step]
        j = step - 1
        
       
        while j >= 0 and key < value[j]:
            value[j + 1] = value[j]
            j = j - 1
        
        value[j + 1] = key


value = [9, 5, 1, 4, 3]
insertionSort(value)
print('Sorted value in Ascending Order:')
print(value)