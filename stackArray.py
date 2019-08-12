from exceptions import Empty
class StackArray:
	
	
	def __init__(self):
		self._data= []
		
	def __len__(self):
		return len(self._data)
	
	def is_empty(self):
		return len(self._data) == 0
		
	def push(self,e):
		self._data.append(e)
	
	def pop(self):
		if self.is_empty():
			raise Empty('Stack is empty')
		return self._data.pop()

	def top(self):
		if self.is_empty():
			raise Empty('Stack is empty')
		return self._data[-1]

	
s = StackArray()
s.push(20)
s.push(30)
print('Stack: ', s._data)	
print('Top Element: ' ,s.top())
s.push(40)
s.push(50)
print('Stack: ', s._data)
print('Popped the element from the stack :' , s.pop())
