import sys
sys.path.insert(0, '/Users/Upendo/Documents/CP1/CP1-amity-allocation')
import unittest
from cp.Amity import Amity
from cp.Living import Living
from cp.Rooms import Rooms
from cp.Office import Office
from cp.Person import Person
from cp.Fellow import Fellow
from cp.Staff import Staff


class TestModel(unittest.TestCase):

    def setUp(self):
        self.amity = Amity()

    """
    ---------------------------------------------------
    Tests for the create_room function in class Amity.
    The tests validate input and output data and also see if
    specified constraints are met.
    --------------------------------------------------- """

    def test_CreatingRoom_with_wrong_RoomType(self):
        self.assertEqual(self.amity.create_room("Narnia", "Quiet_Room"),
                         "Room_Type can only be Office or Living_Space",
                         msg="Room_Type can only be Office or Living_Space")

    def test_CreatedRoom_persisted(self):
        self.amity.create_room("Hogwarts", "Office")
        self.assertIn({'Office': 'Hogwarts'}, self.amity.all_rooms)

    def test_Successful_Office_Creation(self):
        self.assertEqual(self.amity.create_room("Hogwarts", "Office"),
                         "Office successfully created!")

    def test_Successful_Living_space_Creation(self):
        self.assertEqual(self.amity.create_room("Barmuda", "L"),
                         "Living_Space successfully created!")

    def test_Creation_of_MultipleRooms_at_once(self):
        self.assertEqual(self.amity.create_room("Hogwarts Mombasa", "Office"),
                         "Office successfully created!")

    def test_Creation_of_Office_with_O_as_RoomType_Input(self):
        self.assertNotEqual("Living_Space successfully created!",
                            self.amity.create_room('Hogwarts', "O"))

    def test_creation_of_exiting_room(self):
        self.amity.create_room("Hogwarts", "O")
        self.assertEqual(self.amity.create_room("Hogwarts", "O"),
                         "Room Hogwarts already exists!")

    def test_rooms_with_same_name_not_persisted(self):
        # recheck
        self.amity.create_room("VALHALLA VALHALLA", "O")
        self.assertFalse(self.amity.all_rooms.count("VALHALLA") == 2)
    """
    -----------------------------
    Test add_person functionality
    ----------------------------- """

    def test_AddingPerson_with_integers_as_name(self):
        self.assertEqual(self.amity.add_person(2, "STAFF", "N"),
                         "Name can only be String", msg="Name can only be String")

    def test_AddingPeople_with_unrecognized_roles(self):
        self.assertEqual("Role can only be STAFF or FELLOW",
                         self.amity.add_person("John", "Member", "Y"))

    def test_Worong_accomodation_option(self):
        self.assertEqual("Accomodation options are only Y or N",
                         self.amity.add_person("Paul", "STAFF", "J"))

    def test_If_Staff_be_accomodated(self):
        self.assertEqual(self.amity.add_person("Paul", "STAFF", "Y"),
                         "Staff cannot have accomodation!")

    def test_Adding_Fellow_with_accomodation(self):
        self.assertEqual(self.amity.add_person("Paul", "FELLOW", "Y"),
                         "Living_Space successfully allocated")

    def test_Adding_Fellow_without_accomodation(self):
        self.assertEqual(self.amity.add_person("Paul", "FELLOW", "N"),
                         "Living_Space not allocated.")

    """
    -----------------------
    Room reallocation tests
    ----------------------- """

    def test_Reallocating_Person_without_a_room(self):
        self.assertEqual(self.amity.rellocate_person("UID002", "Hogwarts"),
                         "This person was not allocated a room previously.")

    def test_Reallocation_Success(self):
        self.assertEqual(self.amity.rellocate_person("UID001", "Hogwarts"),
                         "Person successfully reallocated")

    def test_Reallocating_to_nonExistent_Room(self):
        self.assertEqual(self.amity.rellocate_person("UID001", "Narnia"),
                         "Oops sorry, this particular room name does not exist!")

    def test_Reallocation_of_NonExistent_person(self):
        self.assertEqual(self.amity.rellocate_person("XCDEE", "Narniaa"),
                         "Ooops, incorrect Person ID format or doesn't exist!")

    def test_Reallocation_to_same_room(self):
        self.assertEqual(self.amity.rellocate_person("UID001", "Hogwarts"),
                         "Ooops Upendo is already allocated to Hogwarts")

    def test_reallocating_staff_to_livingSpace_fails(self):
        self.amity.create_room("Egypt", "L")
        self.amity.add_person("PAUL", "STAFF", "N")
        self.assertTrue(self.amity.rellocate_person("STF001", "Egypt") ==
                        "Ooops Staff cannot be reallocated to a living_Space")

    def test_Successfull_allocation(self):
        self.assertEqual(self.amity.allocate_room(),
                         "Office and Living_space successfuly allocated")

    # Test load_people function

    def test_successfull_people_load(self):
        self.assertEqual(self.amity.load_people("Names.txt"),
                         "Data successfully loaded")

    def test_outputFormat_for_allocations(self):
        self.assertEqual(self.amity.print_allocations(),
                         'ROOM NAME "\n" ------------------------------------\
                         "\n" MEMBER 1, MEMBER 2, MEMBER 3')

    def test_printing_non_existent_room(self):
        self.assertTrue(self.amity.print_room("Kenya") == "Ooops, plesase enter\
                        valid roomName")

    def test_print_persons_in_a_room(self):
        # Think logic
        self.amity.allocate_room()
        self.assertEqual(self.amity.print_room("VALHALLA"),
                         ['Paul Upendo', 'John Chang'])

    def tearDown(self):
        del self.amity


if __name__ == "__main__":
    unittest.main()
