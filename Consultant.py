from Position import Position
from Passenger import Passenger
from Constants import Constants
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
                if (i.position.arc == taxi.position.arc) and \
                   (abs(i.position.location - taxi.position.location) < 0.5):
                    return [i]
            return []#can not find any potential passenger nearby;go on
        if self.mode == Constants['ME']:
            return []

    def guide(self, info):
        for iTaxi in info.taxi_list.Tlist:
            res = self.icandidate(iTaxi, info)
            self.data_base.append(res)
