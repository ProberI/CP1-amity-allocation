class Amity():
    def __init__(self, Rname="Narnia", Rtype=True, Role="STAFF",
                 Pname="PAUL", PId=1):
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


"""
amity = Amity()
amity.create_room("Mombasa", "Office")
"""
