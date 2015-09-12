from Information import Information
from Constants import Constants

class PassengerTaxi(Information):
    """docstring for PassengerTaxi"""
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
            dic = random.randint(0, len(ID_list)-1)
            return ID_list[dice]

    def next_timestep(self, candidates, dt=Constants['dt']):
        """
	candidates comes from the Consultant.data_base
	and candidates is a list
	"""
        for iTaxi in range(len(self.taxi_list.Tlist)):
            if len(candidates[iTaxi]) != 0:
                if self.mode == None:
                    self.push(self.taxi_list.Tlist[iTaxi], candidates[iTaxi][0])
                    del self.taxi_list.Tlist[iTaxi]
                    self.passenger_list.Plist.remove(candidates[iTaxi])
                arc_len = self.city_map.arc_length(self.taxi_list.Tlist[iTaxi].position.arc)
                taxi_location = self.taxi_list.Tlist[iTaxi].position.location
                speed = self.taxi_list.Tlist[iTaxi].velocity
                run_distance = arc_len*taxi_location+speed*dt
                if run_distance <= arc_len:
                    self.taxi_list.Tlist[iTaxi].position.location = run_distance/arc_len
                else:
                    while (run_distance - \
                           self.city_map.arc_length(self.taxi_list.Tlist[iTaxi].position.arc)) > 0:
                        self.taxi_list.Tlist[iTaxi].position.arc = \
                                (self.taxi_list.Tlist[iTaxi].position.arc[1], \
                                 self.navigator(self.taxi_list.Tlist[iTaxi]))
                        run_distance = run_distance - self.city_map.arc_length\
                                       (self.taxi_list.Tlist[iTaxi].position.arc)
                    arc_len = self.city_map.arc_length(self.taxi_list.Tlist[iTaxi].position.arc)
                    self.taxi_list.Tlist[iTaxi].position.location = run_distance/arc_len

    def pool_count(self):
        count = 0
        for i in range(len(self.pool)):
            self.pool[i] -= Constants['dt']
            if self.pool[i] <= 0:
                count += 1
                del self.pool[i]
        return count
