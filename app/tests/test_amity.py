import unittest

from termcolor import cprint

from cp.amity import Amity


class Test_amity_class(unittest.TestCase):

    def setUp(self):
        self.amity = Amity()

    def tearDown(self):
        del self.amity

    def test_create_room_with_wrong_room_type(self):
        self.assertEqual(self.amity.create_room("Quiet_Room", "Narnia"),
                         cprint("Room_Type can only be OFFICE or LIVING_SPACE",
                                'red', attrs=['bold']))

    def test_create_room_office(self):
        self.assertEqual(self.amity.create_room("Office", "Hogwarts"),
                         cprint("OFFICE Hogwarts successfully created!",
                                'yellow', attrs=['bold']))

    def test_create_room_living_space(self):
        self.assertEqual(self.amity.create_room("L", "Barmuda"),
                         cprint("LIVING_SPACE Barmuda successfully created!",
                                'yellow', attrs=['bold']))

    def test_create_room_in_multiples(self):
        self.amity.create_room("Office", "Hogwarts", "Mombasa")
        self.assertEqual(len(self.amity.offices), 2)

    def test_create_room_office_with_o_as_input(self):
        self.assertEqual(cprint("OFFICE Hogwarts successfully created!",
                                'yellow', attrs=['bold']),
                         self.amity.create_room("O", 'Hogwarts'))

    def test_create_room_living_space_with_l_as_input(self):
        self.assertEqual(cprint("LIVING_SPACE Hogwarts successfully created!",
                                'yellow', attrs=['bold']),
                         self.amity.create_room("L", 'Hogwarts'))

    def test_create_room_duplicates(self):
        self.amity.rooms.append("Hogwarts")
        self.assertEqual(self.amity.create_room("O", "Hogwarts"),
                         cprint("Room Hogwarts already exists!", 'red',
                                attrs=['bold']))

    def test_add_person_with_digit_in_name(self):
        self.assertEqual(self.amity.add_person("Paul2", "Upendo", "STAFF", "N"),
                         cprint("Ooops! Name cannot contain a digit!", 'red',
                                attrs=['bold']))

    def test_add_person_duplicate(self):
        self.amity.all_people.append("Paul Upendo")
        self.assertTrue(self.amity.add_person("Paul", "Upendo", "FELLOW", "N")
                        == cprint("Ooops! Paul Upendo already exists in the system.",
                                  'red', attrs=['bold']))

    def test_add_person(self):
        self.amity.create_room("o", "Hogwarts", "Valhalla")
        self.amity.create_room("l", "Dojo")
        self.assertEqual(self.amity.add_person("John", "Waria", "STAFF", "N"),
                         cprint('Person has been successfully added and allocated room',
                                'yellow', attrs=['bold']))
        self.assertEqual(self.amity.add_person("Paul", "Upendo", "FELLOW", "Y"),
                         cprint('Person has been successfully added and allocated room',
                                'yellow', attrs=['bold']))

    def test_add_person_generatedID_in(self):
        self.amity.create_room("o", "Hogwarts", "Valhalla")
        self.amity.create_room("l", "Dojo")
        self.amity.add_person("John", "Waria", "FELLOW", "Y")
        self.amity.add_person("Jon", "Mondo", "FELLOW", "Y")
        self.assertTrue({'John WariaUID0': 'John Waria',
                         'Jon MondoUID1': 'Jon Mondo'} == self.amity.fellow_info)

    def test_add_person_staff_data_persisted(self):
        self.amity.create_room("o", "Hogwarts", "Valhalla")
        self.amity.create_room("l", "Dojo")
        self.amity.add_person("John", "Waria", "STAFF", "N")
        self.assertTrue({'John WariaUID0': 'John Waria'}
                        == self.amity.staff_info)

    def test_add_person_with_number_as_name(self):
        self.assertTrue(self.amity.add_person(2, "Upendo", "STAFF", "N")
                        == cprint("Name cannot be a number!", 'red', attrs=['bold']))

    def test_add_person_with_unrecognized_roles(self):
        self.assertEqual(self.amity.add_person("John", "Maasai", "Member", "Y"),
                         cprint("Role can only be STAFF or FELLOW", 'red', attrs=['bold']))

    def test_add_person_with_wrong_accomodation_option(self):
        self.assertEqual(self.amity.add_person("Paul", "Upendo", "STAFF", "J"),
                         cprint("Accomodation options are only 'Y' or 'N'", 'red',
                                attrs=['bold']))

    def test_add_person_staff_accomodation_options(self):
        self.assertEqual(self.amity.add_person("Paul", "Upendo", "STAFF", "Y"),
                         cprint("Staff cannot have accomodation!", 'red',
                                attrs=['bold']))

    def test_reallocate_person(self):
        self.amity.create_room("o", "Hogwarts", "Narnia")
        self.amity.create_room("l", "Dojo")
        self.amity.add_person("Paul", "Upendo", "FELLOW", "Y")
        self.assertEqual(self.amity.reallocate_person("Paul", "Upendo", "Hogwarts"),
                         cprint("Success", 'blue', attrs=['bold']))

    def test_reallocate_person_to_non_existent_room(self):
        self.amity.create_room("o", "Narnia")
        self.amity.add_person("Paul", "Upendo", "STAFF", "N")
        self.assertEqual(self.amity.reallocate_person("Paul", "Upendo", "Chania"),
                         cprint("Oops sorry, this particular room does not exist!",
                                'red', attrs=['bold']))

    def test_reallocate_person_who_is_not_in_system(self):
        self.amity.create_room("o", "Narnia")
        self.amity.add_person("Paul", "Upendo", "STAFF", "N")
        self.assertEqual(self.amity.reallocate_person("XCDEE", "BBB", "Narnia"),
                         cprint("Ooops, invalid employee_name please try again.",
                                'red', attrs=['bold']))

    def test_reallocate_person_to_same_room(self):
        self.amity.create_room("o", "Hogwarts", "Narnia")
        self.amity.add_person("Paul", "Upendo", "STAFF", "N")
        self.assertEqual(self.amity.reallocate_person("Paul", "Upendo", "Narnia"),
                         "Ooops already allocated here. No changes made")

    def test_reallocate_person_staff_to_living_space(self):
        self.amity.create_room("o", "Hogwarts")
        self.amity.create_room("l", "Egypt")
        self.amity.add_person("Paul", "Upendo", "STAFF", "N")
        self.assertEqual(self.amity.reallocate_person("Paul", "Upendo", "Egypt"),
                         "Ooops! cannot reallocate STAFF to living_space")

    def test_load_people(self):
        self.amity.create_room("o", "Hogwarts")
        self.amity.create_room("l", "Egypt")
        file_name = 'app/cp/names.txt'
        self.assertEqual(self.amity.load_people(file_name),
                         cprint("Data successfull loaded", 'yellow',
                                attrs=['bold']))

    def test_print_room_non_existent(self):
        self.amity.create_room("o", "VALHALLA")
        self.amity.add_person("Paul", "Upendo", "FELLOW", "N")
        self.amity.add_person("John", "Chang", "STAFF", "N")
        self.assertEqual(self.amity.print_room("Kenya"),
                         cprint("Ooops, please enter valid room name", 'red',
                                attrs=['bold']))

    def test_print_room(self):
        self.amity.create_room("o", "VALHALLA")
        self.amity.add_person("Paul", "Upendo", "FELLOW", "N")
        self.assertEqual(self.amity.print_room("VALHALLA"),
                         cprint(['Paul Upendo'], 'white', attrs=['bold']))

    def test_print_allocations(self):
        self.amity.create_room("o", "VALHALLA")
        self.amity.add_person("Paul", "Upendo", "FELLOW", "N")
        self.assertEqual(self.amity.print_allocations(),
                         cprint("Success\n", 'yellow', attrs=['bold']))
