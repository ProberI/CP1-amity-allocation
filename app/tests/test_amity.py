import unittest

from app.cp.amity import Amity
from app.cp.office import Office


class Test_amity_class(unittest.TestCase):

    def setUp(self):
        self.amity = Amity()

    def tearDown(self):
        del self.amity

    def test_create_room_with_wrong_room_type(self):
        self.assertEqual(self.amity.create_room("Quiet_Room", "Narnia"),
                         "Room_Type can only be OFFICE or LIVING_SPACE",
                         msg="Room_Type can only be OFFICE or LIVING_SPACE")

    def test_create_room_office(self):
        self.assertEqual(self.amity.create_room("Office", "Hogwarts"),
                         "OFFICE successfully created!")

    def test_create_room_living_space(self):
        self.assertEqual(self.amity.create_room("L", "Barmuda"),
                         "LIVING_SPACE successfully created!")

    def test_create_room_in_multiples(self):
        self.amity.create_room("Office", "Hogwarts", "Mombasa")
        self.assertEqual(len(self.amity.offices), 2)

    def test_create_room_office_with_o_as_input(self):
        self.assertEqual("OFFICE successfully created!",
                         self.amity.create_room("O", 'Hogwarts'))

    def test_create_room_living_space_with_l_as_input(self):
        self.assertEqual("LIVING_SPACE successfully created!",
                         self.amity.create_room("L", 'Hogwarts'))

    def test_create_room_duplicates(self):
        self.amity.rooms.append("Hogwarts")
        self.assertEqual(self.amity.create_room("O", "Hogwarts"),
                         "Room Hogwarts already exists!")

    def test_add_person_with_digit_in_name(self):
        self.assertEqual(self.amity.add_person("Paul2", "Upendo", "STAFF", "N"),
                         "Ooops! Name cannot contain a digit!",
                         msg="Name can only be String")

    def test_add_person_duplicate(self):
        self.amity.all_people.append("Paul Upendo")
        self.assertTrue(self.amity.add_person("Paul", "Upendo", "FELLOW", "N")
                        == "Ooops! Paul Upendo already exists in the system.")

    def test_add_person(self):
        self.amity.create_room("o", "Hogwarts")
        self.assertEqual(self.amity.add_person("John", "Waria", "STAFF", "N"),
                         'Person has been successfully added and allocated room')
        self.assertEqual(self.amity.add_person("Paul", "Upendo", "FELLOW", "Y"),
                         'Person has been successfully added and allocated room')

    def test_add_person_fellow_data_persisted(self):
        self.amity.add_person("John", "Waria", "FELLOW", "Y")
        self.amity.add_person("Jon", "Mondo", "FELLOW", "Y")
        self.assertTrue({'John WariaUID0': 'John Waria',
                         'Jon MondoUID1': 'Jon Mondo'} == self.amity.fellow_info)

    def test_add_person_staff_data_persisted(self):
        self.amity.add_person("John", "Waria", "STAFF", "N")
        self.assertTrue({'John WariaUID0': 'John Waria'}
                        == self.amity.staff_info)

    def test_add_person_with_number_as_name(self):
        self.assertTrue(self.amity.add_person(2, "Upendo", "STAFF", "N")
                        == "Name cannot be a number!")

    def test_add_person_with_unrecognized_roles(self):
        self.assertEqual(self.amity.add_person("John", "Maasai", "Member", "Y"),
                         "Role can only be STAFF or FELLOW")

    def test_add_person_with_wrong_accomodation_option(self):
        self.assertEqual(self.amity.add_person("Paul", "Upendo", "STAFF", "J"),
                         "Accomodation options are only 'Y' or 'N'")

    def test_add_person_staff_accomodation_options(self):
        self.assertEqual(self.amity.add_person("Paul", "Upendo", "STAFF", "Y"),
                         "Staff cannot have accomodation!")

    def test_reallocate_person(self):
        self.amity.create_room("o", "Hogwarts", "Narnia")
        self.amity.create_room("l", "Dojo")
        self.amity.add_person("Paul", "Upendo", "FELLOW", "Y")
        self.assertEqual(self.amity.rellocate_person("Paul Upendo", "Hogwarts"),
                         "Success")

    def test_reallocate_person_to_non_existent_room(self):
        self.amity.create_room("o", "Narnia")
        self.amity.add_person("Paul", "Upendo", "STAFF", "N")
        self.assertEqual(self.amity.rellocate_person("Paul Upendo", "Chania"),
                         "Oops sorry, this particular room does not exist!")

    def test_reallocate_person_who_is_not_in_system(self):
        self.amity.create_room("o", "Narnia")
        self.amity.add_person("Paul", "Upendo", "STAFF", "N")
        self.assertEqual(self.amity.rellocate_person("XCDEE", "Narnia"),
                         "Ooops, invalid employee_name please try again.")

    def test_reallocate_person_to_same_room(self):
        self.amity.create_room("o", "Narnia")
        self.amity.add_person("Paul", "Upendo", "STAFF", "N")
        self.assertEqual(self.amity.rellocate_person("Paul Upendo", "Narnia"),
                         "Ooops Upendo is already allocated to Narnia. No changes made")

    def test_reallocate_person_staff_to_living_space(self):
        self.amity.create_room("o", "Hogwarts")
        self.amity.create_room("l", "Egypt")
        self.amity.add_person("Paul", "Upendo", "STAFF", "N")
        self.assertEqual(self.amity.rellocate_person("Paul Upendo", "Egypt"),
                         "Ooops! cannot reallocate STAFF to living_space")

    # Test load_people function

    def test_load_people(self):
        self.assertEqual(self.amity.load_people("Names.txt"),
                         "Data successfully loaded")

    def test_print_room_non_existent(self):
        self.assertTrue(self.amity.print_room("Kenya") == "Ooops, plesase enter\
                        valid roomName")

    def test_print_room_occupants(self):
        self.assertEqual(self.amity.print_room("VALHALLA"),
                         ['Paul Upendo', 'John Chang'])
