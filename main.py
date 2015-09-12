import numpy
import random
from CityMap	import CityMap
from Constants import Constants
from Passenger import Passenger
from PassengerList import PassengerList
from Taxi	import Taxi
from TaxiList import TaxiList
from Position	import Position
from Consultant import Consultant
from PassengerTaxi import PassengerTaxi
from Information import Information

ROMA = CityMap()
PLIST = PassengerList()
TLIST = TaxiList()
POINT_NUM = len(ROMA.coordinate)


PLIST.generate(10, ROMA)
TLIST.generate(10, ROMA)
ROMA_PEOPLE = PassengerTaxi(ROMA, PLIST, TLIST)
INNER_TIME = 0
WALL_TIME = 10
while INNER_TIME < WALL_TIME:
    TAXI_ADD_NUM = ROMA_PEOPLE.pool_count()
    for i in range(TAXI_ADD_NUM):
        rd_id = random.randint(POINT_NUM)
        rd_id_tuple = (rd_id, ROMA_PEOPLE.city_map.random_choose(rd_id))
        rd_location = random.random()#model undecided
        tmp_position = Position(rd_id_tuple, rd_location)
        tmp_velocity = Constants["velocity"]
        ROMA_PEOPLE.taxi_list.append(Taxi(tmp_position, tmp_velocity))
    AI = Consultant()
    PAPERS = Information(ROMA_PEOPLE.map, ROMA_PEOPLE.passenger_list, ROMA_PEOPLE.taxi_list)
    AI.guide(PAPERS)
    ROMA_PEOPLE.next_timestep(AI.data_base)
    INNER_TIME += Constants['dt']
