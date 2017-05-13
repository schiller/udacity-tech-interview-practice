# Question 1
# Given two strings s and t, determine whether some anagram of t is a substring of s. 
# For example: if s = "udacity" and t = "ad", then the function returns True. 
# Your function definition should look like: question1(s, t) and return a boolean True or False.

from collections import deque

def question1(s, t):
    if s is not None and t is not None:
        # empty string is substring to any string
        if t == "":
            return True

        t_count = get_letter_dict(t)
        # iterate through s taking len(t) steps
        for i in xrange(len(t) - 1, len(s), len(t)):
            if s[i] in t_count:
                if find_substring(s, i, t_count, len(t)):
                    return True
    return False

""" returns a dict with the letter count for the inputed word """
def get_letter_dict(t):
    t_count = {}
    for letter in t:
        if letter in t_count:
            t_count[letter] += 1
        else:
            t_count[letter] = 1
    return t_count

""" searches for the anagram on left and right of the initial position i """
def find_substring(s, i, t_count, len_t):
    q = deque()
    # walk left searching for anagram letters until one letter does not work
    # append letters on the left of the queue and decrement the letter count
    j = i
    while j >= 0 and j > i - len_t:
        if s[j] in t_count:
            if t_count[s[j]] > 0:
                q.appendleft(s[j])
                t_count[s[j]] -= 1
                j -= 1
            else:
                break
        else:
            break

    # check if anagram was found
    if len(q) == len_t:
        return True

    # now walk right from the initial letter
    # replace exceding left letters with right letters
    j = i + 1
    while j < len(s) and j < i + len_t and len(q) <= len_t:
        if s[j] in t_count:
            if t_count[s[j]] == 0:
                # if letter count is 0, dequeue on the left until we can use it
                k = j - len(q)
                while True:
                    popped = q.popleft()
                    t_count[popped] += 1
                    if popped == s[j]:
                        break
                    k += 1
                    # if we reach the initial letter without finding our letter, give up
                    if k == i:
                        return False
            q.append(s[j])
            t_count[s[j]] -= 1
            j += 1
        else:
            return False

    # check if anagram was found
    if len(q) == len_t:
        return True
        
    return False


print question1(None, None)
# False

print question1("", "")
# True

print question1("udacity", "ad")
# True

print question1("udacity", "ady")
# False



# Question 2
# Given a string a, find the longest palindromic substring contained in a. 
# Your function definition should look like question2(a), and return a string.

""" Traverses the string finding palindromes centers, and then navigates left and right """
def question2(a):
  if a is None:
    return None

  longest_palindrome = ""
  i = 0  
  while i < len(a):
    j = find_palindrome_center_end(a, i)
    p = find_palindrome(a, i, j)
    if len(p) > len(longest_palindrome):
      longest_palindrome = p
    i = j + 1
    
  return longest_palindrome

""" Returns the index of the last adjacent letter equal to a[i] """
def find_palindrome_center_end(a, i):
  while i + 1 < len(a):
    if a[i + 1] != a[i]:
      return i
    i += 1
  return i

""" Checks if the letters to the left and right are equal, then adds them to the palindrome. 
    Repeats until letters are unequal or the word ends """
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



# Question 3
# Given an undirected graph G, find the minimum spanning tree within G. 
# A minimum spanning tree connects all vertices in a graph with the smallest 
# possible total weight of edges. 
# Your function should take in and return an adjacency list structured like this:

# {'A': [('B', 2)],
#  'B': [('A', 2), ('C', 5)], 
#  'C': [('B', 5)]}

# Vertices are represented as unique strings. 
# The function definition should be question3(G)

def question3(G):
  if G is None:
    return None

  mst = {}
  edges = []

  # adds the other vertice to each edge and sorts all edges by weight
  for v1 in G:
    for (v2, e) in G[v1]:
      edges.append((v1, v2, e))
  edges.sort(key = lambda tup: tup[2])

  # builds the minimum spanning tree
  for (v1, v2, e) in edges:
    if v1 not in mst or v2 not in mst:
      if v1 in mst:
        mst[v1].append((v2, e))
      else:
        mst[v1] = [(v2, e)]
      if v2 in mst:
        mst[v2].append((v1, e))
      else:
        mst[v2] = [(v1, e)]

  # special case when G has just one vertice and no edges
  if len(edges) == 0:
    mst = G
    
  return mst


