class Stack:
    def __init__(self):
        self.stack = []

    def push(self, ele):
        self.stack.append(ele)

    def pop(self):
        if len(self.stack):
            return self.stack.pop()
        else:
            return None

    def get_pop(self):
        if len(self.stack):
            return self.stack[-1]
        else:
            return None

def isValid(s: str) -> bool:
	stack = Stack()
	match={')':'(', ']':'[', '}':'{'}
	for ch in s:
		if ch in {'(', '[', '{'}:
			stack.push(ch)
		else:
			if match[ch] == stack.get_pop():
				stack.pop()
			else:
				return False

	if stack.stack == []:
		return True
	else:
		return False		
