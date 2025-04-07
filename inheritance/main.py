class vehicle:
    def __init__(self, name , max_speed , Milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = Milage

class bus(vehicle):
    pass

school_bus = bus("volvo" , 180 , 12)
print("bus name:", school_bus.name, ",max speed:", school_bus.max_speed , ",milage:" , school_bus.milage)
        


