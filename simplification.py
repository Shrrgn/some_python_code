#for me

import keyword
import os

#__truediv__ only with import __future__

INVALID_CHARACTERS = "\\|?/.,:;!@#$%^&-`~<>'\"+=(){}[]1234567890 "
VALID_CHARACTERS = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnPpQqRrOoSsTtUuVvWwXxYyZz_*"
CLASS_NAME_LENGTH = 15
VARIABLE_NAME_LENGTH = 20
PROPERTIES = {"NO_PROPERTY": 0, "GETTER": 1, "SETTER": 2, "FULL_PROPERTY": 3}
MAGIC = ["__new__","__del__","__eq__","__ne__","__lt__","__gt__","__le__","__ne__","__pos__","__neg__","__abs__",
			"__invert__","__round__","__floor__","__ceil__","__trunc__","__add__","__sub__","__mul__","__div__","__floordiv__",
			"__mod__","__divmod__","__pow__","__lshift__","__rshift__","__and__","__or__","__xor__",
			"__radd__","__rsub__","__rmul__","__rdiv__","__rfloordiv__","__rmod__","__rdivmod__","__rpow__","__rlshift__",
		 	"__rshift__","__rand__","__ror__","__rxor__",
		 	"__iadd__","__isub__","__imul__","__idiv__","__ifloordiv__","__imod__","__idivmod__","__ipow__","__ilshift__",
		 	"__ishift__","__irand__","__ior__","__ixor__",
		 	"__int__","__float__","__long__","__complex__","__oct__","__hex__","__index__","__trunc__",
		 	"__str__","__repr__","__unicode__","__format__","__hash__","__bool__","__dir__","__sizeof__",
		 	"__getattr__","__setattr__","__delattr__","__getattribute__",
		 	"__len__","__getitem__","__setitem__","__delitem__","__iter__","__reversed__","__contains__","__missing__",
		 	"__instancecheck__","__subclasscheck__","__enter__","__exit__","__get__","__set__","__del__",
		 	"__copy__","__deepcopy__","__getinittargs__","__getnewargs__","__getstate__","__setstate__"]


def creating_class(class_name, parents):
	print("Creating class...")
	return "class {0}({1}):\n".format(class_name, ",".join(parents) if parents else "") #add abstract classes

def creating_constructor_head(variables, variables_with_default_values):
	print("Creating constructor...")
	
	defi = ", " + ", ".join([f"{k} = {v[0]}" for k,v in variables_with_default_values.items()]) if variables_with_default_values else ""
	v = ", " + ", ".join(variables.keys()) if variables else ""
	
	return f"\tdef __init__(self{v}{defi}):\n"

def creating_constructor_definition(variables, variables_with_default_values):
	return [f"\t\tself.__{i} = {i}\n" for i in list(variables.keys()) + list(variables_with_default_values.keys())] 
	
def creating_property(var, var_with_def):
	return [get_props(k,v) for k,v in var.items()] + [get_props(k,v[1]) for k,v in var_with_def.items()]

def creating_magic_methods(magic):
	print("Creating magic methods...")
	return [f"\n\tdef {k}(self{v}):\n\t\tpass\n" for k,v in magic.items()]

def creating_methods(): 
	pass

def enter_class_data():
	parents = []
	
	while 1:
		name_of_class = input("Write name of a class: ").lower().capitalize()

		if not name_of_class or is_invalid_length_or_chars(name_of_class, "class", CLASS_NAME_LENGTH): continue
		
		else: break

	while 1:
		is_parents = input("Does it class have parents? (y/n) ").lower()

		if is_parents == "n": break
		
		elif is_parents == "y":
			
			while 1:
				parent = input("Write name of a parent: ")
				
				if not parent: break

				elif is_invalid_length_or_chars(parent, "parent class", CLASS_NAME_LENGTH): continue
				
				else: parents.append(parent.lower().capitalize())
			break
		
		else: print("You should write 'y' or 'n'") 
	
	return (name_of_class, list(set(parents)))

