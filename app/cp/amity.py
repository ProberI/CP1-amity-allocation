import sys
import random

from app.cp.living import Living
from app.cp.office import Office
from app.cp.fellow import Fellow
from app.cp.staff import Staff


class Amity():

    def __init__(self):
        self.all_people = []
        self.allocations = []
        self.unallocated_people = []
        self.rooms = []
        self.offices = []
        self.living_spaces = []
        self.fellow_info = {}
        self.staff_info = {}
        self.all_rooms = []

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
                self.offices.append(Office(room_name))
                self.all_rooms.append(Office(room_name).get_room_name())
            elif self.room_type.upper() == "LIVING_SPACE" or \
                    self.room_type.upper() == "L":
                self.room_type = "LIVING_SPACE"
                self.living_spaces.append(Living(room_name))
                self.all_rooms.append(Living(room_name).get_room_name())
            else:
                return "Room_Type can only be OFFICE or LIVING_SPACE"
        return (self.room_type + " successfully created!")

    def add_person(self, First_name, Last_Name, Role, Accomodation="N"):
        self.First_name = First_name
        self.Last_Name = Last_Name
        self.Role = Role
        self.Accomodation = Accomodation
        try:
            self.person_name = (Fellow(self.First_name,
                                       self.Last_Name).get_name())
            self.all_people.append(self.person_name)
            self.Person_id = self.genarate_user_ID()
            if any(char.isdigit() for char in self.person_name):
                return "Ooops! Name cannot contain a digit!"
            elif self.all_people.count(self.person_name) > 1:
                return ("Ooops! %s already exists in the system."
                        % self.person_name)
            elif self.Role not in ("STAFF", "FELLOW"):
                return "Role can only be STAFF or FELLOW"
            elif self.Accomodation not in ("Y", "N"):
                return "Accomodation options are only 'Y' or 'N'"
            elif self.Role == "STAFF" and self.Accomodation == "Y":
                return "Staff cannot have accomodation!"
            else:
                self.fellow_info[self.Person_id] = self.person_name
                self.staff_info[self.Person_id] = self.person_name
                self.allocate_room_randomly()
                return "Person has been successfully added and allocated room"

        except TypeError:
            return "Name cannot be a number!"

    def genarate_user_ID(self):
        prefix = "UID"
        suffix = self.all_people.index(self.person_name)
        while suffix <= len(self.all_people):
            Person_id = self.person_name + prefix + str(suffix)
            return Person_id

    def allocate_room_randomly(self):
        if self.Role == "FELLOW":
            for fellow in self.fellow_info.values():
                fellow_id, selected_fellow = \
                    random.choice(list(self.fellow_info.items()))
                if selected_fellow in self.allocations:
                    return selected_fellow + " " +\
                        "fellow has already been allocated a room"
                elif self.Accomodation == "Y":
                    for room_office in self.offices:
                        room_office.add_occupants(selected_fellow)
                    for room_living in self.living_spaces:
                        room_living.add_occupants(selected_fellow)
                return "Ooops! allocation was Unsuccessful"

        elif self.Role == "STAFF":
            for staff in self.staff_info.values():
                staff_id, selected_staff = \
                    random.choice(list(self.staff_info.items()))
                if selected_staff in self.allocations:
                    return selected_staff + " " +\
                        "Staff has already been allocated a room"
                elif self.Accomodation == "Y":
                    return "Staff cannot have accomodation"
                elif self.Accomodation == "N":
                    for room_office in self.offices:
                        room_office.add_occupants(selected_staff)
                return "Ooops! allocation was Unsuccessful"

    def rellocate_person(self, Person_name, Room_name):
        self.Room_name = Room_name
        """
         -- check if personID or person exists
         -- *check if person was previously not allocated
         -- check if room exists
         -- work on edgecases
         -- Reallocate:
                - Go to occupants list where personId exists
                - pop that element
                - add it to the new room instance
        """
        if Person_name not in self.staff_info.values() or\
                Person_name not in self.fellow_info.values():
            return "Ooops, invalid employee_name please try again."
        elif self.Room_name not in self.all_rooms:
            return "Oops sorry, this particular room does not exist!"
        else:
            if Person_name in self.staff_info.values() or\
                    Person_name in self.fellow_info.values():
                for current_room in self.offices:
                    if Person_name in current_room.get_occupants():
                        current_room.occupants.remove(Person_name)
                        for self.Room_name in self.offices:
                            self.Room_name.add_occupants(Person_name)

                return "Success"
            elif Person_name not in self.staff_info.values():
                for current_room in self.living_spaces:
                    if Person_name in current_room.get_occupants():
                        current_room.occupants.remove(Person_name)
                        for self.Room_name in self.living_spaces:
                            self.Room_name.add_occupants(Person_name)
                return "Success"
            else:
                return "Ooops! cannot reallocate STAFF to living_space"

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
