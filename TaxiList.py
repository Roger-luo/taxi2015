from Taxi import Taxi
from Position import Position
import numpy as np
from Constants import Constants

class TaxiList(object):
    """docstring for TaxiList"""
    def __init__(self):
        self.Tlist = []

    def generate(self,taxi_num,citymap):
<<<<<<< HEAD
        rd_id = np.random.randint(point_num, size=length)
        rd_id_tuple_list = [(rd_id[i], citymap.random_choose(rd_id[i])) for i in range(length)]
        rd_location = np.random.random(length)#model undecided
        self.Tlist = [Taxi(rd_id_tuple_list[i], rd_location[i]) for i in range(taxi_num)]

=======
        rd_id = np.random.randint(len(citymap.coordinate), size=taxi_num)
        rd_id_tuple_list = [(rd_id[i], citymap.random_choose(rd_id[i])) for i in range(taxi_num)]
        rd_location = np.random.random(taxi_num)#model undecided
        
        self.Tlist = [Taxi(Position(rd_id_tuple_list[i], rd_location[i]),Constants["velocity"]) for i in range(taxi_num)]
        
>>>>>>> d0b6278c127cb198c569dcc696f23952ad0510aa
