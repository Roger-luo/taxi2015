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
ROMA.add_node(0, numpy.array([3, 7]))
ROMA.add_node(1, numpy.array([6, 7]))
ROMA.add_node(2, numpy.array([4, 6]))
ROMA.add_node(3, numpy.array([6, 5]))
ROMA.add_node(4, numpy.array([8, 5]))
ROMA.add_node(5, numpy.array([3, 4]))
ROMA.add_node(6, numpy.array([5, 4]))
ROMA.add_node(7, numpy.array([2, 3]))
ROMA.add_node(8, numpy.array([5, 2]))
ROMA.add_arc(0, 1)
ROMA.add_arc(0, 2)
ROMA.add_arc(0, 7)
ROMA.add_arc(1, 3)
ROMA.add_arc(1, 4)
ROMA.add_arc(2, 3)
ROMA.add_arc(2, 5)
ROMA.add_arc(3, 4)
ROMA.add_arc(3, 6)
ROMA.add_arc(4, 8)
ROMA.add_arc(5, 6)
ROMA.add_arc(5, 7)
ROMA.add_arc(5, 8)
ROMA.add_arc(6, 8)
ROMA.add_arc(7, 8)

PLIST = PassengerList()
TLIST = TaxiList()
POINT_NUM = len(ROMA.coordinate)


PLIST.generate(10, ROMA)
TLIST.generate(10, ROMA)
ROMA_PEOPLE = PassengerTaxi(ROMA, PLIST, TLIST)
INNER_TIME = 0
WALL_TIME = 10
while INNER_TIME < WALL_TIME:
    print "pass1"
    import pdb; pdb.set_trace()  # breakpoint 093ed5f0 //
    TAXI_ADD_NUM = ROMA_PEOPLE.pool_count()
    print "pass6"
    print "TAXI_ADD_NUM:%s"%(TAXI_ADD_NUMbre)
    for i in range(TAXI_ADD_NUM):
        print "pass5"
        rd_id = numpy.random.randint(POINT_NUM)
        rd_id_tuple = (rd_id, ROMA_PEOPLE.city_map.random_choose(rd_id))
        rd_location = random.random()#model undecided
        tmp_position = Position(rd_id_tuple, rd_location)
        tmp_velocity = Constants["velocity"]
        ROMA_PEOPLE.taxi_list.Tlist.append(Taxi(tmp_position, tmp_velocity))
    print "pass4"
    AI = Consultant()
    PAPERS = Information(ROMA_PEOPLE.city_map, ROMA_PEOPLE.passenger_list, ROMA_PEOPLE.taxi_list)
    print "pass2"
    AI.guide(PAPERS)
    print "pass3"
    ROMA_PEOPLE.next_timestep(AI.data_base)
    INNER_TIME += Constants['dt']
    print "INNER_TIME:%s" %(INNER_TIME)
