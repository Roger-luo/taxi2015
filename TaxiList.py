from Taxi import Taxi
import numpy as np

class TaxiList(object):
    """docstring for TaxiList"""
    def __init__(self):
        self.Tlist = []

    def generate(self,taxi_num,citymap):
        rd_id = np.random.randint(point_num, size=length)
        rd_id_tuple_list = [(rd_id[i], citymap.random_choose(rd_id[i])) for i in range(length)]
        rd_location = np.random.random(length)#model undecided
        self.Tlist = [Taxi(rd_id_tuple_list[i], rd_location[i]) for i in range(taxi_num)]
        
