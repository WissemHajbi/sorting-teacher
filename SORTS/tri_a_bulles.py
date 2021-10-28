#test
array = [1,654,387,23165,4,1,787,7,3,6]

def tri_a_bulles(array):
    test = True
    while(test==True):
        test=False
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i] , array[i+1] = array[i+1] , array[i]
                test=True
    return array




tri_a_bulles(array)
