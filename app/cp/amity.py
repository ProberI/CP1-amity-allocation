import random

from app.cp.living import Living
from app.cp.office import Office
from app.cp.fellow import Fellow
from app.cp.staff import Staff


class Amity():

    def __init__(self):
        self.all_people = []
        self.all_rooms = []
        self.allocations = []
        self.unallocated_people = []
        self.rooms = []
        self.offices = []
        self.living_spaces = []
        self.fellow_info = {}
        self.staff_info = {}

    def create_room(self, room_type, *name):
        self.name = name
        self.room_type = room_type

        for room_name in name:
            self.rooms.append(room_name)

            if self.rooms.count(room_name) > 1:
                return ("Room %s already exists!" % room_name)
            elif self.room_type.upper() == "OFFICE" or self.room_type.upper()\
                    == "O":
                self.room_type = "OFFICE"
                new_office = self.offices.append(Office(room_name).get_name())
                self.all_rooms.append(dict([(self.room_type, new_office)]))
            elif self.room_type.upper() == "LIVING_SPACE" or \
                    self.room_type.upper() == "L":
                self.room_type = "LIVING_SPACE"
                new_living_space = self.living_spaces.append(Living(room_name).get_name())
                self.all_rooms.append(dict([(self.room_type, new_living_space)]))
            else:
                return "Room_Type can only be OFFICE or LIVING_SPACE"

        return (self.room_type + " successfully created!")

    def add_person(self, First_name, Last_Name, Role, Accomodation="N"):
        self.First_name = First_name
        self.Last_Name = Last_Name
        self.Role = Role
        self.Accomodation = Accomodation
        try:
            self.person_name = (Fellow(self.First_name, self.Last_Name).get_name())
            self.all_people.append(self.person_name)
            Person_id = self.genarate_user_ID()
            if any(char.isdigit() for char in self.person_name):
                return "Ooops! Name cannot contain a digit!"
            elif self.all_people.count(self.person_name) > 1:
                return ("Ooops! %s already exists in the system." % self.person_name)
            elif self.Role not in ("STAFF", "FELLOW"):
                return "Role can only be STAFF or FELLOW"
            elif self.Accomodation not in ("Y", "N"):
                return "Accomodation options are only 'Y' or 'N'"
            elif self.Role == "STAFF" and self.Accomodation == "Y":
                return "Staff cannot have accomodation!"
            else:
                if self.Role.upper() == "FELLOW":
                    self.fellow_info = {Person_id: self.person_name}
                elif self.Role.upper() == "STAFF":
                    self.staff_info = {Person_id: self.person_name}
            return "Person has been successfully added"

        except TypeError:
            return "Name cannot be a number!"

    def genarate_user_ID(self):
        prefix = "UID"
        suffix = self.all_people.index(self.person_name)
        while suffix <= len(self.all_people):
            Person_id = self.person_name + prefix + str(suffix)
            return Person_id

    def allocate_room_randomly(self, list_arg=None):
        """
        - Have people to be allocated in a list
        - Randomly chooose a person from the list in a load_people
        - If person chosen is already in the list pass and give message
        - Append the person to list until list is full
        - When list is full stop allocation and give room full msg
        - Proceed to next face

        """
        # if self.Role.upper() == "FELLOW":
        #     for fellow in self.fellow_info:
        #         list_arg = self.fellow_info.values()
        #         print(list_arg)
        #         selected_fellow = random.choice(list_arg)
        #         if selected_fellow in self.allocations:
        #             return "This fellow has already been allocated a room"
        #         else:
        #             for room in self.all_rooms:
        #
        #                 if room.keys() == ['OFFICE']:
        #
        #                     for room_nam in self.offices:
        # 'append data to dict first then test for size'
        #                         if len(room_nam) < 6:++++
        #                             room_nam = {room.values(): selected_fellow}
        #                             print(room_nam)
        #                         else:
        #                             return "Room is already full"
        #                 elif room.keys() == "LIVING_SPACE":
        #                     if len(room) < 4:
        #                         room.append(selected_fellow)
        #                     else:
        #                         return "Living_space is already occupied"
        #         if self.Role.upper() == "STAFF":
        #             pass

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


amity = Amity()
amity.create_room("Hogwarts", "o")
amity.add_person("PAUL", "UPENDO", "FELLOW", "Y")
print (amity.allocate_room_randomly())
