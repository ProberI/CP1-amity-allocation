import random
import string

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc
from model.model import Employees, All_rooms, Base
from model import model

from termcolor import colored, cprint
from tabulate import tabulate


from cp.living import Living
from cp.office import Office
from cp.fellow import Fellow
from cp.staff import Staff


class Amity():

    def __init__(self):
        self.all_people = []
        self.all_office_names = []
        self.all_living_names = []
        self.allocations = []
        self.unallocated = []
        self.offices = []
        self.living_spaces = []
        self.fellow_info = {}
        self.staff_info = {}
        self.all_rooms = []
        global my_person_id

    def create_room(self, room_type, name):
        self.room_type = room_type

        for room_name in name:

            if self.room_type.upper() not in ("LIVING_SPACE", "LIVING", "OFFICE",
                                              "O", "L"):

                return (colored("Room_Type can only be OFFICE or LIVING_SPACE\n",
                                'red', attrs=['bold']))
            elif self.all_rooms.count(room_name.upper()) >= 1:
                err_msg = "Room %s already exists!" % room_name
                return (colored(err_msg + "\n", 'red', attrs=['bold']))
            elif (self.room_type.upper() in ["OFFICE", "O"]):
                self.room_type = "OFFICE"
                self.offices.append(Office(room_name.upper()))
                self.all_office_names.append(room_name.upper())
                self.all_rooms.append(room_name.upper())
                office_msg = (self.room_type + " " + room_name + " successfully created!")
                cprint(office_msg + '\n', 'green', attrs=['bold'])
            elif (self.room_type.upper() in ["LIVING_SPACE", "L", "LIVING"]):
                self.room_type = "LIVING_SPACE"
                self.living_spaces.append(Living(room_name.upper()))
                self.all_living_names.append(room_name.upper())
                self.all_rooms.append(room_name.upper())
                living_msg = (self.room_type + " " + room_name + " successfully created!")
                cprint(living_msg + '\n', 'green', attrs=['bold'])
        msg = ("Successfull creation!")
        return (colored(msg + "\n", 'green', attrs=['bold']))

    def add_person(self, First_name, Last_Name, role, Accomodation="N"):
        self.First_name = First_name
        self.Last_Name = Last_Name
        self.Role = role
        self.Accomodation = Accomodation
        special = [r'''\\''', r'''+''', r'''-''', r'''&''', r'''|''', r'''!''',
                   r'''(''', r''')''', r'''{''', r'''}''', r'''[''', r''']''',
                   r'''^''', r'''~''', r'''*''', r'''?''', r''':''', r'''"''',
                   r''';''']

        try:
            self.person_name = First_name + " " + Last_Name
            if any(char.isdigit() for char in self.person_name):
                return (colored("Ooops! Name cannot contain a digit!\n", 'red',
                                attrs=['bold']))
            elif any(char in special for char in self.person_name):
                return (colored("Ooops! Name cannot contain a special character!\n",
                                'red', attrs=['bold']))

            elif self.Role.upper() not in ("STAFF", "FELLOW"):
                return (colored("Role can only be STAFF or FELLOW\n", 'red',
                                attrs=['bold']))

            elif self.Accomodation.upper() not in ("Y", "N"):
                return (colored("Accomodation options are only 'Y' or 'N'\n",
                                'red', attrs=['bold']))

            elif self.all_people.count(self.person_name.upper()) >= 1:
                return (colored(("Ooops! %s already exists in the system.\n"
                                 % self.person_name), 'red', attrs=['bold']))

            else:
                if self.Role.upper() == "FELLOW":
                    self.Person_id = self.genarate_user_ID()
                    person_name = (Fellow(self.First_name, self.Last_Name).get_name())
                    self.fellow_info[self.Person_id] = person_name.upper()
                    self.all_people.append(self.person_name.upper())
                elif self.Role.upper() == "STAFF":
                    self.Person_id = self.genarate_user_ID()
                    person_name = (Staff(self.First_name, self.Last_Name).get_name())
                    self.staff_info[self.Person_id] = person_name.upper()
                    self.all_people.append(self.person_name.upper())
                self.allocate_room_randomly()
                return colored("Person has been successfully added\n", 'green',
                               attrs=['bold'])

        except TypeError:
            return (colored("Name cannot be a number!\n", 'red', attrs=['bold']))

    @staticmethod
    def genarate_user_ID():
        person_id = ''.join([random.choice(string.ascii_uppercase)
                             for n in range(5)])
        return person_id

    def allocate_room_randomly(self):
        if self.Role.upper() == "FELLOW":

            for fellow in self.fellow_info.values():
                listt = []
                listt.append(fellow)
            selected_fellow = random.choice(listt)

            if self.Accomodation.upper() == "Y":
                if self.offices:
                    for office in self.offices:
                        if selected_fellow not in office.occupants:
                            chosen_office = random.choice(self.offices)
                    chosen_office.add_occupants(selected_fellow)

                    if selected_fellow in chosen_office.get_occupants():
                        cprint("Office allocated.\n", 'green', attrs=['bold'])
                    else:
                        cprint("Office not allocated\n", 'yellow', attrs=['bold'])
                        if selected_fellow not in self.unallocated:
                            self.unallocated.append(selected_fellow)
                        else:
                            pass
                else:
                    if selected_fellow not in self.allocations:
                        cprint("Office not allocated. Please create office\n",
                               'yellow', attrs=['bold'])
                        self.unallocated.append(selected_fellow)
                    else:
                        pass

                if self.living_spaces:
                    for living in self.living_spaces:
                        if selected_fellow not in living.occupants:
                            chosen_living_space = random.choice(self.living_spaces)
                    chosen_living_space.add_occupants(selected_fellow)

                    if selected_fellow in chosen_living_space.get_occupants():
                        cprint("Living_space allocated.\n", 'green', attrs=['bold'])
                    else:
                        cprint("Living_space not allocated\n", 'yellow', attrs=['bold'])
                        if selected_fellow not in self.unallocated:
                            self.unallocated.append(selected_fellow)
                        else:
                            pass
                else:
                    if selected_fellow not in self.unallocated:
                        self.unallocated.append(selected_fellow)
                        cprint("Living_space not allocated.Please create living_space\n",
                               'yellow', attrs=['bold'])
                    else:
                        pass

            elif self.Accomodation.upper() == "N":
                if self.offices:
                    for office in self.offices:
                        if selected_fellow not in office.occupants:
                            chosen_office = random.choice(self.offices)
                    chosen_office.add_occupants(selected_fellow)

                    if selected_fellow in chosen_office.get_occupants():
                        cprint("Office allocated.\n", 'green', attrs=['bold'])
                    else:
                        cprint("Office not allocated\n", 'yellow', attrs=['bold'])
                        if selected_fellow not in self.unallocated:
                            self.unallocated.append(selected_fellow)
                        else:
                            pass
                else:
                    if selected_fellow not in self.unallocated:
                        self.unallocated.append(selected_fellow)
                        cprint("Office not allocated. Please create office\n",
                               'yellow', attrs=['bold'])
                    else:
                        pass

        elif self.Role.upper() == "STAFF":
            for staff in self.staff_info.values():
                staff_list = []
                staff_list.append(staff)
            selected_staff = random.choice(staff_list)

            if self.Accomodation.upper() == "Y":
                if self.offices:
                    for office in self.offices:
                        if selected_staff not in office.occupants:
                            chosen_office = random.choice(self.offices)
                    chosen_office.add_occupants(selected_staff)
                    if selected_staff in chosen_office.get_occupants():
                        cprint("Office allocated.\n", 'green', attrs=['bold'])
                        cprint("Living_space cannot allocated be to staff\n", 'red',
                               attrs=['bold'])
                    else:
                        cprint("Office not allocated\n", 'yellow', attrs=['bold'])
                        if selected_staff not in self.unallocated:
                            self.unallocated.append(selected_staff)
                        else:
                            pass
                else:
                    if selected_staff not in self.unallocated:
                        self.unallocated.append(selected_staff)
                        cprint("Office not allocated. Please create office\n",
                               'yellow', attrs=['bold'])
                        cprint("Living_space cannot allocated be to staff\n", 'red',
                               attrs=['bold'])
                    else:
                        pass

            elif self.Accomodation.upper() == "N":
                if self.offices:
                    for office in self.offices:
                        if selected_staff not in office.occupants:
                            chosen_office = random.choice(self.offices)
                    chosen_office.add_occupants(selected_staff)
                    if selected_staff in chosen_office.get_occupants():
                        cprint("Office allocated.\n", 'green', attrs=['bold'])
                    else:
                        cprint("Office not allocated\n", 'yellow', attrs=['bold'])
                        if selected_staff not in self.unallocated:
                            self.unallocated.append(selected_staff)
                        else:
                            pass
                else:
                    if selected_staff not in self.unallocated:
                        self.unallocated.append(selected_staff)
                        cprint("Office not allocated. Please create office\n",
                               'yellow', attrs=['bold'])
                    else:
                        pass
        if self.offices:
            for office in self.offices:
                if office.occupants and office not in self.allocations:
                    self.allocations.append(office)
        elif self.living_spaces:
            for living in self.living_spaces:
                if living.occupants and living not in self.allocations:
                    self.allocations.append(living)

    def reallocate_person(self, employee_id, new_room):
        if(employee_id.upper() not in self.staff_info.keys() and employee_id.upper() not
                in self.fellow_info.keys() and new_room.upper() not in self.all_rooms):
            return (colored("Ooops!Can't reallocate with no rooms and people.",
                            'red', attrs=['bold']))

        elif new_room.upper() not in self.all_rooms:
            return (colored("Oops sorry, this particular room does not exist!",
                            'red', attrs=['bold']))
        elif (employee_id.upper() not in self.staff_info.keys() and employee_id.upper() not
                in self.fellow_info.keys()):
            return (colored("Ooops, invalid employee_id please try again.", 'red',
                            attrs=['bold']))
        else:
            if employee_id.upper() in self.fellow_info.keys():
                msg = 'Ooops! cannot reallocate person to same room\n'
                if new_room.upper() in self.all_office_names:
                    for fellow_id, fellow_name in self.fellow_info.items():
                        if fellow_id == employee_id.upper():
                            for office in self.offices:
                                if fellow_name in office.get_occupants():
                                    if new_room.upper() in office.get_room_name():
                                        return colored(msg, 'red', attrs=['bold'])
                                    else:
                                        office.occupants.remove(fellow_name)

                                if new_room.upper() in office.get_room_name():
                                    office.add_occupants(fellow_name)
                                    self.allocations.append(office)
                                    if fellow_name in self.unallocated:
                                        self.unallocated.remove(fellow_name)
                    return colored("Success", 'green', attrs=['bold'])

                elif new_room.upper() in self.all_living_names:
                    msg = 'Ooops! cannot reallocate person to same room\n'
                    for fellow_id, fellow_name in self.fellow_info.items():
                        if fellow_id == employee_id.upper():
                            for living in self.living_spaces:
                                if fellow_name in living.get_occupants():
                                    if new_room.upper() in living.get_room_name():
                                        return colored(msg, 'red', attrs=['bold'])
                                    else:
                                        living.occupants.remove(fellow_name)
                                if new_room.upper() in living.get_room_name():
                                    living.add_occupants(fellow_name)
                                    self.allocations.append(living)
                                    if fellow_name in self.unallocated:
                                        self.unallocated.remove(fellow_name)

                    return colored("Success", 'green', attrs=['bold'])

            if employee_id.upper() in self.staff_info.keys():
                err_msg = 'Ooops! cannot reallocate person to same room\n'
                msg = "Ooops!cannot reallocate STAFF to living_space\n"
                for staff_id, staff_name in self.staff_info.items():
                    if staff_id == employee_id.upper():
                        for living in self.living_spaces:
                            if new_room.upper() == living.get_room_name():
                                return colored(msg, 'red', attrs=['bold'])

                        for office in self.offices:
                            if staff_name in office.get_occupants():

                                if new_room.upper() in office.get_room_name():
                                    return colored(err_msg, 'red', attrs=['bold'])
                                else:
                                    office.occupants.remove(staff_name)
                            if new_room.upper() in office.get_room_name():
                                office.add_occupants(staff_name)
                                self.allocations.append(office)
                                if staff_name in self.unallocated:
                                    self.unallocated.remove(staff_name)

                return colored("Success", 'green', attrs=['bold'])

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
            print(self.add_person(first_name, last_name, role, accomodation))
        return (colored("Data successfull loaded", 'yellow', attrs=['bold']))

    def print_allocations(self, filename=''):
        table_room_data = []
        table_people_data = []
        table_room_type = []
        if not self.all_rooms:
            return colored("Ooops! No rooms created yet\n", 'red', attrs=['bold'])
        else:
            for room_office in self.offices:
                if not room_office.occupants:
                    cprint("No occupants in %s" % room_office.get_room_name(),
                           'red', attrs=['bold'])
                elif room_office in self.allocations and not room_office.occupants:
                    self.allocations.remove(room_office)
                elif room_office.occupants:
                    if room_office not in self.allocations:
                        self.allocations.append(room_office)

            for room_living in self.living_spaces:
                if not room_living.occupants:
                    cprint("No occupants in %s" % room_living.get_room_name(),
                           'red', attrs=['bold'])
                elif room_living in self.allocations and not room_living.occupants:
                    self.allocations.remove(room_living)
                elif room_living.occupants:
                    if room_living not in self.allocations:
                        self.allocations.append(room_living)

            for allocated_rooms in self.allocations:
                if allocated_rooms.get_room_name() not in table_room_data:
                    if allocated_rooms.occupants:
                        table_room_data.append(allocated_rooms.get_room_name())
                        table_room_type.append(allocated_rooms.Rm_type)
                        table_people_data.append(' '.join(str(x)
                                                          for x in allocated_rooms.get_occupants()))
            if filename:

                try:
                    file_obj = open(filename, 'w')

                    try:

                        for room in self.allocations:
                            file_obj.write('\n')
                            file_obj.write('Room_name: ' + room.get_room_name())
                            file_obj.write('\n' + '-' * 30 + '\n')
                            file_obj.write(', '.join(room.get_occupants()))
                            file_obj.write('\n')
                    finally:
                        file_obj.close()
                except IOError as e:
                    return str(e)

            else:

                print('\n' + tabulate({
                    'Room_name': table_room_data,
                    'Room_type': table_room_type,
                    'Occupants': table_people_data
                }, headers="keys",
                    tablefmt="fancy_grid") + '\n')

        return (colored("Success\n", 'green', attrs=['bold']))

    def print_unallocated(self, filename=''):
        if not self.unallocated:
            return colored("Yeiiy!! All persons are currently allocated.",
                           'green', attrs=['bold'])
        else:
            if filename:
                try:
                    file_obj = open(filename, 'w')

                    try:
                        file_obj.write('\n UNALLOCATED PEOPLE')
                        file_obj.write('\n' + '-' * 30 + '\n')
                        file_obj.write(', '.join(self.unallocated))
                    finally:
                        file_obj.close()

                except IOError as e:
                    return str(e)
            else:
                print('\n' + tabulate({
                    'UNALLOCATED PEOPLE': self.unallocated}, headers='keys',
                    tablefmt="fancy_grid") + '\n')
                return colored("Success", 'green', attrs=['bold'])

    def print_room(self, room_name):
        if room_name.upper() not in self.all_rooms:
            return(colored("Ooops, this room does not exist", 'red',
                           attrs=['bold']))
        elif self.offices or self.living_spaces:
            for room in self.offices:
                if room_name.upper() in room.get_room_name() and not room.occupants:
                    return colored("Ooops!%s is empty\n" % room_name, 'yellow',
                                   attrs=['bold'])
            for room in self.living_spaces:
                if room_name.upper() in room.get_room_name() and not room.occupants:
                    return colored("Ooops!%s is empty\n" % room_name, 'yellow',
                                   attrs=['bold'])
        if self.allocations:
            for rooms in self.allocations:
                if room_name.upper() in rooms.get_room_name():
                    occupants = rooms.get_occupants()
            cprint(occupants, 'white',
                   attrs=['bold'])

        return colored("\nSuccessfull print.", 'green', attrs=['bold'])

    def save_state(self, db_name=''):
        if db_name:
            self.db_name = db_name
            file_name = self.db_name + '.db'

            engine = create_engine('sqlite:///model/' + file_name)
            Base.metadata.drop_all(engine)
            Base.metadata.create_all(engine)
            Base.metadata.bind = engine
            model.create_db(self.db_name)
            DBSession = sessionmaker(bind=engine)
            self.session = DBSession()
        else:
            self.db_name = 'amity'
            file_name = self.db_name + '.db'
            engine = create_engine('sqlite:///model/' + file_name)
            Base.metadata.drop_all(engine)
            Base.metadata.create_all(engine)
            Base.metadata.bind = engine
            model.create_db(self.db_name)
            DBSession = sessionmaker(bind=engine)
            self.session = DBSession()

        try:
            if (not self.offices and not self.living_spaces and
                    not self.fellow_info and not self.staff_info):

                return colored("No data to save", 'yellow', attrs=['bold'])

            for room in self.offices:
                self.new_room = All_rooms()
                self.new_room.Room_name = room.get_room_name()
                self.new_room.Room_type = "OFFICE"
                self.new_room.Occupants = ' '.join(str(x) for
                                                   x in room.get_occupants())
                self.session.add(self.new_room)

            for room in self.living_spaces:
                self.new_room = All_rooms()
                self.new_room.Room_name = room.get_room_name()
                self.new_room.Room_type = "LIVING_SPACE"
                self.new_room.Occupants = ' '.join(str(x) for
                                                   x in room.get_occupants())
                self.session.add(self.new_room)

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
            return (colored("Data saved successfuly\n", 'blue', attrs=['bold']))

        except exc.SQLAlchemyError as error:
            print(error)

    def load_state(self, db_name):

        try:
            engine = create_engine('sqlite:///model/' + db_name + '.db')
            Base.metadata.bind = engine

            DBSession = sessionmaker(bind=engine)

            self.session = DBSession()

            office_data = ([str(x[0])for x in
                            self.session.query(All_rooms.Room_name).filter
                            (All_rooms.Room_type == 'OFFICE')])
            living_data = ([str(x[0])for x in
                            self.session.query(All_rooms.Room_name).filter
                            (All_rooms.Room_type == 'LIVING_SPACE')])

            fellow_data = ([str(x[0])for x in
                            self.session.query(Employees.Person_name).filter(Employees.role == "FELLOW")])

            staff_data = ([str(x[0])for x in
                           self.session.query(Employees.Person_name).filter(Employees.role == "STAFF")])

            for Person in fellow_data:
                self.Role = "FELLOW"
                self.all_people.append(Person)
                person_id = ''.join([str(x[0])for x in
                                     self.session.query(Employees.Emp_Id).filter(Employees.Person_name == Person)])

                self.fellow_info[person_id] = Person

            for person in staff_data:
                self.Role = "STAFF"
                self.all_people.append(person)
                person_id = ''.join([str(x[0])for x in
                                     self.session.query(Employees.Emp_Id).filter(Employees.Person_name == person)])

                self.staff_info[person_id] = person

            for rum in office_data:
                self.room_type = "OFFICE"
                self.all_rooms.append(rum)

                self.offices.append(Office(rum))
                self.all_office_names.append(rum)

                for office in self.offices:
                    occupants = ' '.join([str(x[0])for x in
                                          self.session.query(All_rooms.Occupants).filter(All_rooms.Room_name == rum)])
                    if office.get_room_name() in rum:
                        if rum not in self.allocations:
                            self.allocations.clear()
                            self.allocations.append(office)
                            if occupants not in office.occupants:
                                office.occupants.clear()
                                office.add_occupants(occupants)

            for rum in living_data:
                self.room_type = "LIVING_SPACE"
                self.all_rooms.append(rum)

                self.living_spaces.append(Living(rum))
                self.all_living_names.append(rum)

                for living in self.living_spaces:
                    occupants = ' '.join([str(x[0])for x in
                                          self.session.query(All_rooms.Occupants).filter(All_rooms.Room_name == rum)])
                    if living.get_room_name() in rum:
                        if rum not in self.allocations:
                            self.allocations.clear()
                            self.allocations.append(living)
                            if occupants not in living.occupants:
                                living.occupants.clear()
                                living.add_occupants(occupants)

            return colored("success", 'green', attrs=['bold'])
        except exc.SQLAlchemyError as error:
            if error:
                return "No database"

    def get_person_id(self, first_name, last_name):
        full_name = first_name + " " + last_name
        if full_name.upper() in self.fellow_info.values():
            for person_id, person_name in self.fellow_info.items():
                if person_name == full_name.upper():
                    my_person_id = person_id
            return my_person_id
        elif full_name.upper() in self.staff_info.values():
            for person_id, person_name in self.staff_info.items():
                if person_name == full_name.upper():
                    my_person_id = person_id

            return my_person_id
        else:
            return "Ooops! %s does not exist" % full_name

    def list_people(self):
        ids = []
        names = []
        staff_ids = []
        staff_names = []
        msg = 'Ooops! No Employee or staff data available at the moment\n'
        if self.staff_info or self.fellow_info:
            for fellow_id, fellow_name in self.fellow_info.items():
                ids.append(fellow_id)
                names.append(fellow_name)

            for staff_id, staff_name in self.staff_info.items():
                staff_ids.append(staff_id)
                staff_names.append(staff_name)

            cprint(('\n' + 'FELLOW DATA' + '\n' + '=' * 30 + '\n'), 'green')
            print('\n' + tabulate({
                'Fellow_id': ids,
                'Fellow_name': names},
                headers='keys',
                tablefmt="fancy_grid") + '\n')

            cprint(('\n' + 'STAFF DATA' + '\n' + '=' * 30 + '\n'), 'green')
            print('\n' + tabulate({
                'Staff_id': staff_ids,
                'Staff_names': staff_names},
                headers='keys',
                tablefmt='fancy_grid') + '\n')

            return colored('Employees list success.', 'green', attrs=['bold'])
        else:
            return colored(msg, 'yellow', attrs=['bold'])
