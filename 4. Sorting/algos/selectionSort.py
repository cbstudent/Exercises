def SelectionSort(arr):
	
	for i in range(len(arr)):
		
		min_num = arr[i]
		swap_index = i
		
		for j in range(i+1, len(arr)):
			if(arr[j] <= min_num):
				min_num = arr[j]
				swap_index = j
		
		tmp_si = arr[swap_index]
		tmp_i = arr[i]
		arr[i] = tmp_si
		arr[swap_index] = tmp_i
		


if __name__ == '__main__':
	
	# test cases
	arr = [10,6,8,4,8,5,1,3,7,9,8,2]
	
	SelectionSort(arr)
	
	print(arr)
