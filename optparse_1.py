#optparse_1
from optparse import OptionParser

def main():
	parser = OptionParser()
	parser.add_option("-p", "--pow", dest = "pow1", type = "int", action = "callback",
						callback = pow1, help = ("pow of digit"))
	parser.add_option("-d", "--double", dest = "double", type = "int", action = "callback",
						callback = double, help = ("double a digit"))
	opts, args = parser.parse_args()
	#print(opts)
	#print(args)

def pow1(option, opt_str, value, parser): 
	print(value ** 2)

def double(option, opt_str, value, parser): 
	print(value * 2)

#main()

class WorkWithNumbers:
	
	def __init__(self):
		parser = OptionParser()
		parser.add_option("-p", "--pow", dest = "pow2", type = "int", action = "callback",
							callback = self.pow2,  help = ("pow of digit"))
		parser.add_option("-d", "--double", dest = "double2", type = "int", action = "callback",
							callback = self.double2, help = ("double a digit"))
		opts, args = parser.parse_args()
		print(opts)
		print(args)


	def pow2(self,option, opt_str, value, parser):
		print(value ** 2)

	def double2(self,option, opt_str, value, parser):
		print(value * 2)

w = WorkWithNumbers()