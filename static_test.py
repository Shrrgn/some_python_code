
class Teststatic():

	db = []

	def __init__(self, smth):
		Teststatic.db.append(smth)

	@property
	def smth(self):
		return self.__smth

	@smth.setter
	def smth(self, value):
		self.__smth = value

	@staticmethod
	def add(smth):
		Teststatic.db.append(smth)

	@staticmethod
	def delete(smth):
		Teststatic.db.pop(smth)

	def about(self):
		print(Teststatic.db)


d = Teststatic(4)
d.add(5)
d.about()
a = Teststatic(8)
a.add(10)
a.about()