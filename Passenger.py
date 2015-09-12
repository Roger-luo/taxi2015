class Passenger(object):
    def __init__(self, position_, distance_, tips_, wait_time_=0):
        self.position = position_
        self.distance = distance_
        self.tips = tips_
        self.wait_time = wait_time_
