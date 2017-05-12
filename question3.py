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

  MSP = {}
  edges = []

  for v1 in G:
    for (v2, e) in G[v1]:
      edges.append((v1, v2, e))
  edges.sort(key = lambda tup: tup[2])

  for (v1, v2, e) in edges:
    if v1 not in MSP or v2 not in MSP:
      if v1 in MSP:
        MSP[v1].append((v2, e))
      else:
        MSP[v1] = [(v2, e)]
      if v2 in MSP:
        MSP[v2].append((v1, e))
      else:
        MSP[v2] = [(v1, e)]

  if len(edges) == 0:
    MSP = G
    
  return MSP


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