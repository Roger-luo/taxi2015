from Information import Information
from Constants import Constants
import random

class PassengerTaxi(Information):
    def __init__(self, citymap, passenger_list_, taxi_list_):
        self.pool = []
        self.mode = None
        Information.__init__(self, citymap, passenger_list_, taxi_list_)

    def push(self, taxi, passenger):
        MIN_TIME = 10
        run_time = random.uniform(MIN_TIME, passenger. distance/taxi.velocity)
        back_time = self.city_map.min_distance\
                            (taxi.position, passenger.position)/taxi.velocity + run_time
        self.pool.append(back_time)

    def navigator(self, taxi):
        if self.mode == None:
            ID_list = self.city_map.neighbor_nodes(taxi.position.arc[1])
            dice = random.randint(0, len(ID_list)-1)
            return ID_list[dice]

    def next_timestep(self, candidates, dt=Constants['dt']):
        """
        candidates comes from the Consultant.data_base
        and condidate is a list
        """
        List_end = len(self.taxi_list.Tlist)
        iTaxi = 0
        while iTaxi < List_end:
            if len(candidates[iTaxi]) != 0:
                if self.mode == None:
                    self.push(self.taxi_list.Tlist[iTaxi], candidates[iTaxi][0])
                    cur_passenger = candidates[iTaxi][0]
                    candidates = [filter(lambda x:x!=cur_passenger,i) for i in candidates]
                    self.passenger_list.Plist = filter(lambda x:x!=cur_passenger,self.passenger_list.Plist)
                    del self.taxi_list.Tlist[iTaxi]
                    del candidates[iTaxi]
                    List_end=len(self.taxi_list.Tlist)
            else:
                # print "iTaxi:%s"%(iTaxi)
                # print "len:%s"%(len(self.taxi_list.Tlist))
                cur_taxi = self.taxi_list.Tlist[iTaxi]
                cur_arc = cur_taxi.position.arc#the arc in taxi (i,j)means a taxi run from i to j
                arc_len = self.city_map.arc_length(cur_taxi.position.arc)
                cur_location = cur_taxi.position.location
                cur_speed = cur_taxi.velocity#velocity has to be unsigned
                mileage = arc_len*cur_location+cur_speed*dt#mileage is an unsigned float
                if mileage<0:
                        print "help"
                        print cur_location
                        print cur_speed
                if mileage<=arc_len:
                    cur_taxi.position.location = mileage/arc_len
                elif mileage > arc_len:
                    cur_len = self.city_map.arc_length(cur_taxi.position.arc)
                    while mileage>cur_len:
                        mileage -= cur_len
                        cur_taxi.position.arc = (cur_taxi.position.arc[1],self.navigator(cur_taxi))
                        cur_len = self.city_map.arc_length(cur_taxi.position.arc)
                    arc_len=self.city_map.arc_length(cur_taxi.position.arc)
                    cur_taxi.position.location = mileage/arc_len
                iTaxi+=1
        return

    def pool_count(self):
        count = 0
        for i in range(len(self.pool)):
            self.pool[i] -= Constants['dt']
        count = len(filter(lambda x: x<=0, self.pool))
        self.pool=filter(lambda x: x>0, self.pool)
        return count
