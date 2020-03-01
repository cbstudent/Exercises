# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
        
		queue = []
		
		array.append(self.name)
		for i in self.children:
				queue.append(i)
				
		while queue:
			cur = queue.pop(0)
			array.append(cur.name)
			for i in cur.children:
				queue.append(i)
		return array
				
			
			
