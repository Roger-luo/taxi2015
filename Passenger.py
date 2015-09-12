import random

class Passenger(object):
	def __init__(self, position_, distance_, tips_, wait_time_ = 0):
		self.position = position_ 
		self.distance = distance_ ##distance_ is a tuple include parameters for distance setting
		self.tips = tips_ ##tips_ is the same as distance_
		self.wait_time_ = wait_time_ 
	def wait_time_refresh(self, dt_):
			self.wait_time_ += dt_
