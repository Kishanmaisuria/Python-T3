def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n -i -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
                
         
Hamber = [34, 54, 12, 9, 45, 87, -9]
print("Orriginal Array: ", Hamber)
                
bubble_sort(Hamber)
print("Sorted Array: ", Hamber)