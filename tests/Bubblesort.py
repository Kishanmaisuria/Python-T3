def bubsort(value):
    for i in range(len(value)):
        for j in range (0,len(value)-i-1):
            if value[j]>value[j+1]:
                

                temp = value[j]
                value[j]=value[j+1]
                value[j+1]= temp
                
value = [-2,45,0,11,-9]
bubsort(value)
print("sorted values:")
print(value)


# easyer buuble sort 
#value = [7, 5, 4, 6, 3, 9, 8]
#value.sort()
#print (value)