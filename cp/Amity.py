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
                Rtype = "Office"
                self.space.append(dict([("Office", rname)]))
                # return(space)
            elif Rtype == "Living_Space" or Rtype == "L":
                Rtype = "Living_Space"
                self.space.append(dict([("Living_Space", rname)]))
                # return(space)
            else:
                return "Room_Type can only be Office or Living_Space"
        return(str(Rtype) + " successfully created!")

    def add_person(self, PersonName, Role, Accomodation="N"):
        self.PersonName = PersonName
        self.Role = Role
        NameStore = []
        if isinstance(PersonName, str) and Role in ("STAFF",
                                                    "FELLOW") and Accomodation in ("Y", "N"):
            PersonName.split()
            if Role == "STAFF" and Accomodation == "Y":
                return "Staff cannot have accomodation!"
            elif Role == "FELLOW" and Accomodation == "Y":
                return "Living_Space successfully allocated"
            elif Role == "FELLOW" and Accomodation == "N":
                return "Living_Space not allocated."
            else:
                NameStore.append(PersonName)
            return NameStore
        else:
            if not isinstance(PersonName, str):
                return ("Name can only be String")
            elif Role not in ("STAFF", "FELLOW"):
                return("Role can only be STAFF or FELLOW")
            elif Accomodation not in ("Y", "N"):
                return("Accomodation options are only Y or N")

    def allocate_room(self, Person_name, Role, Accomodation_status):
        pass

    def rellocate_person(self, PersonID, Room_name):
        pass

    def load_people(self):
        pass

    def print_allocations(self):
        pass

    def print_unallocated(self):
        pass

    def print_room(self):
        pass


# print(Amity().add_person("Hey", "FELLOW", "Y"))
