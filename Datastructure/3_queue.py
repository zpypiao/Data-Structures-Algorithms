class Queue:
	def __init__(self, l):
		self.l = l
		self.queue = ['' for _ in range(l)]
		self.front = 0
		self.rear = l-1
		
	def move(self, val):
		if val == self.l-1:
			return 0
		else:
			return val+1
	def remove(self, val):
		if val == 0:
			return self.l - 1
		else:
			return val - 1
		
	def join(self, ele):
		self.rear = self.move(self.rear)
		self.queue[self.rear] = ele
		
	def get_front(self):
		if self.front == self.rear:
			return None
		else:
			return self.queue[self.front+1]
		
	def pop(self):
		if self.front == self.rear:
			return None
		else:
			self.front = self.move(self.front)
			return self.queue[self.remove(self.front)]
