class MaxPriorityQueue:

	def __init__(self):
		self.arr = [None]
	
	def insert(self, key):
		self.arr.append(key)
		self.swim()

	def swim(self):		
		idx = len(self.arr) - 1
		
		while(idx//2 > 0 and self.arr[idx//2] < self.arr[idx]):
			self.arr[idx//2], self.arr[idx] = self.arr[idx], self.arr[idx//2]
			idx = idx // 2

	def get_max(self):
		return self.arr[1]

	def del_max(self):
		self.arr[1], self.arr[len(self.arr)-1] = self.arr[len(self.arr)-1], self.arr[1]
		maxitem = self.arr.pop()
		self.sink()
		return maxitem		

	def sink(self):
		idx = 1
		
		while(idx * 2 < len(self.arr)):
			curr = self.arr[idx]
			left = self.arr[idx * 2]
			right = float('-inf')
			if (idx * 2 + 1 < len(self.arr)):
				right = self.arr[idx * 2 + 1]
			if curr >= left and curr >= right:
				return 
			if left > right:
				self.arr[idx * 2], self.arr[idx] = self.arr[idx], self.arr[idx * 2]
				idx = idx * 2
			else:
				self.arr[idx * 2 + 1], self.arr[idx] = self.arr[idx], self.arr[idx * 2 + 1]
				idx = idx * 2 + 1

	def is_empty(self):
		return len(self.arr) == 1
		
	def size(self):
		return len(self.arr) - 1

def heapSort(arr):
	pq = MaxPriorityQueue()
	
	for i in arr:
		pq.insert(i)	
	
	idx = len(arr) - 1
	
	while not pq.is_empty():
		arr[idx] = pq.del_max()
		idx -= 1	

if __name__ == '__main__':
	arr = [1,6,2,3,8,240,109,-2,8]
	heapSort(arr)
	print(arr)
