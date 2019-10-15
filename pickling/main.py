from foo_class_tests import FooClassTests
from glob_tests import GlobTests
from vehicle_exception_tests import *


def main():
    FooClassTests.test_foo_class()
    GlobTests.test_glob()
    test_vehicle_exception()


if __name__=="__main__":
    main()
