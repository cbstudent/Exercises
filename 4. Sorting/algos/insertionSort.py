def insertionSort(arr):
	
	for i in range(1, len(arr)):
		for j in range(i,0,-1):
			if arr[j] < arr[j-1]:
				tmpj = arr[j]
				tmpjm1 = arr[j-1]
				arr[j] = tmpjm1
				arr[j-1] = tmpj
			else:
				break

	
	
	
	
if __name__ == "__main__":
	arr = [4,3,7,6,5,1,2,9,8]
	insertionSort(arr)
	print(arr)
