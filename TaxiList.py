from Taxi import Taxi
from Position import Position
import numpy as np
from Constants import Constants

class TaxiList(object):
    """docstring for TaxiList"""
    def __init__(self):
        self.Tlist = []

    def generate(self,taxi_num,citymap):
    	for i in range(taxi_num):
        		rd_id = np.random.randint(len(citymap.coordinate))
        		rd_id_tuple = (rd_id, citymap.random_choose(rd_id))
        		rd_location = np.random.random()#model undecided
        		if citymap.direction(rd_id_tuple):
        			velocity = Constants["velocity"]
        		else:
        			rd_id_tuple = (rd_id_tuple[1],rd_id_tuple[0])
        			velocity = -Constants["velocity"]
        		self.Tlist.append(Taxi(Position(rd_id_tuple,rd_location),velocity))

