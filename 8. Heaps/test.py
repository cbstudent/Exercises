import heapq

class TestScore:
	def __init__(self, student_name, student_id, percent_score):
		self.student_name = student_name # string
		self.student_id = student_id  # integer
		self.precent_score = percent_score # integer
		

amy = TestScore("amy", 12, 80)
bob = TestScore("bob", 13, 92)
carl = TestScore("carl", 10, 95)
sam = TestScore("sam", 14, 84)

students_heap_tuple = []
heapq.heappush(students_heap_tuple, (amy.student_id, amy))
heapq.heappush(students_heap_tuple, (bob.student_id, bob))
heapq.heappush(students_heap_tuple, (carl.student_id, carl))
heapq.heappush(students_heap_tuple, (sam.student_id, sam))

# We print the student names in order of student_id.
while students_heap_tuple:
	print(heapq.heappop(students_heap_tuple)[1].student_name)
