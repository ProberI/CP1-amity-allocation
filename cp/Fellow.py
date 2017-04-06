import sys

sys.path.insert(0, '/Users/Upendo/Documents/CP1/CP1-amity-allocation')
from cp.Person import Person


class Fellow(Person):
    def __init__(self, Fellow_names="Paul"):
        self.Fellow_names = Fellow_names

    def get_attr(self):
        return self.Fellow_names
