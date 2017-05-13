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
  while ll.next:
    ll = ll.next
    q.append(ll.data)
    if len(q) > m:
      q.popleft()
  return q.popleft()    


print question5(None, None)
# None

nodes = [Node(i) for i in xrange(5)]
for i, n in enumerate(nodes):
  if i + 1 < len(nodes):
    n.next = nodes[i + 1]

print question5(nodes[0], 2)
# 3