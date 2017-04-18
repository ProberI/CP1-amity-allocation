import sys

import random

import string

from termcolor import colored, cprint

# from sqlalchemy import create_engine
#
# from sqlalchemy.orm import sessionmaker
#
# from cp.model import Amity_employees, Amity_rooms

from cp.living import Living
from cp.office import Office
from cp.fellow import Fellow
from cp.staff import Staff


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

    def create_room(self, room_type, name):
        """
        TODO
            - Use load state to verify is room already exists.
        """
        self.room_type = room_type
        for room_name in name:
            self.rooms.append(room_name)
            if self.rooms.count(room_name) > 1:
                err_msg = "Room %s already exists!" % room_name
                print(colored(err_msg + "\n", 'red', attrs=['bold']))
                return err_msg
            elif self.room_type.upper() == "OFFICE" or self.room_type.upper()\
                    == "O":
                self.room_type = "OFFICE"
                self.offices.append(Office(room_name))
                self.all_rooms.append(Office(room_name).get_room_name())
            elif self.room_type.upper() == "LIVING_SPACE" or\
                    self.room_type.upper() == "L":
                self.room_type = "LIVING_SPACE"
                self.living_spaces.append(Living(room_name))
                self.all_rooms.append(Living(room_name).get_room_name())
            else:
                print(colored("Room_Type can only be OFFICE or LIVING_SPACE\n",
                              'red', attrs=['bold']))
                return "Room_Type can only be OFFICE or LIVING_SPACE"

        msg = (self.room_type + " " + room_name + " successfully created!")
        print(colored(msg + "\n", 'yellow', attrs=['bold']))
        return msg

    def add_person(self, First_name, Last_Name, Role, Accomodation="N"):
        self.First_name = First_name
        self.Last_Name = Last_Name
        self.Role = Role
        self.Accomodation = Accomodation
        try:
            self.person_name = (Fellow(self.First_name,
                                       self.Last_Name).get_name())
            self.Person_id = self.genarate_user_ID()
            self.all_people.append(self.person_name)
            if any(char.isdigit() for char in self.person_name):
                print (colored("Ooops! Name cannot contain a digit!\n", 'red',
                               attrs=['bold']))
                return "Ooops! Name cannot contain a digit!"

            elif self.all_people.count(self.person_name) > 1:
                print (colored(("Ooops! %s already exists in the system.\n"
                                % self.person_name), 'red', attrs=['bold']))
                return "Ooops! %s already exists in the system." % self.person_name

            elif self.Role not in ("STAFF", "FELLOW"):
                print (colored("Role can only be STAFF or FELLOW\n", 'red',
                               attrs=['bold']))
                return "Role can only be STAFF or FELLOW"
            elif self.Accomodation not in ("Y", "N"):
                print (colored("Accomodation options are only 'Y' or 'N'\n", 'red',
                               attrs=['bold']))
                return "Accomodation options are only 'Y' or 'N'"
            elif self.Role == "STAFF" and self.Accomodation == "Y":
                print (colored("Staff cannot have accomodation!\n", 'red',
                               attrs=['bold']))
                return "Staff cannot have accomodation!"
            else:
                self.fellow_info[self.Person_id] = self.person_name
                self.staff_info[self.Person_id] = self.person_name
                self.allocate_room_randomly()
                print(colored("Person has been successfully added an allocated room\n",
                              'yellow', attrs=['bold']))
                return "Person has been successfully added and allocated room"

        except TypeError:
            print (colored("Name cannot be a number!\n", 'red', attrs=['bold']))
            return "Name cannot be a number!"

    def genarate_user_ID(self):
        person_id = ''.join([random.choice(string.ascii_uppercase)
                             for n in range(5)])
        return person_id

    def allocate_room_randomly(self):
        """
        TODO
            - Check if no rooms are available and raise an error
        """

        if self.Role == "FELLOW":
            for fellow in self.fellow_info.values():
                fellow_id, selected_fellow = random.choice(list(self.fellow_info.items()))
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
                staff_id, selected_staff = random.choice(list(self.staff_info.items()))
                if self.Accomodation == "Y":
                    print(colored("Staff cannot have accomodation", 'red',
                                  attrs=['bold']))
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

    def reallocate_person(self, First_name, Last_name, Room_name):
        """
        TODO
            -Verify and solve reallocation
            -Make realloactions work
        """
        self.Room_name = Room_name
        self.Person_name = First_name + " " + Last_name
        self.office_names = []
        self.living_s_names = []

        for _Room_name in self.offices:
            self.office_names.append(_Room_name.get_room_name())

        for rooms in self.living_spaces:
            self.living_s_names.append(rooms.get_room_name())
        for r in self.allocations:
            print("allocated", r.get_room_name(), r.occupants)
        for s in self.unallocated:
            print("Unallocated", s.get_room_name(), s.occupants)

        if self.Room_name not in self.all_rooms:
            print(colored("Oops sorry, this particular room does not exist!",
                          'red', attrs=['bold']))
            return "Oops sorry, this particular room does not exist!"
        elif self.Person_name not in self.fellow_info.values() or\
                self.Person_name not in self.staff_info.values():
            print(colored("Ooops, invalid employee_name please try again.", 'red',
                          attrs=['bold']))
            return "Ooops, invalid employee_name please try again."
        elif self.Person_name in self.staff_info.values() and\
                self.Room_name in self.living_s_names:
            print(colored("Ooops! cannot reallocate STAFF to living_space", 'red',
                          attrs=['bold']))
            return "Ooops! cannot reallocate STAFF to living_space"

        elif self.Room_name == r.get_room_name() and r.room_capacity == 4:
            r.occupants.remove(self.Person_name)
            if rooms == self.Room_name:
                rooms.add_occupants(self.Person_name)
                print(colored("Success", 'blue', attrs=['bold']))
                return "Success"

        elif self.Room_name == r.get_room_name() and r.room_capacity == 6:
            r.occupants.remove(self.Person_name)

            if _Room_name == self.Room_name:
                _Room_name.add_occupants(self.Person_name)
                print(colored("Success", 'blue', attrs=['bold']))
                return "Success"

    def load_people(self, file_name):
        """
        TODO
            - Let add_person loop through file data >> only one person is added
        """
        file_name = 'cp/names.txt'
        f = open(file_name, mode='r', encoding='utf-8')
        for line in f.readlines():
            data = line.split()
            first_name = data[0]
            last_name = data[1]
            role = data[2]
            accomodation = data[3]
            if role.upper() == "STAFF":
                accomodation = "N"
            self.add_person(first_name, last_name, role, accomodation)
            self.print_allocations()
            print(colored("Data successfull loaded", 'yellow', attrs=['bold']))
            return "Data successfull loaded"

    def print_allocations(self):
        for allocated_rooms in self.allocations:
            print("======================\n"
                  + str(allocated_rooms.get_room_name()) + "\n"
                  + "-------------------\n"
                  + str(allocated_rooms.get_occupants()) + "\n"
                  + "=====================\n")
        print(colored("Success\n", 'yellow', attrs=['bold']))
        return "Success"

    def print_unallocated(self):
        pass

    def print_room(self, room_name):
        """
        TODO
            - If room is empty give a message
        """
        self.room_name = room_name
        if self.room_name not in self.all_rooms:
            print(colored("Ooops, please enter valid room name", 'red',
                          attrs=['bold']))
            return "Ooops, please enter valid room name"
        for allocated_rooms in self.allocations:
            if allocated_rooms.get_room_name() == self.room_name:
                return cprint(allocated_rooms.get_occupants(), 'white',
                              attrs=['bold'])

    # def save_state(self, db_name):
    #     engine = create_engine(db_name)
    #     Base.metadata.bind = engine
    #
    #     DBSession = sessionmaker(bind=engine)
    #     session = DBSession()
    #
    #     new_employee = Employees()
    #     new_employee.Emp_Id = self.Person_id
    #     new_employee.first_name = self.fellow_info.person_name
    #     # new_employee.last_name =

    def load_state(self):
        pass
