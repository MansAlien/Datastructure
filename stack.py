class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class stack:
	def __init__(self):
		self.head = None

	def add(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
		else:
			current = self.head
			while current.next is not None:
				current = current.next

			current.next = new_node


	def print(self):
		if self.head is None:
			print("this stack is empty")
		else:
			current = self.head
			while current is not None:
				print(current.data, end=" --> ")
				current = current.next
			print()


s1 = stack()
s1.add(10)
s1.add(20)
s1.print()
