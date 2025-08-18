# sort a array using recursion . margeSort 


def marge(arr, left, right): # this although used iterative way ! 
    i,j,k=0,0,0
     
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
# okay with leetcode ! 
def margeSort(arr): # recursive way here ! 
    
    if len(arr)==1: # if len(arr) <= 1:
        return arr
    mid= len(arr)//2 # using whole array that's why no need to do that ->    #lo+(hi-lo)//2  # although works fine on pc, but not on leetcode ! 
    left=margeSort(arr[:mid+1])
    right=margeSort(arr[mid+1:])
    return marge(arr,left, right)



print(margeSort([3,5,1,2,4]))
