
import numpy as np
import random
from CityMap	import CityMap
from Constants import Constants
#basic storage class

class Position(object):
	def __init__(self, arc_, location_):
		self.arc = arc_
		self.location = location_

class Passenger(object):
	def __init__(self, position_, distance_, tips_, wait_time_ = 0):
		self.position = position_ 
		self.distance = distance_ 
		self.tips = tips_ 
		self.wait_time = wait_time_ 

class Taxi(object):
	def __init__(self, position_,velocity_):
		self.position 	= position_
		self.velocity 	= velocity_

#data
class PassengerList(object):
	def __init__(self):
		self.Plist = []

	def generate(self,len,citymap):
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
		rd_location	= np.random.random(len)#model undecided 
		rd_distance	= np.random.randn(len)#model undecided
		rd_tips_list 	= np.random.randn(len)#model undecided
		rd_pos  	= [Position(rd_id_tuple_list[i],rd_location[i]) for i in range(len)]
		self.Plist 	= [Passenger(rd_pos[i],rd_distance[i],rd_tips_list[i]) for i in range(len)]

class TaxiList(object):
	"""docstring for TaxiList"""
	def __init__(self):
		self.Tlist = []

	def generate(self,taxi_num,citymap):
		rd_id		= np.random.randint(point_num,size = len)
		rd_id_tuple_list 	= [(rd_id[i],citymap.random_choose(rd_id[i])) for i in range(len)] 
		rd_location	= np.random.random(len)#model undecided
		self.Tlist = [Taxi(rd_id_tuple_list[i] , rd_location[i]) for i in range(taxi_num)]

class Information(object):
	def __init__(self,citymap,passenger_list_,taxi_list_):
		self.map 		= citymap
		self.passenger_list	= passenger_list_
		self.taxi_list		= taxi_list_

class Consultant(object):
	def __init__(self, mode_=None):
		self.data_base = []
		self.mode = mode_

	def icandidate(self,taxi,info):
		"""
		icandidate provide the taxi a list of passenger candidates
		and a score to evaluate that the taxi should go on or find
		a passenger

		if the taxi should go on return an empty list
		else return the passenger candidates list
		"""
		if self.mode == None:
			for i in info.passenger_list.Plist:#try to find a passenger nearby
				if(i.position.arc==taxi.position.arc)and(abs(i.position.location - taxi.position.location)<0.5):
					return [i]
			return []#can not find any potential passenger nearby;go on

	def guide(self,info):
		for iTaxi in info.taxi_list.Tlist:
			res = icandidate(self,iTaxi,info)
			data_base.append(res)

class PassengerTaxi(Information):
	"""docstring for PassengerTaxi"""
	def __init__(self,citymap,passenger_list_,taxi_list_):
		self.pool = []
		self.mode = None
		Information.__init__(self,citymap,passenger_list_,taxi_list_)
	
	def push(self,taxi,passenger):
		MIN_TIME=10
		run_time = random.uniform(MIN_TIME,passenger.distance/taxi.velocity)
		back_time = CityMap.min_distance(taxi.position,passenger.position)/taxi.velocity + run_time
		self.pool.append(back_time)

	def navigator(self,taxi):
		if self.mode == None:
			ID_list = self.map.neighbor_nodes(taxi.position.arc[1])
			dic = random.randint(0,len(ID_list)-1)
			return ID_list[dice]

	def next_timestep(self,candidates,dt=Constants['dt']):
		"""
		candidates comes from the Consultant.data_base
		and candidates is a list
		"""
		for iTaxi in range(len(self.taxi_list.Tlist)):
			if len(candidates[iTaxi])!=0:
				if self.mode == None:
					self.push(self.taxi_list.Tlist[iTaxi],candidates[iTaxi][0])
					del self.taxi_list.Tlist[iTaxi]
					self.passenger_list.Plist.remove(candidates[iTaxi])
			arc_len 		= self.map.arc_length(self.taxi_list.Tlist[iTaxi].position.arc)
			taxi_location 	= self.taxi_list.Tlist[iTaxi].position.location
			speed 		= self.taxi_list.Tlist[iTaxi].velocity
			run_distance = arc_len*taxi_location+speed*dt
			pass
			if run_distance<=arc_len:
				self.taxi_list.Tlist[iTaxi].position.location = run_distance/arc_len
			else:
				while (run_distance - self.map.arc_length(self.taxi_list.Tlist[iTaxi].position.arc))>0:
					self.taxi_list.Tlist[iTaxi].position.arc 	= (self.taxi_list.Tlist[iTaxi].position.arc[1],self.navigator(self.taxi_list.Tlist[iTaxi]))
					run_distance = run_distance - self.map.arc_length(self.taxi_list.Tlist[iTaxi].position.arc)
				arc_len 	= self.map.arc_length(self.taxi_list.Tlist[iTaxi].position.arc)
				self.taxi_list.Tlist[iTaxi].position.location = run_distance/arc_len

	def pool_count(self):
		count = 0
		for i in range(len(self.pool)):
			self.pool[i] -=Constants['dt']
			if self.pool[i]==0:
				count += 1
				del self.pool[i]
		return count


Roma = CityMap()
plist = PassengerList()
tlist = TaxiList()

plist.generate(10,Roma)
tlist.generate(10,Roma)
Roma_people = PassengerTaxi(Roma,plist,tlist)
inner_time = 0
WALL_TIME = 10
while inner_time<WALL_TIME:
	taxi_add_num = Roma_people.pool_count()
	for i in range(taxi_add_num):
		rd_id		= np.random.randint(point_num,size = len)
		rd_id_tuple_list 	= [(rd_id[i],citymap.random_choose(rd_id[i])) for i in range(len)] 
		rd_location	= np.random.random(len)#model undecided
		tmp = Taxi(rd_id_tuple_list[i] , rd_location[i])
		Roma_people.taxi_list.append(tmp)
	pass
	ai = Consultant()
	papers = Information(Roma_people.map,Roma_people.passenger_list,Roma_people.taxi_list)
	ai.guide(papers)
	Roma_people.next_timestep(ai.data_base)
	inner_time += Constants['dt']