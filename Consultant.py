from Position import Position
from Passenger import Passenger
from Constants import Constants
import numpy as np
class Consultant(object):
    def __init__(self, mode_=None):
        self.data_base = []
        self.mode = mode_

    def icandidate(self, taxi, info):
        """
	icandidate provide the taxi a list of passenger candidates
	and a score to evaluate that the taxi should go on or find
	a passenger

	if the taxi should go on return an empty list
	else return the passenger candidates list
	"""
        if self.mode == None:
            for i in info.passenger_list.Plist:#try to find a passenger nearby
                if (i.position.arc[0] == taxi.position.arc[0]) and \
                   (abs(i.position.location - taxi.position.location) < 0.5)\
                   and(i.position.arc[1] == taxi.position.arc[1]):
                    return [i]
            return []#can not find any potential passenger nearby;go on
        if self.mode == Constants['ME']:
            score = []
            for i in info.passenger_list.Plist:
                s_wait = i.wait_time*i.wait_time
                s_travel = 10*np.exp(-(i.distance-0.5)*(i.distance-0.5))
                s_fee = 10*i.tips
                mdis = info.city_map.min_distance(i.position,taxi.position)
                s_distance = 10*abs(np.exp(-mdis*mdis))
                s_sum = s_wait+s_travel+s_fee+s_distance
                score.append((i,s_sum))
            score.sort(key = lambda x:-x[1])
            return [i[0] for i in score][0:10]

    def guide(self, info):
        for iTaxi in info.taxi_list.Tlist:
            res = self.icandidate(iTaxi, info)
            self.data_base.append(res)
