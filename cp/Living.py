import sys
sys.path.insert(0, '/Users/Upendo/Documents/CP1/CP1-amity-allocation')
from cp.Rooms import Rooms


class Living(Rooms):

    """ People"""

    def numTest(self, fellows):
        self.Rname = fellows
        each = self.Rname.split()
        store = []
        for name in each:
            if (len(store)) < 4:
                store.append(name)
            else:
                return "You have exceeded maximum"
        return(store)
