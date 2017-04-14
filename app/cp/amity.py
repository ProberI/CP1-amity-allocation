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
        self.unallocated = []
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
                if self.Accomodation == "Y":
                    chosen_office = random.choice(self.offices)
                    chosen_office.add_occupants(selected_fellow)
                    for room_office in self.offices:
                        if len(room_office.occupants) > 0:
                            self.allocations.append(room_office)
                        else:
                            self.unallocated.append(room_office)

                    chosen_living_space = random.choice(self.living_spaces)
                    chosen_living_space.add_occupants(selected_fellow)
                    for room_living in self.living_spaces:
                        if len(room_living.occupants) > 0:
                            self.allocations.append(room_living)
                        else:
                            self.unallocated.append(room_living)
                elif self.Accomodation == "N":

                    chosen_office = random.choice(self.offices)
                    chosen_office.add_occupants(selected_fellow)
                    for room_office in self.offices:
                        if len(room_office.occupants) > 0:
                            self.allocations.append(room_office)
                        else:
                            self.unallocated.append(room_office)

                return "Ooops! allocation was Unsuccessful"

        elif self.Role == "STAFF":
            for staff in self.staff_info.values():
                staff_id, selected_staff = \
                    random.choice(list(self.staff_info.items()))
                if self.Accomodation == "Y":
                    return "Staff cannot have accomodation"
                elif self.Accomodation == "N":
                    chosen_office = random.choice(self.offices)
                    chosen_office.add_occupants(selected_staff)
                    for room_office in self.offices:
                        if len(room_office.occupants) > 0:
                            self.allocations.append(room_office)
                        else:
                            self.unallocated.append(room_office)
                return "Ooops! allocation was Unsuccessful"

    def rellocate_person(self, Person_name, Room_name):
        self.Room_name = Room_name
        self.Person_name = Person_name
        self.office_names = []
        self.living_s_names = []
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
        for _Room_name in self.offices:
            self.office_names.append(_Room_name.get_room_name())

        for rooms in self.living_spaces:
            self.living_s_names.append(rooms.get_room_name())
        for r in self.allocations:
            print("allocated", r.get_room_name(), r.occupants)
        for s in self.unallocated:
            print("Unallocated", s.get_room_name(), s.occupants)

        if self.Room_name not in self.all_rooms:
            return "Oops sorry, this particular room does not exist!"
        elif self.Person_name not in self.fellow_info.values() or\
                self.Person_name not in self.staff_info.values():
            return "Ooops, invalid employee_name please try again."
        elif self.Person_name in self.staff_info.values() and\
                self.Room_name in self.living_s_names:
            return "Ooops! cannot reallocate STAFF to living_space"
        else:
            pass

            # for _Room_name in self.offices:
            #     print(_Room_name.occupants)
            #     if self.Room_name in self.all_rooms:
            #         for room_selected in self.offices:
            #             self.Room_name == room_selected.get_room_name()
            #             if self.Room_name in self.all_rooms:
            #                 if len(room_selected.occupants) == 6:
            #                     return "Ooops!Office occupied. Please try another"
            #                 elif self.Person_name not in self.fellow_info.values() or\
            #                         self.Person_name not in self.staff_info.values():
            #                     return "Ooops, invalid employee_name please try again."
            #                 else:
            #                     for rooms in self.offices:
            #                         if self.Person_name in rooms.occupants:
            #                             rooms.occupants.remove(self.Person_name)
            #                             room_selected.add_occupants(self.Person_name)
            #                         return "Success"
            #
            #     else:
            #         for room_selected in self.living_spaces:
            #             if self.Room_name == room_selected.get_room_name():
            #                 if self.Room_name in self.all_rooms:
            #                     if len(room_selected.occupants) == 4:
            #                         return "Ooops! Living_space Occupied. Plaese try another"
            #                     elif self.Person_name in self.staff_info.values():
            #                         return "Ooops! cannot reallocate STAFF to living_space"
            #                     elif self.Person_name not in self.fellow_info.values():
            #                         return "Ooops, invalid employee_name please try again."
            #                     else:
            #                         for rooms in self.living_spaces:
            #                             if self.Person_name in rooms.occupants:
            #                                 rooms.occupants.remove(self.Person_name)
            #                                 room_selected.add_occupants(self.Person_name)
            #                             return "Success"
            #     if self.Room_name not in _Room_name.get_room_name():
            #         return "Oops sorry, this particular room does not exist!"

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
