from app.cp.rooms import Rooms


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
