# Question 2
# Given a string a, find the longest palindromic substring contained in a. 
# Your function definition should look like question2(a), and return a string.

""" traverses a finding palindromes centers, and then navigates left and right """
def question2(a):
  if a is None:
    return None
  i = 0
  longest_palindrome = ""
  while i < len(a):
    j = find_palindrome_center_end(a, i)
    p = find_palindrome(a, i, j)
    if len(p) > len(longest_palindrome):
      longest_palindrome = p
    i = j + 1
  return longest_palindrome

""" returns the index of the last adjacent letter equal to a[i] """
def find_palindrome_center_end(a, i):
  while i + 1 < len(a):
    if a[i + 1] != a[i]:
      return i
    i += 1
  return i

def find_palindrome(a, i, j):
  p = ""
  for k in xrange(i, j + 1):
    p += a[k]
  i -= 1
  j += 1
  while i >= 0 and j < len(a):
    if a[i] == a[j]:
      p = a[i] + p + a[j]
      i -= 1
      j += 1
    else:
      break
  return p


print question2(None)
# None

print question2("")
# ""

print question2("aeioieu")
# "eioie"

print question2("aeioooieu")
# "eioooie"
