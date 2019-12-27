def quickSort(array):
    # Write your code here.
    _quickSort(array, 0, len(array) - 1)
	return array

def _quickSort(array, lo, hi):
	
	if lo >= hi:
		return
	
	pivot = partition(array, lo, hi)
	
	# process the bottom part
	_quickSort(array, lo, pivot - 1)
	
	# process the top part
	_quickSort(array, pivot + 1, hi)
	
	
def partition(array, lo, hi):
	pivot = array[lo]
	swap_index = lo + 1
	
	for i in range(lo + 1, hi + 1):
		if array[i] < pivot:
			array[i], array[swap_index] = array[swap_index], array[i]
			swap_index += 1
		
	array[lo], array[swap_index - 1] = array[swap_index - 1], array[lo]
	
	return swap_index - 1

