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

Roma = CityMap()
plist = PassengerList()
tlist = TaxiList()
point_num = len(Roma.coordinate)

plist.generate(10,Roma)
tlist.generate(10,Roma)
Roma_people = PassengerTaxi(Roma,plist,tlist)
inner_time = 0
WALL_TIME = 10
while inner_time<WALL_TIME:
	taxi_add_num = Roma_people.pool_count()
	for i in range(taxi_add_num):
		rd_id		= np.random.randint(point_num,size = length)
		rd_id_tuple_list 	= [(rd_id[i],citymap.random_choose(rd_id[i])) for i in range(length)] 
		rd_location	= np.random.random(length)#model undecided
		tmp = Taxi(rd_id_tuple_list[i] , rd_location[i])
		Roma_people.taxi_list.append(tmp)
	pass
	ai = Consultant()
	papers = Information(Roma_people.map,Roma_people.passenger_list,Roma_people.taxi_list)
	ai.guide(papers)
	Roma_people.next_timestep(ai.data_base)
	inner_time += Constants['dt']
