def quickSort(arr):
	_quickSort(arr, 0, len(arr) - 1)

def _quickSort(arr, lo, hi):
	
	if lo >= hi:
		return
	
	pivot = partition(arr, lo, hi)
	
	# partition bottom part
	_quickSort(arr, lo, pivot - 1)
	
	# partition top part
	_quickSort(arr, pivot + 1, hi)

def partition(arr, lo, hi):
	pivot = arr[lo]
	swap_index = lo + 1
	
	for i in range(lo + 1, hi + 1):
		if arr[i] < pivot:
			arr[i], arr[swap_index] = arr[swap_index], arr[i]
			swap_index += 1
	
	arr[lo], arr[swap_index - 1] = arr[swap_index - 1], arr[lo]
	
	return swap_index -1
	



if __name__ == "__main__":
	arr = [2,7,5,1,3,4,6,9,8]
	quickSort(arr)
	print(arr)
