from collections import deque

# Here the nodes are just represented through their indices in the adjacency list, which is adj
 
adj = [[1],[2],[0]]

n = len(adj) 
indegree = [0]*n
for i in range(n): 
		for j in adj[i]:
			indegree[i]+=1
queue = deque()
count = 0
for i in range(len(indegree)):
	if indegree[i] == 0:
		queue.append(i)
		count += 1

while queue:
	node = queue.popleft()
	for adjacent in adj[node]:
		indegree[adjacent] -= 1
		if indegree[adjacent] == 0:
			queue.append(adjacent)#
			count += 1
			
print(count == n)


