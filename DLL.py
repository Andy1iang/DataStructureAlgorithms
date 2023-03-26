class Node:

	def __init__(self, data):
		self.data = data
		self.prev = None
		self.next = None

	def __str__(self):
		return str(self.data)


class DLL:

	def __init__(self):
		self.head = None
		self.tail = None
		self.count = 0

	def add_head(self, data):
		new_node = Node(data)
		self.count += 1
		if self.head is None:
			# if DLL is empty, instantiate head and tail node (same node)
			self.head = new_node
			self.tail = new_node
		else:
			new_node.next = self.head
			self.head.prev = new_node
			self.head = new_node

	def add_tail(self, data):
		new_node = Node(data)
		self.count += 1
		if self.tail is None:
			# if DLL is empty, instantiate head and tail node (same node)
			self.head = new_node
			self.tail = new_node
		else:
			new_node.prev = self.tail
			self.tail.next = new_node
			self.tail = new_node

	def traverse_forward(self):
		temp = self.head
		while temp is not None:
			print(temp)
			temp = temp.next

	def traverse_backward(self):
		temp = self.tail
		while temp is not None:
			print(temp)
			temp = temp.prev

	def reverse(self):
		curr_node = self.head
		temp = None

		while curr_node is not None:
			temp = curr_node.prev
			curr_node.prev = curr_node.next
			curr_node.next = temp
			curr_node = curr_node.prev

		self.head = temp.prev

	def remove(self, target):
		# O(N) time complexity
		if self.head is None:
			return None
		else:
			temp = self.head
			while temp is not None and temp.data != target:
				temp = temp.next

			if temp is None:
				return None

			elif self.count == 1:
				# if there's only one node, reset DLL by deleting that node
				self.head = None
				self.tail = None

			elif temp.prev is None:
				# disconnect new head node with previous node
				self.head = temp.next
				self.head.prev = None

			elif temp.next is None:
				# disconnect new tail node with previous node
				self.tail = temp.prev
				self.tail.next = None
			else:
				temp.prev.next = temp.next
				temp.next.prev = temp.prev

			self.count -= 1
			return temp

	def node_count(self):
		return self.count
