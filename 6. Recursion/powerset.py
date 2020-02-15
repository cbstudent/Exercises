def powerset(array):
    subset = [[]] # initialize with empty array
	
	for i in array:
		for x in range(len(subset)):
			subset.append(subset[x] + [i])
	return subset
	
	
