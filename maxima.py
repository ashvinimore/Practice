print("maxima")
array =  [1 ,2 ,3]
if len(array) <= 2:
    if (array[0] > array[1]):
        print(array[0])
    else:
        print(array[0])

else:
    j = 0
    k = 0
    for i,val in enumerate(array):

       if j < (len(array)-1) :
           j = i+1
           k = i-1
           if(array[k] < array[i] > array[j]):
               print(array[i])

       else:
            pass