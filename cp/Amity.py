class Amity():
    def __init__(self, Rname="Narnia", Rtype="Office", Role="STAFF",
                 PersonName="PAUL", PId=1):
        self.Rname = Rname
        self.Rtype = Rtype
        self.Role = Role
        self.PersonName = PersonName
        self.PId = PId
        self.space = []

    def create_room(self, name, Rtype):
        self.Rname = name
        self.Rtype = Rtype
        each = self.Rname.split()
        for rname in each:
            if Rtype == "Office" or Rtype == "O":
                self.space.append(dict([("Office", rname)]))
                # return(space)
            elif Rtype == "Living_Space" or Rtype == "L":
                self.space.append(dict([("Living_Space", rname)]))
                # return(space)
            else:
                return "Wrong input"
        return(self.space)

    def add_person(self, PersonName, Role, Accomodation):
        self.PersonName = PersonName
        self.Role = Role
        NameStore = []
        if isinstance(PersonName, str) and Role in ("STAFF", "FELLOW") and Accomodation in ("Y", "N"):
            PersonName.split()
            NameStore.append(PersonName)
            return NameStore
        else:
            if not isinstance(PersonName, str):
                raise TypeError("Name can only be String")
            elif Role not in ("STAFF", "FELLOW"):
                raise ValueError("Role can only be Staff or fellow")
            elif Accomodation not in ("Y", "N"):
                raise ValueError("only Y or N accepted ")


#print(Amity().add_person("Hey", "Staff", "Y"))
