NTH_NUMBER = 6

def fibonacci(n):
  if n == 1: return 0
  if n == 2: return 1
  two_prev = 0
  one_prev = 1
  i = 3

  print(two_prev)
  print(one_prev)
  while i <= n:
    this_num = two_prev + one_prev
    two_prev = one_prev
    one_prev = this_num
    print(this_num)
    i+=1

fibonacci(100)

