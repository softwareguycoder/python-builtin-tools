import pickle


class TheUnpickler(object):
    
    @staticmethod
    def unpickle(pickled_data):
        if not pickled_data:
            return
        
        # Assume the pickled data is a string
        return pickle.loads(pickled_data)