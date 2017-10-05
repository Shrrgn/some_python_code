#Kramer
import numpy as np

class Kramer:
	
	def __init__(self, matrix, vector):
		
		if matrix.shape[0] == matrix.shape[1] and np.linalg.det(matrix) != 0:
			self.__A = matrix
			self.__matrixDet = np.linalg.det(self.__A)
		else:
			raise ValueError("Matrix hasn't square shape or det = 0")
	
		if matrix.shape[0] == vector.shape[1]:
			self.__b = vector
		else:
			raise ValueError("Vector rows must be equal to matrix rows")
			
		self.__X = np.zeros_like(self.__b, dtype = float)
		self.calculate()
		self.printX()
			
	@property
	def A(self):
		return self.__A #inner matrix
		
	@property
	def b(self):
		return self.__b #vector
	
	def calculate(self):
		for i in range(self.__b.shape[1]):
			M = self.__A.copy()
			M[:,i] = self.__b
			self.__X[:,i] = np.linalg.det(M)/self.__matrixDet
		return self.__X
	
	def printX(self):
		print(self.__X)
		

kr = Kramer(np.array([[1,1,1],[2,-1,-4],[3,4,8]]), np.array([[3,25,4]]))
#kr.calculate()
