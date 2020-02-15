def findClosestValueInBst(tree, target):
    # Write your code here.
    closest = float("-inf")
	return findClosest(tree, target, closest)


def findClosest(node, target, closest):
	if not node:
		return closest
	if abs(closest - target) > abs(node.value - target):
		closest = node.value
	
	if target < node.value:
		return findClosest(node.left, target, closest)
	elif target > node.value:
		return findClosest(node.right, target, closest)
	else:
		return closest

	
