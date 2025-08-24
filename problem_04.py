
# reverse a stack:

def insert_it(arr, item):
   if not arr:
      return arr.append(item)
   
   # got element 
   it= arr.pop()
   insert_it(arr, item) # 1st job: last element on 1st position 
   arr.append(it)


def sol(arr):
   if not arr: # stack empty 
      return

   item= arr.pop()   
   sol(arr) # without last element 
   insert_it(arr,item) # insert the last into it's place 1stly !
   return arr

print(sol([1,2,3,4,5])) 
