import pickle
from vehicle import Vehicle
from vehicle_exception import VehicleException


FILEPATH="/home/vehicle_exception_data.dat"


class VechicleExceptionTests:
    
    @staticmethod
    def _load_vehicle_exception_from_file(path):
        """Loads the object whose data is in the file with the path specified."""
        result = None
        with open(path, "rb") as f:
            result = pickle.load(f)
        return result
    
    
    @staticmethod
    def _save_vehicle_exception_to_file(ve, path):
        """Saves the object referened by ve to the file with the path specified."""
        with open(path, "wb") as f:
            pickle.dump(ve, f)
        pass
    
    
    @staticmethod
    def test_vehicle_exception():
        """Unit test for vehicle exception object."""
        v = Vehicle(120, 4, "green")
        ve = VehicleException("top_speed must be in mph and must be a positive, whole number")
        print(ve)
        print(pickle.dumps(ve))
        new_ve = pickle.loads(pickle.dumps(ve))
        print(new_ve)
        _save_vehicle_exception_to_file(ve, FILEPATH)
        new_ve_2 = _load_vehicle_exception_from_file(FILEPATH)
        print(new_ve_2)
        pass
