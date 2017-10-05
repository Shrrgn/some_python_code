#class that workiimg with complex numbers

class Complex:
	def __init__(self, real = 0.0, imaginary = 0.0):
		self.real = real
		self.imaginary = imaginary
	
	def __repr__(self):
		return "Complex({!r},{!r})".format(self.real,self.imaginary)
		
	def __str__(self):
		return "{}{:+d}i".format(self.real,self.imaginary)
		
	def __add__(self, other):
		return Complex(self.real + other.real, self.imaginary + other.imaginary)
		
	def __neg__(self):
		return Complex(-self.real, -self.imaginary)
		
	def __sub__(self, other):
		return self + (-other)
	
	def __abs__(self):
		return (self.real ** 2 + self.imaginary ** 2) ** 0.5

	def __eq__(self, other):  #for == and !=
		return self.real == other.real and self.imaginary == other.imaginary
	
if __name__ == "__main__":
	print(Complex(2,3) - Complex(2,1))
	print(abs(Complex(3,4)))
	print(Complex(3,4) != Complex(4,4))