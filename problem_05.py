# reverse a string

def sol(arr):
  if len(arr)==0:
    return arr # return ''        <- same effect ! 

  return sol(arr[1:])+arr[0]

print(sol('fhfsusao'))
