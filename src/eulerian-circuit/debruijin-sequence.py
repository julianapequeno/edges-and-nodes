# Python3 implementation of
# the above approach
import math 

seen = set()
edges = []

# Modified DFS in which no edge
# is traversed twice
def dfs( node, k, A):
	
	for i in range(k):
		str = node + A[i]
		if (str not in seen):
			seen.add(str)
			dfs(str[1:], k, A)
			edges.append(i)

# Function to find a de Bruijn sequence
# of order n on k characters
def deBruijn(n, k, A):
	
	# Clearing global variables
	seen.clear()
	edges.clear()
	
	startingNode = A[0] * (n - 1)
	dfs(startingNode, k, A)
	
	S = ""
	
	# Number of edges
	l = int(math.pow(k, n))
	for i in range(l):
		S += A[edges[i]]
		
	S += startingNode
	return S

# Driver code
n = 3
k = 2
A = "01"

print(deBruijn(n, k, A))

# This code is contributed by shubhamsingh10
