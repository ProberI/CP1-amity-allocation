class Amity():

    def __init__(self):
        self.all_people = []
        self.all_rooms = []
        self.allocations = []
        self.unallocated_people = []
        self.rooms = []
        self.offices = []
        self.living_spaces = []
        self.fellow = "John"
        self.fellows = []

    def create_room(self, name, room_type):
        self.name = name
        self.room_type = room_type
        each = self.name.split()

        for room_name in each:
            self.rooms.append(room_name)

            if self.rooms.count(room_name) > 1:
                return ("Room %s already exists!" % room_name)
            elif self.room_type.upper() == "OFFICE" or self.room_type.upper()\
                    == "O":
                self.room_type = "OFFICE"
                self.offices.append(room_name)
                self.all_rooms.append(dict([(self.room_type, room_name)]))
            elif self.room_type.upper() == "LIVING_SPACE" or \
                    self.room_type.upper() == "L":
                self.room_type = "LIVING_SPACE"
                self.living_spaces.append(room_name)
                self.all_rooms.append(dict([(self.room_type, room_name)]))
            else:
                return "Room_Type can only be OFFICE or LIVING_SPACE"

        return (self.room_type + " successfully created!")

    def add_person(self, First_name, Last_Name, Role, Accomodation="N"):

        try:
            Person_name = First_name + " " + Last_Name
            self.fellow = Person_name
            self.all_people.append(Person_name)
            Person_id = self.genarate_user_ID()
            if any(char.isdigit() for char in Person_name):
                return "Ooops! Name cannot contain a digit!"
            elif self.all_people.count(Person_name) > 1:
                return ("Ooops! %s already exists in the system." % Person_name)
            elif Role not in ("STAFF", "FELLOW"):
                return "Role can only be STAFF or FELLOW"
            elif Accomodation not in ("Y", "N"):
                return "Accomodation options are only 'Y' or 'N'"
            elif Role == "STAFF" and Accomodation == "Y":
                return "Staff cannot have accomodation!"
            else:
                self.fellows.append(dict([(Person_id, Person_name)]))
                return self.fellows

        except TypeError:
            return "Name cannot be a number!"

    def genarate_user_ID(self, First_name="John"):
        First_name = self.fellow
        prefix = "UID"
        suffix = self.all_people.index(First_name)
        while suffix <= len(self.all_people):
            Person_id = First_name + prefix + str(suffix)
            return Person_id

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
