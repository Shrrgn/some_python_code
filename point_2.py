
import math

class Point:

	def __init__(self, x = 0, y = 0, z = None):
		if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
			self.__x = x
			self.__y = y
			if z is None or type(z) == int or type(z) == float: #what the fuck?
				self.__z = z
			else:
				raise ValueError("zzzzz")
		else:
			raise ValueError("x and y should have int or float type")

	@property
	def x(self):
		return self.__x

	@property
	def y(self):
		return self.__y

	@property
	def z(self):
		return self.__z

	def __add__(self, other):
		if self.z is None:
			return Point(self.x + other.x, self.y + other.y)
		else:
			return Point(self.x + other.x, self.y + other.y, self.z + other.z)

	def __repr__(self):
		return "Point({0.x!r},{0.y!r},{0.z!r})".format(self)

	def __str__(self):
		return "({0.x!r},{0.y!r},{0.z!r})".format(self)

	def __neg__(self):
		if self.z is None:
			return Point(-self.x, -self.y)
		else:
			return Point(-self.x, -self.y, -self.z)

	def __mul__(self, scalar):
		if self.z is None:
			Point(self.x * scalar, self.y * scalar)
		else:
			return Point(self.x * scalar, self.y * scalar, self.z * scalar)

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y and self.z == other.z

	def distance_from_origin(self):
		return math.hypot(self.x, self.y)


class Shape:
	def __init__(self, *points):
		if all(isinstance(i, Point) for i in points):
			self.__points = list(points)
		else:
			raise ValueError("Arguments should be an instance of Point class")
		
		self.__sides = self.calculate_sides()

	def what_shape(self):
		if len(self.__points) == 2:
			print("It is line or vector")
		
		elif len(self.__points) == 3:
			self.check_triangle()
		
		else:
			pass


	def length(self, point1, point2):
		return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)

	def calculate_sides(self):
		sides = []
		i = 0
		
		while 1:
			if i == (len(self.__points) - 1):
				sides.append(self.length(self.__points[i], self.__points[0]))
				break
			else:
				sides.append(self.length(self.__points[i], self.__points[i + 1]))
			i += 1
		
		return [round(i, 3) for i in sides]

	@staticmethod
	def square_circle(radius):
		return round(math.pi * (radius ** 2), 3)

	@staticmethod
	def circumference(radius):
		return round(2 * math.pi * radius, 3)

	@property
	def sides(self):
		return self.__sides
	"""
	def sorting(self):
		return self.sides.sort()
	"""
	def check_triangle(self):
		print("checking...")
		return all([self.sides[0] + self.sides[1] > self.sides[2], self.sides[1] + self.sides[2] > self.sides[0], self.sides[0] + self.sides[2] > self.sides[1]])


SHAPES_OF_TRIANGLE = {"ORDINARY" : 0, "REGURAL" : 1, "EQUILATERAL" : 2, "ISOSCELES" : 3}

class Triangle:

	def __init__(self, point1, point2, point3):
		if Shape(point1, point2, point3).check_triangle():
			self.__point1 = point1
			self.__point2 = point2
			self.__point3 = point3
		else:
			raise ValueError("Points doesn't make a triangle")
		
		self.__a, self.__b, self.__c = sorted(Shape(point1, point2, point3).sides)
		self.__shape_of_triangle = self.triangle_shape()
		self.__alpha, self.__beta, self.__gamma = self.get_angles()
	
	def triangle_sides(self):
		return [self.a, self.b, self.c]
	
	@property
	def alpha(self):
		return self.__alpha

	@property
	def beta(self):
		return self.__beta

	@property
	def gamma(self):
		return self.__gamma

	@property
	def a(self):
		return self.__a

	@property
	def b(self):
		return self.__b

	@property
	def c(self):
		return self.__c

	@property
	def shape(self):
		return self.__shape_of_triangle

	def get_angles(self):
		return [self.find_angle(self.b, self.c, self.a), self.find_angle(self.a, self.c, self.b), self.find_angle(self.a, self.b, self.c)]

	def find_angle(self, a,b,c):
		return round(math.degrees(math.acos(((a ** 2 + b ** 2) - c ** 2) / (2 * a * b))), 3)

	def perimetr(self):
		return round(self.a + self.b + self.c, 3)

	def half_perimetr(self):
		return self.perimetr() / 2

	def square(self):
		if SHAPES_OF_TRIANGLE["ORDINARY"] == self.shape:
			return math.sqrt(self.half_perimetr() * (self.half_perimetr() - self.a) * (self.half_perimetr() - self.b) * (self.half_perimetr() - self.c))
		
		elif SHAPES_OF_TRIANGLE["REGULAR"] == self.shape:
			return 0.5 * self.a * self.b
		
		elif SHAPES_OF_TRIANGLE["EQUILATERAL"] == self.shape:
			return ((self.a ** 2) * math.sqrt(3)) / 4
		
		elif SHAPES_OF_TRIANGLE["ISOSCELES"] == self.shape:
			return 0.5 * self.a * self.c * math.sin(self.beta)
		
		else:
			raise Exception("Something wrong")

	def radius_inner_circle(self):
		return self.square() / self.half_perimetr()

	def square_inner_cicle(self):
		return round(Shape.square_circle(self.radius_inner_circle()), 3)
	
	def radius_outer_circle(self):
		return (self.a * self.b * self.c) / (4 * self.square())

	def square_outer_circle(self):
		return round(Shape.square_circle(self.radius_outer_circle()), 3)		

	def triangle_shape(self):
		if self.a == self.b == self.c:
			return SHAPES_OF_TRIANGLE["EQUILATERAL"]
		
		elif self.a == self.b:
			return SHAPES_OF_TRIANGLE["ISOSCELES"]
		
		elif (self.a ** 2 + self.b ** 2) == self.c ** 2:
			return SHAPES_OF_TRIANGLE["REGULAR"]
		
		else:
			return SHAPES_OF_TRIANGLE["ORDINARY"]

	def __eq__(self, other):
		return self.a == other.a and self.b == other.b and self.c == other.c

	def about(self):
		print("Triangle has a side 'a' = {0.a}, side 'b' = {0.b}, side 'c' = {0.c}".format(self))


a = Point(0, 0)
b = Point(3, 6)
c = Point(0, 3)
d = Point(0,3,1)
print(d)
print(a)
#print(a + b)
#print(-a)
dd = Shape(a,b,c)
print(dd.sides)
#print(dd.check_triangle())
tr = Triangle(a,b,c)
print(tr.triangle_sides)
print(tr.get_angles())
print(tr.square())
tr2 = Triangle(a,b,c)
print(tr == tr2)
tr.about()
print(tr.square_outer_circle())
print("--------------------")
x,y,z = Point(0,0), Point(4,7), Point(0,4)
xyz = Triangle(x,y,z)
print(xyz.square_outer_circle())