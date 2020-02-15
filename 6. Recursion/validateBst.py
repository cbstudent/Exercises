# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # O(n) - time
	# O(d) - space (max depth of tree)
	
	max = float("inf")
	min = float("-inf")
	return isValid(tree, max, min)

def isValid(node, max, min):
	if not node:
		return True
	if node.value < min or node.value >= max:
		return False
	leftIsValid = isValid(node.left, node.value, min)

	return leftIsValid and isValid(node.right, max, node.value)
