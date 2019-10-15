import pickle
from foo_class import FooClass


class FooClassTests:
    
    @staticmethod
    def test_foo_class():
        foo = FooClass()
        foo.a = 1
        print(foo)
        print(pickle.dumps(foo))
        new_foo = pickle.loads(pickle.dumps(foo))
        print(new_foo)
        print(new_foo.a)
        pass
