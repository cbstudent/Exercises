class twoSum:
	
	def __init__(self):
		nums = [2, 7, 11, 15]
		target = 18
		
		indices = self.getIndices(nums, target)
		print(indices)
		
	def getIndices(self, nums, target):
		# Create an empty dict
		complements = {}
		
		# Walk through the list
		for idx, i in enumerate(nums):
			# Check if target - i is in the list
			if (target-i) in complements:
				# If yes, return the indices
				return (idx, complements[target-i])
			else:
				# If not, add it to the dict
				complements[i] = idx
		
		return (-1, -1)

twoSum()
