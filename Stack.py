# LIFO (Last in first out) structure

class Stack:

	def __init__(self):
		self.stack = []

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		# O(1) Running Time
		if not self.is_empty():
			return self.stack.pop()
		else:
			return None

	def peek(self):
		# O(1) Running Time
		if not self.is_empty():
			return self.stack[-1]
		else:
			return None

	def is_empty(self):
		# O(1) Running Time
		return self.stack == []

	def __len__(self):
		return len(self.stack)
