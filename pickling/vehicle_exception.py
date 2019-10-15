class VehicleException(Exception):
    def __init__(self, msg):
        super(VehicleException, self).__init__(msg)
        self.msg = msg
        
    
    def __str__(self):
        return "Your error was: %s" % self.msg
        
        
    def __repr__(self):
        return "The repr of your error was: %s" % self.msg
