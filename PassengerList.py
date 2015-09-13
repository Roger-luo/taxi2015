import numpy as np
from Position import Position
from Passenger import Passenger
from Constants import Constants

class PassengerList(object):
    def __init__(self):
        self.Plist = []

    def generate(self, passenger_num, citymap):
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
	for i in range(passenger_num):
		rd_id = np.random.randint(len(citymap.coordinate))
		rd_id_tuple = (rd_id,citymap.random_choose(rd_id))
		rd_location = np.random.random()
		rd_distance = np.random.randn()
		rd_tips_list = np.random.randn()
		rd_pos = Position(rd_id_tuple,rd_location)
		self.Plist.append(Passenger(rd_pos,rd_distance,rd_tips_list))