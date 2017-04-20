import sys
import random
import string

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.model import Employees, All_rooms, Base
from model import model

from termcolor import colored, cprint
from tabulate import tabulate


from cp.living import Living
from cp.rooms import Rooms
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
        self.room_type = room_type
        for self.room_name in name:
            self.rooms.append(self.room_name)
            if self.rooms.count(self.room_name) > 1:
                err_msg = "Room %s already exists!" % self.room_name
                print(colored(err_msg + "\n", 'red', attrs=['bold']))
                return err_msg
            elif self.room_type.upper() == "OFFICE" or self.room_type.upper()\
                    == "O":
                self.room_type = "OFFICE"
                self.offices.append(Office(self.room_name))
                self.all_rooms.append(Office(self.room_name).get_room_name())
            elif self.room_type.upper() == "LIVING_SPACE" or\
                    self.room_type.upper() == "L":
                self.room_type = "LIVING_SPACE"
                self.living_spaces.append(Living(self.room_name))
                self.all_rooms.append(Living(self.room_name).get_room_name())
            else:
                print(colored("Room_Type can only be OFFICE or LIVING_SPACE\n",
                              'red', attrs=['bold']))
                return "Room_Type can only be OFFICE or LIVING_SPACE"

        msg = (self.room_type + " " + self.room_name + " successfully created!")
        print(colored(msg + "\n", 'yellow', attrs=['bold']))
        return msg

    def add_person(self, First_name, Last_Name, role, Accomodation="N"):
        self.First_name = First_name
        self.Last_Name = Last_Name
        self.Role = role
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
                if self.Role == "FELLOW":
                    self.fellow_info[self.Person_id] = self.person_name
                elif self.Role == "STAFF":
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
            - Prevent allocation of person to multiple rooms
        """

        if self.Role == "FELLOW":
            for fellow in self.fellow_info.values():
                fellow_id, selected_fellow = random.choice(list(self.fellow_info.items()))
                if self.Accomodation == "Y":
                    chosen_office = random.choice(self.offices)
                    chosen_office.add_occupants(selected_fellow)

                    chosen_living_space = random.choice(self.living_spaces)
                    chosen_living_space.add_occupants(selected_fellow)

                elif self.Accomodation == "N":

                    chosen_office = random.choice(self.offices)
                    chosen_office.add_occupants(selected_fellow)

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

                return "Ooops! allocation was Unsuccessful"

    def reallocate_person(self, employee_id, new_room):

        if new_room not in self.all_rooms:
            print(colored("Oops sorry, this particular room does not exist!",
                          'red', attrs=['bold']))
            return "Oops sorry, this particular room does not exist!"
        elif employee_id not in self.staff_info.keys() and employee_id not \
                in self.fellow_info.keys():
            print(self.staff_info.keys())
            print(self.fellow_info.keys())
            print(colored("Ooops, invalid employee_name please try again.", 'red',
                          attrs=['bold']))
            return "Ooops, invalid employee_name please try again."
        else:

            for fellow_id, fellow_name in self.fellow_info.items():
                if fellow_id == employee_id:
                    for office in self.offices:
                        if fellow_name in office.get_occupants():
                            office.occupants.remove(fellow_name)
                        if office.get_room_name() == new_room:
                            office.add_occupants(fellow_name)
                    cprint("Success", 'blue', attrs=['bold'])
                    return "Success"

                    for living in self.living_spaces:
                        if f_name in office.get_occupants():
                            living.occupants.remove(f_name)
                        if living.get_room_name() == new_room:
                            living.add_occupants(f_name)
                    cprint("Success", 'blue', attrs=['bold'])
                    return "Success"
                else:
                    cprint("Invalid Id. Please Use get_id command", 'red',
                           attrs=['bold'])
                    return "Invalid Id. Please Use get_id command"

            for staff_id, staff_name in self.staff_info.items():

                for living in self.living_spaces:
                    if new_room == living.get_room_name():
                        cprint("Ooops! cannot reallocate STAFF to living_space",
                               'red', attrs=['bold'])
                        return "Ooops! cannot reallocate STAFF to living_space"
                for office in self.offices:
                    if staff_name in office.get_occupants():
                        office.occupants.remove(staff_name)
                    if office.get_room_name() == new_room:
                        office.add_occupants(staff_name)
                cprint("Success", 'blue', attrs=['bold'])
                return "Success"

    def load_people(self, file_name):
        file_name = 'cp/names.txt'
        f = open(file_name, mode='r', encoding='utf-8')
        for line in f.readlines():
            data = line.split()
            first_name = data[0]
            last_name = data[1]
            role = data[2]
            if role.upper() == "STAFF":
                accomodation = "N"
            else:
                accomodation = data[3]

            self.add_person(first_name, last_name, role, accomodation)

        self.print_allocations()
        print(colored("Data successfull loaded", 'yellow', attrs=['bold']))
        return "Data successfull loaded"

    def print_allocations(self):
        table_room_data = []
        table_people_data = []
        for room_office in self.offices:
            self.allocations.append(room_office)

        for room_living in self.living_spaces:
            self.allocations.append(room_living)

        for allocated_rooms in self.allocations:
            table_room_data.append(allocated_rooms.get_room_name())
            table_people_data.append(allocated_rooms.get_occupants())

        print('\n' + tabulate({
            'Room_name': table_room_data,
            'Occupants': table_people_data
        }, headers="keys",
            tablefmt="fancy_grid") + '\n')

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

    def save_state(self, db_name):
        """
        TODO
            - Check if db exists
            - Check if record exists don't add it
        """
        if db_name == '':
            db_name = 'amity'
        else:
            self.db_name = db_name
            model.create_db(self.db_name)
            engine = create_engine('sqlite:///model/' + db_name + '.db')
            Base.metadata.bind = engine

            DBSession = sessionmaker(bind=engine)
            self.session = DBSession()

            if self.room_type == "OFFICE" or self.room_type == "LIVING_SPACE":
                for room in self.offices:
                    self.new_room = All_rooms()
                    self.new_room.Room_name = room.get_room_name()
                    self.new_room.Room_type = room.Rm_type
                    self.session.add(self.new_room)

                for room in self.living_spaces:
                    self.new_room = All_rooms()
                    self.new_room.Room_name = room.get_room_name()
                    self.new_room.Room_type = room.Rm_type
                    self.session.add(self.new_room)

            if self.Role == "FELLOW" or self.Role == "STAFF":
                for person_id, name in self.fellow_info.items():
                    self.new_person = Employees()
                    self.new_person.Emp_Id = person_id
                    self.new_person.Person_name = name
                    self.new_person.role = "FELLOW"
                    self.session.add(self.new_person)

                for staff_id, staff_name in self.staff_info.items():
                    self.new_person = Employees()
                    self.new_person.Emp_Id = staff_id
                    self.new_person.Person_name = staff_name
                    self.new_person.role = "STAFF"
                    self.session.add(self.new_person)

        self.session.commit()
        print(colored("Data saved successfuly", 'blue', attrs=['bold']))
        return "Data saved successfully"

    def load_state(self):
        try:
            room_data = ([str(x[0])for x in self.session.query(All_rooms.Room_name).all()])
            person_data = ([str(x[0])for x in self.session.query(Employees.Person_name).all()])
            for rum in room_data:
                self.rooms.append(rum)
            for Person in person_data:
                self.all_people.append(Person)
            return "success"
        except:
            return "No database"

    def get_person_id(self, first_name, last_name):
        """
        TODO
            - Add to docopt
        """
        full_name = first_name + " " + last_name
        for person_id, person_name in self.fellow_info.items():
            if person_name == full_name:
                print(colored(person_id, 'yellow', attrs=['bold']))
                return person_id
            else:
                return "Fail"

        for person_id, person_name in self.staff_info.items():
            if person_name == full_name:
                print(colored(person_id, 'yellow', attrs=['bold']))
                return person_id
            else:
                return "Fail"
