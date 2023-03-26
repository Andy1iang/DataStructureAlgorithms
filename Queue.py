# FIFO (First in First out) structure
# Doubly Linked List could be used for O(1) running time for both enqueue and dequeue method

class Queue:

	def __init__(self):
		self.queue = []

	def is_empty(self):
		return self.queue == []

	def enqueue(self, data):
		# O(1) running time
		self.queue.append(data)

	def dequeue(self):
		# O(N) running time
		if len(self.queue) == 0:
			return None
		return self.queue.pop(0)

	def peek(self):
		# O(1) running time
		return self.queue[0]

	def __len__(self):
		return len(self.queue)
