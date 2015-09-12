import numpy as np
import random
from Passenger import Passenger
from CityMap import CityMap
from Constants import Constants

class TaxiPool(object):
	"""
	definition of  class TaxiPool
	"""
	def __init__(self):
		self.pool_list = []

	def push(self,taxi,passenger):
		MIN_TIME=10
		run_time = random.uniform(MIN_TIME,passenger.distance/taxi.velocity)
		back_time = CityMap.min_distance(taxi.position,passenger.position)/velocity + run_time
		self.pool_list.append((taxi,back_time))

	def run(self):
		count = 0
		for i in self.pool_list:
			i[1]-=Constants['dt']
			if i[1]==0:
				del i
				count+=1
		return count

