import random

class RecommendList(object):
	"""RecommendList"""
	def __init__(self, _CityMap, _passenger_list, _taxi, _mode = None):
		self.city_map 		= _CityMap
		self.passenger_list 	= _passenger_list
		self.taxi			= _taxi
		self.mode		= _mode
		
	def choose(self):
		"""
		Choose a direction
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
			self.passenger_list
			return
		elif mode == ME:
			return
