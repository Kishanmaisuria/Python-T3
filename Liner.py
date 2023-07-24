def search(value, items):
 
    for i , val in enumerate(value):
 
        if val == items:
            return i
        

value = [2,4,0,1,9]
items = 1




result = search (value, items)
if result == -1:
    print("Element not found")
else:
    print("Element found at index: ", result)

                