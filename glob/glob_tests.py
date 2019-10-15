import glob, os


DIRPATH="/home"
GLOB_PATTERN="/home/*.py"


class GlobTests:
    
    @staticmethod
    def _list_files_in(dirpath):
        files = os.listdir(dirpath)
        print()
        print("List of files in '{0}' produced by os.listdir:".format(dirpath))
        print()
        for file in files:
            print(file)
        pass


    @staticmethod
    def _list_files_by_globbing(glob_pattern):
        print()
        print("List of files produced by globbing on '{0}'".format(glob_pattern))
        print()
        files = []
        files = glob.glob(GLOB_PATTERN)
        for file in files:
            print(file)
        pass


    @staticmethod
    def _tell_user_we_are_done():
        print()
        print("Done listing.")
        print()
        pass


    @staticmethod
    def test_glob():
        _list_files_in(DIRPATH)
        _list_files_by_globbing(GLOB_PATTERN)
        _tell_user_we_are_done()
        pass