def enter_constructor_data():
	variables = {}
	variables_with_default_values = {}

	while 1:
		var = input("\nWrite name of variable: ").lower()
		if not var: break

		if is_invalid_length_or_chars(var, "variable"): continue	

		else:
			prop = property_using()
			variables[var] = prop

	print("\nWrite name of variables with default values...")
	
	while 1:
		key = input("Enter a key: ").lower()
		if not key: break
		
		if is_invalid_length_or_chars(key, "key"): continue

		else:
			value = input("Enter a value: ")
			prop = property_using()
			variables_with_default_values[key] = value, prop		

	return (variables, variables_with_default_values)

def enter_magic():
	magic = {}
	
	while 1:
		method = input("Enter a method: ").lower()
		
		if not method: break
		
		elif method in MAGIC:
			args = input("Does it have argument? (y/n)")
			if args == "y":
				magic[method] = ",other"
			else:
				magic[method] = ""
		
		else:
			print("Method doesn't exist") 
	
	return magic
		
def get_constructor_data():
	return enter_constructor_data()	

def property_using():
	print("\nVariable doesn't need a property. Enter '0' (default).")
	print("Variable need only a getter. Enter '1'.")
	print("Variable need only a setter. Enter '2'.")
	print("Variable need setter and getter. Enter '3'.")
	
	prop = input("Enter a digit for property: ")
	
	if prop == "1": 
		prop = PROPERTIES["GETTER"]
	elif prop == "2":
		prop = PROPERTIES["SETTER"]
	elif prop == "3":
		prop = PROPERTIES["FULL_PROPERTY"]
	else:
		prop = PROPERTIES["NO_PROPERTY"] 
	
	return prop

def get_props(variable, prop):
	#if PROPERTIES["NO_PROPERTY"] == prop: pass
	
	if PROPERTIES["GETTER"] == prop:
		return "\n\t@property\n\tdef {0}(self):\n\t\treturn self.__{0}\n".format(variable)
	
	elif PROPERTIES["SETTER"] == prop:
		return "\n\t@{0}.setter\n\tdef {0}(self, value):\n\t\tself.__{0} = value\n".format(variable)
	
	else:
		return "\n\t@property\n\tdef {0}(self):\n\t\treturn self.__{0}\n".format(variable) + "\n\t@{0}.setter\n\tdef {0}(self, value):\n\t\tself.__{0} = value\n".format(variable)

def is_invalid_characters(data):
	return False if any([i in INVALID_CHARACTERS or i not in VALID_CHARACTERS for i in data]) else True

def is_invalid_length_or_chars(value, name, length = VARIABLE_NAME_LENGTH):
	if len(value) >= length:
		print(f"Name {name} is too big")
		return True

	elif keyword.iskeyword(value):
		print(f"You can't use it because '{name}' is keyword.")
		return True
			
	elif any([not is_invalid_characters(i) for i in value]):
		print(f"Name {name} has invalid characters.")
		return True
	
	else: 
		return False


def main():
	class_name, parents = enter_class_data()
	variables, variables_with_default_values = get_constructor_data()
	magic_methods = enter_magic()

	mode = 'w'
	make_empty = True

	while 1:
		if make_empty:
			file = input('Enter name of file: ')
		else:
			break
		
		if os.path.exists(file):
			while 1:
				print("Do you wanna add new class to end of existing file or rewrite file or make new?")
				choose = input("Enter 'n' for new, 'r' for rewrite, 'a' for add in the end: ").lower()
				
				if choose == "a":
					mode = 'a'
					make_empty = False
					break
				
				elif choose == "r":
					make_empty = False
					break
				
				elif choose == "n": break
				
				else: print("Wrong choose!")
		else:
			break

	try:
		with open(file, mode) as f:
			f.write("\n" + creating_class(class_name, parents) + "\n") #add abstract classes)
			f.write(creating_constructor_head(variables, variables_with_default_values))
			
			for i in creating_constructor_definition(variables, variables_with_default_values):
				f.write(i)

			for i in creating_property(variables, variables_with_default_values):
				f.write(i)

			for i in creating_magic_methods(magic_methods):
				f.write(i)

	except OSError:
		print("Something wrong from 'os' module")

	finally:
		print("Done...")


#creating_class()
#creating_constructor()
#creating_property()
main()