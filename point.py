
import math

class Point(object):

    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    @property
    def getX(self):
        return self.__x

    @property
    def getY(self):
        return self.__y


    def distance_from_origin(self):
        return math.hypot(self.getX, self.getY)

    def __eq__(self, other):
        return self.getX == other.getX and self.getY == other.getY

    def length_from_center(self):
        return math.sqrt(self.getX ** 2 + self.getY ** 2)

    #__len__ = length_from_center

    def __repr__(self):
        return "Point({0.getX!r},{0.getY!r})".format(self)

    def __str__(self):
        return "({0.getX!r},{0.getY!r})".format(self)

class Circle(Point):

    def __init__(self, radius, x = 0, y = 0):
        super().__init__(x, y)
        self.__radius = radius


    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self,value):
        if value > 0:
            self.__radius = value
        else:
            raise ValueError("Radius must be bigger than zero.")


    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        return self.radius == other.radius and super().__eq__(other)

    def __repr__(self):
        return "Circle(Radius = {0.radius!r}; center = {0.x!r},{0.y!r})".format(self)

    __str__ = __repr__

    def volume(self):
        return (4 * math.pi * (self.radius ** 3))/3

    def about(self):
        print("Circumference = {0},\nArea = {1},\nVolume = {2}\n".format(self.circumference(),
                                                                           self.area(),
                                                                           self.volume()))



a = Point()
b = Point(3,4)
print(a)
print(b)
print(b.length_from_center())
print(a == b)
print(b.__repr__())
print("+++++++++++++++++")
"""
c = Circle(5,3,4)
print(c)
c.about()
d = Circle(5,3,4)
print(c == d)
"""
