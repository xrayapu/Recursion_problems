# factorial number

def sol(num):
  if num ==0 or num==1:
    return 1

  return num*sol(num-1)

print(sol(3))
