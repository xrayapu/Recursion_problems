#problem : sort a stack ; kind of same problem as reverse a stack

def insert_it(arr, item):
  if not arr or item > arr[-1] # just last compair part extra then reverse the stack
    return arr.append(item)
  it=arr.pop()
  insert_it(arr, item)
  arr.append(arr,it)

def sol(arr): # same code as reverse a stack
  if not arr:
    return 
  item=arr.pop()
  sol(arr)
  insert_it(arr, item)
  return arr

print(sol([1,3,2,5,4]))
