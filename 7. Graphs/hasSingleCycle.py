def hasSingleCycle(array):
    # Write your code here.	
	idx = 0
	counter = 0
	while counter < len(array):
		# If we've jumped more than once and we find ourselves back at the starting index, we haven't visited each element
		if counter > 0 and idx == 0:
			return False
		jump = array[idx]
		idx = (idx + jump) % len(array)
		if idx < 0:
			idx = idx + len(array)
		counter += 1

	if idx == 0:
		return True
	else:
		return False
	
	
	
	
	
