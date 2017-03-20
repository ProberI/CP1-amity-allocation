
class Amity():
    def __init__(self, Rname="Narnia", Rtype=True, Role="STAFF",
                 Pname="PAUL", PId=001):
        self.Rname = Rname
        self.Rtype = Rtype
        self.Role = Role
        self.Pname = Pname
        self.PId = PId

    def create_room(self, name, Rtype):
        self.Rname = name
        self.Rtype = Rtype
        each = self.Rname.split()
        for rname in each:
            if Rtype == "Office" or Rtype == "O":
                space = dict([(True, rname)])
                # return(space)
            elif Rtype == "Living_Space" or Rtype == "L":
                space = dict([(False, rname)])
                # return(space)
            else:
                return "Wrong input"
        return(space)

    def add_person(self, PName, Role, Accomodation):
        self.Pname = PName
        self.Role = Role
        NStore = []
        names = PName.split()
        for each in names:
            if type(each) == String:
                NStore.append(each)
            else:
                return ValuerError("Name can only be String value")
        return(NStore)


class Rooms(Amity):
    amity = Amity()
    if amity.Rtype == "Office" or amity.Rtype == "O":
        pass


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


class Office(Rooms):
    pass


"""
amity = Amity()
amity.create_room("Mombasa", "Office")
"""