print question3(None)
# None

print question3({})
# {}

print question3({'A': []})
# {'A': []}

G = {'A': [('B', 1), ('C', 5), ('D', 4)],
     'B': [('A', 1), ('C', 2), ('D', 6)],
     'C': [('A', 5), ('B', 2), ('D', 3)],
     'D': [('A', 4), ('B', 6), ('C', 3)]}

print question3(G)
# {'A': [('B', 1)],
#  'B': [('A', 1), ('C', 2)],
#  'C': [('B', 2), ('D', 3)],
#  'D': [('C', 3)]}



# Question 4
# Find the least common ancestor between two nodes on a binary search tree. The 
# least common ancestor is the farthest node from the root that is an ancestor 
# of both nodes. For example, the root is a common ancestor of all nodes on the 
# tree, but if both nodes are descendents of the root's left child, then that 
# left child might be the lowest common ancestor. You can assume that both nodes 
# are in the tree, and the tree itself adheres to all BST properties. 
# The function definition should look like question4(T, r, n1, n2), where T is 
# the tree represented as a matrix, where the index of the list is equal to the 
# integer stored in that node and a 1 represents a child node, r is a 
# non-negative integer representing the root, and n1 and n2 are non-negative 
# integers representing the two nodes in no particular order. For example, one 
# test case might be

# question4([[0, 1, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [1, 0, 0, 0, 1],
#            [0, 0, 0, 0, 0]],
#           3,
#           1,
#           4)

# and the answer would be 3.

def question4(T, r, n1, n2):
  if not T or r is None or n1 is None or n2 is None:
    return None
  # if n1 and n2 are on oposing sides from the root
  if (n1 <= r and n2 >= r) or (n1 >= r and n2 <= r):
    return r
  if n1 == n2:
    return n1

  # make sure n2 is the most distant from the root
  if abs(n2 - r) < abs(n1 - r):
    aux = n1
    n1 = n2
    n2 = aux

  # go up from n2 until the value crosses n1 
  lca = n2
  n2 = get_parent(T, lca)
  while abs(n2 - r) > abs(n1 - r):
    lca = n2
    n2 = get_parent(T, lca)
    
  return lca

""" Returns the parent of the specified node or None if it does not have one """
def get_parent(T, n):
  for idx, row in enumerate(T):
    if row[n] == 1:
      return idx
  return None


print question4(None, None, None, None)
# None

print question4([[0]],
                0,
                0,
                0)
# 0

print question4([[0, 0, 1, 0],
                 [0, 0, 0, 0],
                 [0, 1, 0, 1],
                 [0, 0, 0, 0]],
                0,
                1,
                3)
# 2



# Question 5
# Find the element in a singly linked list that's m elements from the end. 
# For example, if a linked list has 5 elements, the 3rd element from the end is 
# the 3rd element. The function definition should look like question5(ll, m), 
# where ll is the first node of a linked list and m is the "mth number from the end". 
# You should copy/paste the Node class below to use as a representation of a 
# node in the linked list. Return the value of the node at that position.

# class Node(object):
#   def __init__(self, data):
#     self.data = data
#     self.next = None

from collections import deque

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

def question5(ll, m):
  if not ll or not m:
    return None

  q = deque()
  q.append(ll.data)
  # traverses the linked list keeping m values on the queue
  while ll.next:
    ll = ll.next
    q.append(ll.data)
    if len(q) > m:
      q.popleft()

  # if m is larger than the linked list
  if len(q) < m:
    return None

  return q.popleft()    


print question5(None, None)
# None

print question5(Node(4), 2)
# None

nodes = [Node(i) for i in xrange(5)]
for i, n in enumerate(nodes):
  if i + 1 < len(nodes):
    n.next = nodes[i + 1]

print question5(nodes[0], 2)
# 3
