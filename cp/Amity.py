class Amity():

    def __init__(self):
        self.all_people = []
        self.all_rooms = []
        self.allocations = []
        self.unallocated_people = []

    def create_room(self, name, Rtype):
        self.name = name
        self.Rtype = Rtype
        each = self.name.split()
        for rname in each:
            if Rtype == "Office" or Rtype == "O":
                Rtype = "Office"
                self.all_rooms.append(dict([("Office", rname)]))
                # return(space)
            elif Rtype == "Living_Space" or Rtype == "L":
                Rtype = "Living_Space"
                self.all_rooms.append(dict([("Living_Space", rname)]))
                # return(space)
            else:
                return "Room_Type can only be Office or Living_Space"
        return(str(Rtype) + " successfully created!")

    def add_person(self, PersonName, Role, Accomodation="N"):
        self.PersonName = PersonName
        self.Role = Role
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
                self.all_people.append(PersonName)
            return self.all_people
        else:
            if not isinstance(PersonName, str):
                return ("Name can only be String")
            elif Role not in ("STAFF", "FELLOW"):
                return("Role can only be STAFF or FELLOW")
            elif Accomodation not in ("Y", "N"):
                return("Accomodation options are only Y or N")

    def allocate_room(self):
        return "Office and Living_space successfuly allocated"

    def rellocate_person(self, PersonID, Room_name):
        pass

    def load_people(self, file_name):
        pass

    def print_allocations(self):
        pass

    def print_unallocated(self):
        pass

    def print_room(self):
        pass


# print(Amity().add_person("Hey", "FELLOW", "Y"))
