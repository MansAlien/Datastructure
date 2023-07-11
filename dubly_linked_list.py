class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.pre = None


class doubly_linked_list:
	def __init__(self):
		self.head = None

	def add_empty(self, data):
		if self.head is None:
			new_node = Node(data)
			self.head = new_node
		else:
			print("Linked list is not empyt!")

	def display(self):
		if self.head is None:
			print("linked list is empty!")
		else:
			current = self.head
			while current is not None:
				print(current.data, end=" --> ")
				current = current.next


l1 = doubly_linked_list()
l1.add_end(10)
l1.display()