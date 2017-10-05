#FCM-mod
import numpy as np
import cv2
import time
from math import fabs

#Exceptions
class ImageError(Exception):pass
class LoadImageError(ImageError):pass
class SaveImageError(ImageError):pass


class FCM:
	
	def __init__(self,file,clusters = 5,max_iterations = 100,error = 0.00001, m = 2):
		
		if all(list(map(lambda x: type(x) == int, (clusters, max_iterations, m)))) and type(error) == float:
		
			if 5 <= clusters <= 50:
				self.__clusters = clusters
			else:
				raise ValueError("Quantity of clusters should be from 5 to 50.")
		
			if 10 <= max_iterations <= 500:
				self.__max_iter = max_iterations
			else:
				raise ValueError("Quantity of iterations should be from 10 to 500.")
		
			if 0 < error < 1:
				self.__error = error
			else:
				raise ValueError("Error should be from 0 to 1")
			
			if m > 0:
				self.__m = m #exponential weight
			else:
				raise ValueError("The exponential weight should be bigger than zero.")
		
		else:
			raise TypeError("Clusters, max_iterations, m - should have int type, error - float.")
		
		
		self.__image = cv2.imread(file)
		if self.__image is not None:
			self.__data = self.__image.reshape(self.__image.shape[0]*self.__image.shape[1], self.__image.shape[2])
		else:
			raise LoadImageError("Can't find a file.")
		
		
		
	def vector_of_begining_centres(self, data, clusters):
		V0 = np.zeros((clusters,data.shape[1]))
		data_rows,data_chanels = data.shape
		steps = round(data_rows/clusters)
		
		for c in range(data_chanels):
			k = 0
			for i in range(clusters):
				if k > data_rows:
					break
				V0[i,c] = data[k,c]
				k += steps
		return V0
	
	def print_res(self):
		#self.__V0 = self.vector_of_begining_centres(self.__data, self.__clusters)
		#self.distance(self.__V0, self.__data)
		#print(self.__V0.shape)
		self.iterations()
		dx,dy,di = self.__image.shape
		#img = cv2.equalizeHist((self.__U.max(0)).reshape(dx,dy))
		print(self.__U)
		print(self.__U.shape)
		#cv2.imshow("img",self.__U.max(0).reshape(dx,dy))
		print("hey")
		
	def distance(self, center, data):
		Dist = np.zeros((center.shape[0],data.shape[0]))
		
		if center.shape[1] > 2:
			for i in range(center.shape[0]):
				smth = (data-np.ones((data.shape[0],1))).dot(center[i,:])
				Dist[i,:] = ((np.sqrt(sum(smth)))**2)
		else:
			for i in range(center.shape[0]):
				Dist[i,:] = (fabs(center[i] - data)).T
		
		print(f"Dist = {Dist.shape}")
		return Dist
		
		
	def iterations(self):
		centres_previous = self.vector_of_begining_centres(self.__data, self.__clusters)
		
		for i in range(0,self.__max_iter):
			Dist = self.distance(centres_previous, self.__data)
			tmp = Dist ** (-2/(self.__m - 1))
			U = tmp/(np.ones((self.__clusters,1)).dot(sum(tmp))) ##!!!!!!---------multiply
			#print(f"U.shape = {U.shape}")
			mf = U ** self.__m
			center = mf.dot(self.__data)/(np.ones((self.__data.shape[1],1))*(sum(mf.transpose()))).T ##!!!!!!---------multiply
			
			delta = sum(np.sqrt(((center - centres_previous)**2).sum(axis=1)))/self.__clusters
			if i > 1 and  delta > self.__error:
				break
			
			print(f"i = {i}, delta = {delta}")
			
			centres_previous = center
		
		self.__U = U
		self.__center = center	
		
	
		
f = FCM("D:\ht_im1.tif",10)
f.print_res()