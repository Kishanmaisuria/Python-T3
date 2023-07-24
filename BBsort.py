def BBsort(value):
    n = len(value)
        
    for i in range(n):
        
        for Borg in range(0, n-i-1):
            
            if value[Borg] > value[Borg+ 1]:
                value[Borg], value[Borg +1] = value[Borg + 1], value[Borg]
                
                
         
Hamber = [34, 54, 12, 9, 45, 87, -9]
print("Orriginal Array: ", Hamber)
                
BBsort(Hamber)
print("Sorted Array: ", Hamber)