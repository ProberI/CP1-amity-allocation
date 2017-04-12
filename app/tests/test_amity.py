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

    # Allocation and Reallocation tests

    def test_reallocate_person_not_allocated(self):
        self.assertEqual(self.amity.rellocate_person("UID002", "Hogwarts"),
                         "This person was not allocated a room previously.")

    def test_reallocate_person(self):
        self.assertEqual(self.amity.rellocate_person("UID001", "Hogwarts"),
                         "Person successfully reallocated")

    def test_reallocate_preson_to_non_existent_room(self):
        self.assertEqual(self.amity.rellocate_person("UID001", "Narnia"),
                         "Oops sorry, this particular room name does not exist!")

    def test_reallocate_preson_non_existent(self):
        self.assertEqual(self.amity.rellocate_person("XCDEE", "Narniaa"),
                         "Ooops, incorrect Person ID format or doesn't exist!")

    def test_reallocate_person_to_same_room(self):
        self.assertEqual(self.amity.rellocate_person("UID001", "Hogwarts"),
                         "Ooops Upendo is already allocated to Hogwarts")

    def test_reallocate_person_staff_to_living_space(self):
        self.amity.create_room("Egypt", "L")
        self.amity.add_person("PAUL", "STAFF", "N")
        self.assertTrue(self.amity.rellocate_person("STF001", "Egypt") ==
                        "Ooops Staff cannot be reallocated to a living_Space")

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
