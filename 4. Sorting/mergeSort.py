def mergeSort(array):
	_mergeSort(array, 0, len(array) - 1)
	return array

def _mergeSort(array, lo, hi):
	if lo >= hi:
		return
	
	mid = (lo + hi) // 2 + 1
	
	_mergeSort(array, lo, mid - 1)
	
	_mergeSort(array, mid, hi)
	
	merge(array, lo, mid, hi)
	
def merge(array, lo, mid, hi):
	copy = array[:]
	p1 = lo
	p2 = mid
	cur = lo
	
	while cur <= hi:
		if p1 < mid and p2 <= hi:
			if copy[p1] < copy[p2]:
				array[cur] = copy[p1]
				p1 += 1
			else:
				array[cur] = copy[p2]
				p2 += 1			
		elif p1 < mid:
			array[cur] = copy[p1]
			p1 += 1
		else:
			array[cur] = copy[p2]
			p2 += 1
			
		cur += 1
	
