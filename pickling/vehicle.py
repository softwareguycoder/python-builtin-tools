from vehicle_exception import VehicleException


class Vehicle(object):
    
    def __init__(self, top_speed, num_wheels, color):
        """Creates a new vehicle with the specified top_speed, num_wheels, and color."""
        if (top_speed <= 0):
            raise VehicleException("top_speed must be a positive number of mph.")
        self.top_speed = top_speed
        self.num_wheels = num_wheels
        self.color = color
        self.miles_traveled = 0
        
    
    def __str__(self):
        return "The vehicle has a top speed of {0} mph.  It is a {1} vehicle with {2} wheels. It's traveled {3} miles so far." \
            .format(self.top_speed, self.color, self.num_wheels, self.miles_traveled)
            
    
    def drive(self, hours):
        # assume hours is an int, and top speed is in mph
        # hours must be positive
        if (hours <= 0):
            raise VehicleException("Hours must be a positive number.")
            
        self.miles_traveled += hours * self.top_speed
        print("Vehicle has been driven for {0} hours at {1} mph.".format(hours, self.top_speed))
        
        return self.miles_traveled
        
    
    def honk(self):
        print("Honk!!!")
        pass
