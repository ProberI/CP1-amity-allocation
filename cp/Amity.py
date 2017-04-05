import sys
sys.path.insert(0, '/Users/Upendo/Documents/CP1/CP1-amity-allocation')
from cp.Rooms import Rooms


class Amity():

    def __init__(self):
        self.all_people = []
        self.all_rooms = []
        self.allocations = []
        self.unallocated_people = []
        self.rooms = []
        self.offices = []
        self.living_spaces = []

    def create_room(self, name, Rtype):
        self.name = name
        self.Rtype = Rtype
        each = self.name.split()
        self.cleaned = []

        for rname in each:
            self.rooms.append(rname)

            if self.rooms.count(rname) > 1:
                return ("Room %s already exists!" % rname)
            elif Rtype.upper() == "OFFICE" or Rtype.upper() == "O":
                Rtype = "OFFICE"
                self.offices.append(rname)
                self.all_rooms.append(dict([(Rtype, rname)]))
            elif Rtype.upper() == "LIVING_SPACE" or Rtype.upper() == "L":
                Rtype = "LIVING_SPACE"
                self.living_spaces.append(rname)
                self.all_rooms.append(dict([(Rtype, rname)]))
            else:
                return "Room_Type can only be OFFICE or LIVING_SPACE"

        return (Rtype + " successfully created!")

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
        # return "Office and Living_space successfuly allocated"
        pass

    def rellocate_person(self, PersonID, Room_name):
        pass

    def load_people(self, file_name):
        pass

    def print_allocations(self):
        pass

    def print_unallocated(self):
        pass

    def print_room(self, room_name):
        # print(room_name)
        pass

    def save_state(self, db_name):
        pass

    def load_state(self):
        pass


#print(Amity().create_room("Mombasa Hogwarts Kenya", "o"))
