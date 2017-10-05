#transaction and bank account

CURRENCY_LIST_COURSE = {"USD":1,"GRN":0.04,"EURO":1.05,"RUB":0.013,"ZLT":0.25}
NUMBER_BANK_BOOK_LENGTH = 12
TRANSACTION_NUMBER_LENGTH = 10
DESCRIPTION_LENGTH = 256
PHONE_NUMBER_LENGTH = 12

class Transaction:

	def __init__(self, transaction_number, amount, date, currency="USD", description = None):

		if type(transaction_number) != str:
			raise TypeError("Value must be string.")
		elif len(transaction_number) != TRANSACTION_NUMBER_LENGTH:
			raise ValueError("Value must be equal to 10 symbols.")
		else:
			self.__transaction_number = transaction_number

		if amount is not None and amount >= 0:
			self.__amount = float(amount)
		else:
			raise ValueError("Amount must be equal or bigger then zero.")

		self.__date = date

		if len(currency) > 4 or currency not in CURRENCY_LIST_COURSE:
			raise ValueError("Currency value must be not bigger than 4 symbols and exist in CURRENCY_LIST.")
		else:
			self.__currency = currency
			self.__course = float(CURRENCY_LIST_COURSE[currency])

		if description != None and len(description) > DESCRIPTION_LENGTH:
			self.__description = description[:(DESCRIPTION_LENGTH - 1)]
		else:
			self.__description = description

	@property
	def transaction_number(self):      #unique
		return self.__transaction_number

	@property
	def amount(self):
		return self.__amount

	@property
	def date(self):
		return self.__date

	@property
	def currency(self):
		return self.__currency

	@property
	def course(self):
		return self.__course

	@property
	def description(self):
		return self.__description

	def __str__(self):
		return """Transaction number - '{0}', amount = {1}, date of transaction - {2},
                     \rcurrency - {3}, course = {4},\ndescription - '{5}'""".format(self.transaction_number,
																					self.amount,
																					self.date,
																					self.currency,
																					self.course,
																					self.description)

	def usd(self):
		return self.__amount * self.__course

class Account:

	def __init__(self, number_bank_book, name_bank_book, *transaction_list):

		if len(number_bank_book) == NUMBER_BANK_BOOK_LENGTH:
			self.__number_bank_book = number_bank_book
		else:
			raise ValueError("Length should be equal to 12 symbols")

		if len(name_bank_book) > 6:
			self.__name_bank_book = name_bank_book
		else:
			raise ValueError("Firstname and secondname must be not empty and doesn't have digits.")

		if transaction_list:
			self.__transaction_list = []
			for tr in list(transaction_list):
				if isinstance(tr,Transaction):
					self.__transaction_list.append(tr)
				else:
					continue
		else:
			self.__transaction_list = []

		self.__phone_number = None

	@property
	def number_bank_book(self):
		return self.__number_bank_book

	@property
	def name_bank_book(self):
		return self.__name_bank_book

	@name_bank_book.setter
	def name_bank_book(self,value):
		if 4 <= len(value) <= 20:
			self.__name_bank_book = value
		else:
			raise ValueError("Length should be bigger than 4 symbols.")

	@property
	def transaction_list(self):
		return [tr.transaction_number for tr in self.__transaction_list]

	@property
	def phone_number(self):
		return self.__phone_number

	@phone_number.setter
	def phone_number(self, value):
		if len(value) == PHONE_NUMBER_LENGTH and all(i.isdigit() for i in value):
			self.__phone_number = value
		else:
			raise ValueError("Phone number must be not empty and  have only digits.")

	def __len__(self): 
		return len(self.__transaction_list)

	transaction_quantity = __len__

	"""
	def __iter__(self):
		return iter(self.__transaction_list)

	def __getitem__(self,index):
		return self.__transaction_list[index]
	"""

	def balance(self):
		return sum(tr.amount * tr.course for tr in self.__transaction_list)

	def all_usd(self):
		return all(tr.currency == "USD" for tr in self.__transaction_list)

	def add_transaction(self, amount, date, currency = "USD", course = 1, description = None):
		self.__transaction_list.append(Transaction(amount, date, currency, course, description))

	def delete_transaction(self,number):
		for tr in self.__transaction_list:
			if tr.transaction_number == number:
				index = self.__transaction_list.index(tr)
				del self.__transaction_list[index]
				break
		else:
			raise AttributeError("Invalid number of transaction")

	def delete_all_transaction(self):
		while self.__transaction_list != []:
			del self.__transaction_list[-1]


	def transaction_info(self):
		for tr in self.__transaction_list:
			print("Number = {0}, amount = {1}, date = {2},currency = {3},course = {4}".format(tr.transaction_number,
																								tr.amount,
																								tr.date,
																								tr.currency,tr.course))

	def __str__(self):
		return "Number of bank book - {0}, Name of bank book - {1},\ntransaction_list - {2}".format(self.number_bank_book,
																									self.name_bank_book,
																									self.transaction_list)




t1 = Transaction("021fr34g45",5800,"16.02.13","GRN")
t2 = Transaction("0879sdft45",640,"18.12.13")

ted = Account("789698757898","Marco Phoenix",t1,t2)
ted.add_transaction("rot7891245",3000, "16.11.14", "GRN")
ted.add_transaction("789dfsd545",2000,"12.13.15","GRN")

ted.transaction_info()
print(ted.balance())
print(ted.transaction_list)
#ted.delete_all_transaction()
print(ted.transaction_list)
print("---------------")
print(ted)

t3 = Transaction("021fr34gkl",0,"16.02.13","GRN")
print(t3)
jinny = Account("dsfwer456123","Jinny Wisley",Transaction("1234567890",4000,"08.11.12"))
print(jinny.all_usd())

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#u1 = UserBank("1234567890123456","Leroy","Jenkins","380981234569",ted)
#u2 = UserBank("1122334455667788","Laxus","Dreyadr","380456789566",jinny)
#print(u1.account)
