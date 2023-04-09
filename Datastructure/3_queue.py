class Queue:
	def __init__(self, size):
		self.size = size
		self.queue = ['' for _ in range(size)]
		self.front = 0
		self.rear = 0
		
	def move(self, val):
		return (val+1)%self.size
		
	def join(self, ele):
		if self.is_filled():
			print('The queue is filled!')
		else:
			self.rear = self.move(self.rear)
			self.queue[self.rear] = ele
		
	def get_front(self):
		if self.front == self.rear:
			return 'The queue is empty!'
		else:
			return self.queue[self.front+1]
		
	def pop(self):
		if not self.is_empty():
			self.front = self.move(self.front)
			return self.queue[self.front]
		else:
			return 'The queue is empty!'
		
	def is_empty(self):
		return self.front == self.rear
	
	def is_filled(self):
		return (self.rear+1)%self.size == self.front
