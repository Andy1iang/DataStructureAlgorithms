class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

	def __str__(self):
		return str(self.data)


class SLL:

	def __init__(self):
		self.head = None
		self.nodes_count = 0

	def insert_start(self, data):
		# O(1) running time
		self.nodes_count += 1
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
		else:
			new_node.next = self.head
			self.head = new_node

	def insert_end(self, data):
		# O(N) running time
		self.nodes_count += 1
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
		else:
			temp = self.head
			while temp.next is not None:
				temp = temp.next
			temp.next = new_node

	def traverse(self):
		# O(N) running time
		temp = self.head
		while temp is not None:
			print(temp)
			temp = temp.next

	def reverse(self):
		# O(N) running time
		curr_node = self.head
		prev_node = None
		next_node = None
		while curr_node is not None:
			# setting next node variable to the next node
			next_node = curr_node.next
			# setting the actual current node's next link to the previous node (reverse)
			curr_node.next = prev_node
			# sitting previous node variable to current node
			prev_node = curr_node
			# sitting current node variable to the next node
			curr_node = next_node

		# setting the head node variable to the last node (current node is None, prev is last node)
		self.head = prev_node

	def remove(self, data):
		# O(N) running time
		if self.head is None:
			return None
		else:
			temp = self.head
			prev = None

			while temp is not None and temp.data != data:
				prev = temp
				temp = temp.next

			if temp is None:
				return None

			self.nodes_count -= 1
			if prev is None:
				self.head = temp.next
			else:
				prev.next = temp.next

			return temp

	def list_size(self):
		return self.nodes_count
