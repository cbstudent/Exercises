def threeNumberSum(array, targetSum):
    
	# Sort the array (can be sorted in place, because we don't care about the original indices)
	array.sort()
	
	res = []
	
	# Use two pointers, one starting from the left, and one starting from the right	
	for idx, curr in enumerate(array):
		i = idx + 1
		j = len(array) - 1
		
		while i < j:
			currSum = curr + array[i] + array[j]
			
			if currSum < targetSum:
				i += 1
			elif currSum > targetSum:
				j -= 1
			elif currSum == targetSum:
				ares = sorted([curr, array[i], array[j]])
				res.append(ares)
				i += 1
				j -= 1
		
	return sorted(res)
