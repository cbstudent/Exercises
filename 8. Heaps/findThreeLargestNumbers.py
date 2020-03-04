import heapq

def findThreeLargestNumbers(array):
    # Write your code here.
	
	#O(N lg 3) solution using heapq lib
	#arr = []
	#
	#for i in range(3):
	#	heapq.heappush(arr, array[i])
	#
	#for i in range(3,len(array)):
	#	if(arr[0] < array[i]):
	#		heapq.heappop(arr)
	#		heapq.heappush(arr, array[i])
	#
	#res = []
	#while arr:
	#	res.append(heapq.heappop(arr))
	#
	#return res
	
	
	#O(N) solution without library
	arr = [None, None, None]
	
	for i in array:
		if arr[2] is None or i > arr[2]:
			shiftArr(arr, i, 2)
		elif arr[1] is None or i > arr[1]:
			shiftArr(arr, i, 1)
		elif arr[0] is None or i > arr[0]:
			shiftArr(arr, i, 0)
	return arr
	
def shiftArr(arr, num, idx):
	if idx == 0:
		arr[0] = num
	if idx == 1:
		arr[0] = arr[1]
		arr[1] = num
	if idx == 2:
		arr[0] = arr[1]
		arr[1] = arr[2]
		arr[2] = num
	
	
	
	
	
	
	
