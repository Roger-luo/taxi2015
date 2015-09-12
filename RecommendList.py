import random

class RecommendList(object):
	"""
	class RecommendList is a class to store strategies
	and contains functions to guid a taxi
	"""
	def __init__(self, _CityMap, _passenger_list, _taxi, _mode = None):
		self.city_map 		= _CityMap
		self.passenger_list 	= _passenger_list
		self.taxi			= _taxi
		self.mode		= _mode
		
	def choose(self):
		"""
		Choose can use defferent methods to guide a taxi
		to high population density blocks

		Parameters
		---------------
		self

		Returns
		----------
		if mode == None return  a random walk direction
		"""
		if mode == None:
			ID_list = _CityMap.neighbor_nodes(taxi.position.arc[1])
			dice = random.randint(0,len(ID_list)-1)
			return ID_list[dice]

	def decisionTree(self):
		"""
		decision tree use different methods to contact 
		a passenger & a taxi

		Parameters
		---------------
		passenger_list:	List[Passenger,[Passenger..]]
		Graph:		networkx.DiGraph

		Returns
		----------
		mode==None
		List[passenger]
		"""
		if mode == None:
			for i in self.passenger_list:
				if (i.position.arc==self.taxi.position.arc)and(abs(i.position.location - self.taxi.position.location)<0.5):
					return [i.ID]
				else:
					return []
		elif mode == ME:
			return []
