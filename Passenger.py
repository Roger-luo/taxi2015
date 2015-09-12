import numpy as np
from Position 	import Position
from CityMap	import CityMap

class Passenger(object):
	def __init__(self, position_, distance_, tips_, wait_time_ = 0):
		self.position = position_ 
		self.distance = distance_ ##distance_ is a tuple include parameters for distance setting
		self.tips = tips_ ##tips_ is the same as distance_
		self.wait_time_ = wait_time_ 
	def wait_time_refresh(self, dt_):
			self.wait_time_ += dt_

class PassengerList(object)
	def __init__(self):
		self.list = []

	def gen(self,len,citymap):
	"""
	Parameter
	--------------
	rd_id:		list[float...]
		random ID List
	rd_id_tuple_list:	list[tuple...]
		random tuple List
	rd_distance:	list[float...]
		random distance List
	rd_tips_list:	list[float...]
		random tips List
	rd_location:	list[float...]
		random location List
	rd_pos:		list[Position...]
		random position List

	Returns
	----------
	gen:None
		generate a PassengerList with length(Passenger number) len
	"""
		rd_id		= np.random.randint(point_num,size = len)
		rd_id_tuple_list 	= [(rd_id[i],citymap.random_choose(rd_id[i])) for i in range(len)] 
		rd_distance	= np.random.randn(len)#model undecided
		rd_tips_list 	= np.random.randn(len)#model undecided
		rd_location	= np.random.random(len)#model undecided
		rd_pos  	= [Position(rd_id_tuple_list[i],rd_location[i]) for i in range(len)]
		self.list 	= [Passenger(rd_pos[i],rd_distance[i],rd_tips_list[i]) for i in range(len)]

	def run(self):
		
		