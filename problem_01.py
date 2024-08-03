# print 1 to n numbers and n to 1 numbers.

question 1:
def sol(n):
  if n==0:
    return 1
  sol(n-1)
  print(n)

sol(5) # 1,2,3,4,5

question 2:

def sol2(n):
  if n==0:
    return 1

  print(n)
  sol(n-1)


sol(5) # 5,4,3,2,1



