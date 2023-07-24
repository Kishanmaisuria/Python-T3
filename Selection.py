def SSort(value, size):
    for step in range(size):  
        min_index = step

        for i in range(step + 1, size):
            if value[i] < value[min_index]:
                min_index = i


        value[step], value[min_index] = value[min_index], value[step]

value = [-2, 45, 0, 11, -9]
size = len(value)
SSort(value, size)
print('Sorted Order:')
print(value)
