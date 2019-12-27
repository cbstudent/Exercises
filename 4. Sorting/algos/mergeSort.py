def mergeSort(arr):
	_mergeSort(arr, 0, len(arr)-1)
	

def _mergeSort(arr, lo, hi):
	
	if lo >= hi:
		return
	
	# get midpoint
	mid = (lo + hi) // 2
	
	# left half
	_mergeSort(arr, lo, mid)
	
	# right half
	_mergeSort(arr, mid + 1, hi)
	
	# merge both
	merge(arr, lo, mid, hi)
	

def merge(arr, start_1, start_2, end_2):
	copy = arr[:]
	cur = start_1
	p1 = start_1
	p2 = start_2

	while(cur <= end_2):
		if p1 < start_2 and p2 <= end_2:
			if copy[p1] < copy[p2]:
				arr[cur] = copy[p1]
				p1 += 1
			else:
				arr[cur] = copy[p2]
				p2 += 1
		elif p1 < start_2:
			arr[cur] = copy[p1]
			p1 += 1
		else:
			arr[cur] = copy[p2]
			p2 += 1
		
		cur += 1




if __name__ == "__main__":
	
	arr = [3,4,0,1,5,6,9,8,7,2]
	
	mergeSort(arr)
	
	print(arr)
