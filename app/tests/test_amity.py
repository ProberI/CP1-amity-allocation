import unittest

from termcolor import colored

from cp.amity import Amity


class Test_amity_class(unittest.TestCase):

    def setUp(self):
        self.amity = Amity()

    def tearDown(self):
        del self.amity

    def test_create_room_with_wrong_room_type(self):
        self.assertEqual(self.amity.create_room("Quiet_Room", ["Narnia"]),
                         (colored("Room_Type can only be OFFICE or LIVING_SPACE\n",
                                  'red', attrs=['bold'])))

    def test_create_room_office(self):
        self.assertEqual(self.amity.create_room("Office", ["Hogwarts"]),
                         (colored("Successfull creation!\n",
                                  'green', attrs=['bold'])))

    def test_create_room_living_space(self):
        self.assertEqual(self.amity.create_room("L", ["Barmuda"]),
                         (colored("Successfull creation!\n",
                                  'green', attrs=['bold'])))

    def test_create_room_in_multiples(self):
        self.amity.create_room("Office", ["Hogwart", "Mombasa"])
        self.assertEqual(len(self.amity.offices), 2)

    def test_create_room_office_with_o_as_input(self):
        self.assertEqual((colored("Successfull creation!\n", 'green',
                                  attrs=['bold'])),
                         self.amity.create_room("O", ['Hogwarts']))

    def test_create_room_living_space_with_l_as_input(self):
        self.assertEqual((colored("Successfull creation!\n",
                                  'green', attrs=['bold'])),
                         self.amity.create_room("L", ['Hogwrts']))

    def test_create_room_duplicates(self):
        self.amity.create_room("O", ["Hogwarts"])
        self.assertEqual(self.amity.create_room("O", ["Hogwarts"]),
                         (colored("Room Hogwarts already exists!\n", 'red',
                                  attrs=['bold'])))

    def test_add_person_with_digit_in_name(self):
        self.amity.create_room("o", ["Narnia"])
        self.assertEqual(self.amity.add_person("Paul2", "Upendo", "STAFF", "N"),
                         (colored("Ooops! Name cannot contain a digit!\n", 'red',
                                  attrs=['bold'])))

    def test_add_person_with_special_char_in_name(self):
        self.amity.create_room("o", ["Narnia"])
        self.assertEqual(self.amity.add_person("Paul$", "Upe&do", "STAFF", "N"),
                         (colored("Ooops! Name cannot contain a special character!\n",
                                  'red', attrs=['bold'])))

    def test_add_person_duplicate(self):
        self.amity.create_room("o", ["Mara", "Uganda"])
        self.amity.create_room("l", ["Doj"])
        self.amity.add_person("Paul", "Upendo", "FELLOW", "N")
        self.amity.load_state('Try')
        self.assertEqual(self.amity.add_person("Paul", "Upendo", "FELLOW", "N"),
                         (colored(("Ooops! Paul Upendo already exists in the system.\n"),
                                  'red', attrs=['bold'])))

    def test_add_person(self):
        self.amity.create_room("o", ["ogwarts", "Valhal"])
        self.amity.create_room("l", ["Dojo"])
        self.assertEqual(self.amity.add_person("John", "Waria", "STAFF", "Y"),
                         colored("Person has been successfully added\n",
                                 'green', attrs=['bold']))
        self.assertEqual(self.amity.add_person("Paul", "Upendo", "FELLOW", "Y"),
                         colored("Person has been successfully added\n",
                                 'green', attrs=['bold']))

    @unittest.expectedFailure  # Id is randomly generated
    def test_add_person_generatedID_in(self):
        self.amity.create_room("o", ["Hogwars", "Valhalla"])
        self.amity.create_room("l", ["Dojo"])
        self.amity.add_person("John", "Waria", "FELLOW", "Y")
        self.amity.add_person("Jon", "Mondo", "FELLOW", "Y")
        self.assertEqual({'GHYUK': 'John Waria',
                          'HYJIK': 'Jon Mondo'}, self.amity.fellow_info)

    @unittest.expectedFailure  # Id is randomly generated
    def test_add_person_staff_data_persisted(self):
        self.amity.create_room("o", ["Hogwarts", "Valhalla"])
        self.amity.create_room("l", ["Dojo"])
        self.amity.add_person("John", "Waria", "STAFF", "N")
        self.assertTrue({'XHGYR': 'John Waria'}
                        == self.amity.staff_info)

    def test_add_person_with_number_as_name(self):
        self.amity.create_room("o", ["Narnia"])
        self.assertTrue(self.amity.add_person(2, "Upendo", "STAFF", "N")
                        == (colored("Name cannot be a number!\n", 'red',
                                    attrs=['bold'])))

    def test_add_person_with_unrecognized_roles(self):
        self.amity.create_room("o", ["Narnia"])
        self.assertEqual(self.amity.add_person("John", "Maasai", "Member", "Y"),
                         (colored("Role can only be STAFF or FELLOW\n", 'red',
                                  attrs=['bold'])))

    def test_add_person_with_wrong_accomodation_option(self):
        self.amity.create_room("o", ["Narnia"])
        self.assertEqual(self.amity.add_person("Paul", "Upendo", "STAFF", "J"),
                         (colored("Accomodation options are only 'Y' or 'N'\n",
                                  'red', attrs=['bold'])))

    @unittest.expectedFailure  # print statement instead of return
    def test_add_person_staff_accomodation_options(self):
        self.amity.create_room("o", ["Narnia"])
        self.assertEqual(self.amity.add_person("Paul", "Upendo", "STAFF", "Y"),
                         colored("Living_space cannot allocated be to staff\n", 'red',
                                 attrs=['bold']))

    @unittest.expectedFailure
    def test_reallocate_person_from_office(self):
        self.amity.create_room("o", ["Narnia", "Hogwarts"])
        self.amity.add_person("Paul", "Upendo", "FELLOW", "N")
        person_id = self.amity.get_person_id("Paul", "Upendo")
        self.assertEqual(self.amity.reallocate_person(person_id, "Narnia"),
                         colored("Success", 'green', attrs=['bold']))

    @unittest.expectedFailure
    def test_reallocate_person_from_living_space(self):
        self.amity.create_room("o", ["Narnia", "Hogwarts"])
        self.amity.create_room("l", ["Dojo", "amity"])
        self.amity.add_person("Paul", "Upendo", "FELLOW", "Y")
        person_id = self.amity.get_person_id("Paul", "Upendo")
        self.assertEqual(self.amity.reallocate_person(person_id, "Amity"),
                         colored("Success", 'green', attrs=['bold']))

    def test_reallocate_person_with_no_data_in_system(self):
        self.assertEqual(self.amity.reallocate_person('XXXX', 'Hogwarts'),
                         (colored("Ooops!Can't reallocate with no rooms and people.",
                                  'red', attrs=['bold'])))

    def test_reallocate_person_to_same_office(self):
        err_msg = 'Ooops! cannot reallocate person to same room\n'
        self.amity.create_room("o", ["Valhalla"])
        self.amity.add_person("Paul", "Upendo", "staff", "n")
        person_id = self.amity.get_person_id("Paul", "Upendo")
        self.assertEqual((self.amity.reallocate_person(person_id, "valhalla")),
                         colored(err_msg, 'red', attrs=['bold']))

    def test_reallocate_person_to_same_living_space(self):
        err_msg = 'Ooops! cannot reallocate person to same room\n'
        self.amity.create_room("o", ["Valhalla"])
        self.amity.create_room("L", ["Mara"])
        self.amity.add_person("Paul", "Upendo", "fellow", "y")
        person_id = self.amity.get_person_id("Paul", "Upendo")
        self.assertEqual((self.amity.reallocate_person(person_id, "Mara")),
                         colored(err_msg, 'red', attrs=['bold']))

    def test_reallocate_person_to_non_existent_room(self):
        self.amity.create_room("o", ["Narnia"])
        self.amity.add_person("Paul", "Upendo", "fellow", "N")
        person_id = self.amity.get_person_id("Paul", "Upendo")
        self.assertEqual(self.amity.reallocate_person(person_id, "Chania"),
                         (colored("Oops sorry, this particular room does not exist!",
                                  'red', attrs=['bold'])))

    def test_reallocate_person_who_is_not_in_system(self):
        self.amity.create_room("o", ["Narnia"])
        self.amity.add_person("Paul", "Upendo", "STAFF", "N")
        self.assertEqual(self.amity.reallocate_person("XCCDF",  "Narnia"),
                         (colored("Ooops, invalid employee_id please try again.",
                                  'red', attrs=['bold'])))

    def test_reallocate_person_staff_to_living_space(self):
        self.amity.create_room("o", ["Hogwarts"])
        self.amity.create_room("l", ["Egypt"])
        self.amity.add_person("Paul", "Upendo", "STAFF", "N")
        person_id = self.amity.get_person_id("Paul", "Upendo")
        self.assertEqual(self.amity.reallocate_person(person_id, "Egypt"),
                         colored("Ooops!cannot reallocate STAFF to living_space\n",
                                 'red', attrs=['bold']))

    def test_load_people(self):
        self.amity.create_room("o", ["Hogwarts", "Mombasa"])
        self.amity.create_room("l", ["Egypt"])
        file_name = 'app/cp/names.txt'
        self.assertEqual(self.amity.load_people(file_name),
                         (colored("Data successfull loaded", 'yellow',
                                  attrs=['bold'])))

    def test_print_room_non_existent(self):
        self.amity.create_room("o", ["VALHALLA"])
        self.amity.add_person("Paul", "Upendo", "FELLOW", "N")
        self.amity.add_person("John", "Chang", "STAFF", "N")
        self.assertEqual(self.amity.print_room("Kenya"),
                         (colored("Ooops, this room does not exist", 'red',
                                  attrs=['bold'])))

    def test_print_room(self):
        self.amity.create_room("O", ["VALHALLA"])
        self.amity.add_person("Paul", "Upendo", "FELLOW", "N")
        self.amity.add_person("Paul", "Kay", "FELLOW", "N")
        self.assertEqual(self.amity.print_room("VALHALLA"),
                         colored("\nSuccessfull print.", 'green',
                                 attrs=['bold']))

    def test_print_allocations(self):
        self.amity.create_room("o", ["VALHALLA"])
        self.amity.create_room("l", ["VALH"])
        self.amity.add_person("Paul", "Upendo", "FELLOW", "y")
        self.assertEqual(self.amity.print_allocations(),
                         (colored("Success\n", 'green', attrs=['bold'])))

    def test_print_allocations_without_rooms(self):
        self.assertEqual(self.amity.print_allocations(),
                         colored("Ooops! No rooms created yet\n", 'red',
                                 attrs=['bold']))

    def test_print_allocations_without_person_data(self):
        self.amity.create_room("o", ["Hogwarts"])
        self.assertEqual(self.amity.print_room('Hogwarts'),
                         colored("Ooops!Hogwarts is empty\n", 'yellow',
                                 attrs=['bold']))

    def test_save_state(self):
        self.amity.create_room("o", ["VAHALLA", "Mobasa"])
        self.amity.create_room("L", ["Dojo"])
        self.amity.add_person("Paul", "Upendo", "FELLOW", "Y")
        self.amity.add_person("Pau", "Upend", "STAFF", "N")
        self.assertEqual(self.amity.save_state("Try"), (colored(
            "Data saved successfuly\n", 'blue', attrs=['bold'])))
        self.assertEqual(self.amity.load_state('Try'),
                         colored("success", 'green', attrs=['bold']))

    def test_get_person_id(self):
        self.amity.create_room("o", ["VALHALLA", "Mombasa"])
        self.amity.add_person("Paul", "Upendo", "STAFF", "N")
        self.assertEqual(self.amity.get_person_id("Pal", "Upeno"),
                         "Ooops! Pal Upeno does not exist")

    def test_list_people_without_data(self):
        msg = 'Ooops! No Employee or staff data available at the moment\n'
        self.assertEqual(self.amity.list_people(), colored(msg, 'yellow',
                                                           attrs=['bold']))

    def test_list_people(self):
        self.amity.add_person("Paul", "Upendo", "FELLOW", "Y")
        self.amity.add_person("Pau", "Upend", "STAFF", "N")
        self.assertEqual(self.amity.list_people(), colored(
            'Employee listing success.', 'green', attrs=['bold']))

    def test_list_rooms(self):
        self.amity.create_room("o", ["VALHALLA", "Mombasa"])
        self.amity.create_room("L", ["Dojo"])
        self.assertEqual(self.amity.list_rooms(), colored(
            'Room listing success.\n', 'green', attrs=['bold']))

    def test_list_rooms_without_existence(self):
        msg = 'Ooops! No rooms exist yet\n'
        self.assertEqual(self.amity.list_rooms(),
                         colored(msg, 'yellow', attrs=['bold']))

    def test_delete_person_non_existent(self):
        self.assertEqual(self.amity.delete_person('KHYC'),
                         (colored("Ooops! This particular Id doesn't exist",
                                  'red', attrs=['bold'])))

    def test_delete_person(self):
        self.amity.add_person('Paul', 'Upendo', 'FELLOW', 'N')
        person_id = self.amity.get_person_id('Paul', 'Upendo')
        self.assertEqual(self.amity.delete_person(person_id),
                         colored('Operation success!', 'green',
                                 attrs=['bold']))
