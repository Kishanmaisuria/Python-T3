def Search(value, x, low, high):

  
    while low <= high:

        mid = low + (high - low)//2

        if value[mid] == x:
            return mid

        elif value[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


value = [3, 4, 5, 6, 7, 8, 9]
x = 8

result = Search(value, x, 0, len(value)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")

