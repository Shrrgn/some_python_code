#my stack

class MyStack:

	def __init__(self, *data):
		if not data:
			self.__data = []
		else:
			self.__data = list(data)

	def push(self, data):
		self.__data.append(data)

	def pop(self):
		if not self.__data:
			raise IndexError("My stack is empty") 
		else: 
			 del self.__data[-1]

	def __len__(self):
		return len(self.__data)

	size = __len__

	def __iter__(self):
		return iter(self.__data)

	def pip(self):
		for i in self.__data: print(i)


a = MyStack(5,6,7)
a.push(9)
a.pip()
