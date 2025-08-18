# sort a array using recursion . margeSort 


def marge(arr, left, right): # this although used iterative way ! 
    i=j=k=0
     
    while i < len(left) and j < len(right):
        if left[i]<= right[j]:
            arr[k]= left[i]
            k+=1
            i+=1

        else:
            arr[k]= right[j]
            k+=1
            j+=1

    while i< len(left):
        arr[k]= left[i]
        k+=1
        i+=1

    while j < len(right):
        arr[k]= right[j]
        k+=1
        j+=1

    return arr

def margeSort(arr): # recursive way here ! 
    lo=0
    hi=len(arr)-1
    if len(arr)==1:
        return arr
    mid= lo+(hi-lo)//2
    left=margeSort(arr[:mid+1])
    right=margeSort(arr[mid+1:])
    return marge(arr,left, right)



print(margeSort([3,5,1,2,4]))
