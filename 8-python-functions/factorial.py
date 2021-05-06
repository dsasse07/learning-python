def main():
  return factorial(5)

def factorial(num):
  if num == 1 or num == 0:
    print(num)
    return num
  value = num * factorial(num-1)
  print(value) 
  return value

main()