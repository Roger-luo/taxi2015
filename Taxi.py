from RecommendList import RecommendList
from TaxiPool import TaxiPool
from Constants import Constants

class Taxi(object):
	"""Generate a taxi"""
	def __init__(self, position_,velocity_):
		self.position 	= position_
		self.velocity 	= velocity_
		self.carry	= 0

	def next_timestep(self,rcmd_list,pool,dt=Constants['dt']):
		"""
		time evolution of a single taxi
		
		Parameter
		--------------
		rcmd_list: 	RecommendList
		pool:		TaxiPool
		dt 		unit time

		Returns
		----------
		None
		"""
		DCT_res = rcmd_list.decisionTree()
		if len(DCT_res)!=0:
			if rcmd_list.mode==None:
				 pool.push(self,DCT_res[0])
		delta_x =self.position.location + dt*self.velocity
		pool.run()
		if  delta_x >= 1:
			index = int(delta_x)
			while index:
				self.position.arc		= (self.position.arc[1],rcmd_list.choose())
				index-=1
			self.position.location	= delta_x-int(delta_x)
		elif delta_x<1:
			self.position.location 	= delta_x
			


