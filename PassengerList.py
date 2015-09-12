import numpy as np

class PassengerList(object):
    def __init__(self):
        self.Plist = []

    def generate(self, length, citymap):
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
        rd_id = np.random.randint(len(citymap.coordinate), size=length)
        rd_id_tuple_list = [(rd_id[i], citymap.random_choose(rd_id[i])) for i in range(length)]
        rd_location = np.random.random(length)#model undecided
        rd_distance = np.random.randn(length)#model undecided
        rd_tips_list = np.random.randn(length)#model undecided
        rd_pos = [Position(rd_id_tuple_list[i], rd_location[i]) for i in range(length)]
        self.Plist = [Passenger(rd_pos[i], rd_distance[i], rd_tips_list[i]) for i in range(length)]
