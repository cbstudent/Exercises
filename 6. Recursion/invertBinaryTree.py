def invertBinaryTree(tree):
    # O(N) - R
	# O(N) - S
	
	queue = [tree]
	
	while len(queue) > 0:
		
		node = queue.pop(0)
		
		if not node:
			continue
		swapChildren(node)
		queue.append(node.left)
		queue.append(node.right)
		
def swapChildren(node):
	node.left, node.right = node.right, node.left
