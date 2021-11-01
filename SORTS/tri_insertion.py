array = [1,654,387,23165,4,1,787,7,3,6]

for i in range(1,len(array)):
    aux=array[i]
    j=i
    
    while(array[j-1]>aux) and (j>1):
        array[j]=array[j-1]
        j=j-1
    
    array[j]=aux

print(array)