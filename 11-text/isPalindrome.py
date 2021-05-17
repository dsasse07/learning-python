'''
  Determine if a string is a palindrome
'''

def isPalindrome(str):
  left = 0
  right = len(str) - 1
  while left < right:
    while not str[left].isalpha(): left += 1
    while not str[right].isalpha(): right -= 1
    if str[left].lower() != str[right].lower(): return False
    left += 1
    right -= 1
  return True


print(isPalindrome('racecar racecar racecar')) #True
print(isPalindrome('A man, a plan, a canal - Panama')) #True
print(isPalindrome('banana')) #false
