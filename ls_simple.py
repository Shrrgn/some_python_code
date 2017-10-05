#ls

import os
from optparse import OptionParser


#def files_list(path = ".", end = ""):
#	return os.listdir(path) if end == "" else [i for i in os.listdir(path) if i.endswith(end)]

def info(path = ".", end = ".txt"):
	files_list = os.listdir(path) if end == "" else [i for i in os.listdir(path) if i.endswith(end)]
	list_info = []
	
	for i in files_list:
		list_info.append({'name' : i, 'size' : os.stat(i).st_size, 'modified' : os.stat(i).st_mtime, 'creation' : os.stat(i).st_ctime})
	#for i in list_info:
	#	print("{0}||{1}||{2}".format(i['name'], i['size'], i['creation']))
	return list_info

def sort1(order = "n"):
	if order == "n":
		#print(sorted(info(), key = lambda x: x['name']))
		for i in sorted(info(), key = lambda x: x['name']):
			print("{0}  ||  {1}  ||  {2}".format(i['name'], i['size'], i['creation']))
	elif order == 's':
		for i in sorted(info(), key = lambda x: x['size']):
			print("{0}  ||  {1}  ||  {2}".format(i['name'], i['size'], i['creation']))
	elif order == 'c':
		for i in sorted(info(), key = lambda x: x['creation']):
			print("{0}  ||  {1}  ||  {2}".format(i['name'], i['size'], i['creation']))

def modified():
	for i in sorted(info(), key = lambda x: x['modified']):
		print("{0}   ||   {1}".format(i['name'],i['modified']))



modified()