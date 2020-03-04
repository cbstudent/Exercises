from collections import deque

adj = [[1],[2],[]]

n = len(adj)
indegree = [0]*n
# Looks through every vertex
for i in range(n):
	#Looks through every outgoing edge
	for j in adj[i]:
		indegree[j]+=1
	# indegree array:
	# [1, 1, 0]
print(indegree)
queue = deque()
count = 0
for i in range(len(indegree)):
	if indegree[i] == 0:
		queue.append(i)
		count += 1
# Queue: {2} count: 1
while queue:
	node = queue.popleft()
	#Outgoing neighbors for a specific node
	for adjacent in adj[node]:
		indegree[adjacent] -= 1
		if indegree[adjacent] == 0:
			count += 1
			queue.append(adjacent)
print(count != n)
