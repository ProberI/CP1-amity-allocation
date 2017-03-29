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

# Test if room exists
# Test room capacity
# Test Room Allocation
# Test accomodation differences STAFF Y raise error

    """
    ---------------------------------------------------
    Tests for the create_room function in class Amity.
    The tests validate input and output data and also see if
    specified constraints are met.
    ---------------------------------------------------
    """

    def test_wrong_Room_Type_Input(self):
        self.assertEqual(self.amity.create_room("Narnia", "Quiet_Room"),
                         "Room_Type can only be Office or Living_Space",
                         msg="Room_Type can only be Office or Living_Space")

    def test_if_Room_already_exists(self):
        self.assertEqual(self.amity.create_room("Hogwarts Hogwarts", "Office"),
                         "Rooms already exists")

    def test_Office_type_creation(self):
        self.assertEqual(self.amity.create_room("Hogwarts", "Office"),
                         "Office successfully created!")

    def test_living_space_creation(self):
        self.assertEqual(self.amity.create_room("Barmuda", "L"),
                         "Living_Space successfully created!")

    def test_Multiple_Room_Creation(self):
        self.assertEqual(self.amity.create_room("Hogwarts Mombasa", "Office"),
                         "Office successfully created!")

    def test_Created_RoomTYpe_Is_Office(self):
        self.assertNotEqual("Living_Space successfully created!",
                            self.amity.create_room('Hogwarts', "O"))

    def test_PersonName_as_String_Only(self):
        self.assertEqual(self.amity.add_person(2, "STAFF", "N"),
                         "Name can only be String", msg="Name can only be String")

    def test_Correct_RoleType(self):
        self.assertEqual("Role can only be STAFF or FELLOW",
                         self.amity.add_person("John", "Member", "Y"))

    def test_Accomodation_Input_options(self):
        self.assertEqual("Accomodation options are only Y or N",
                         self.amity.add_person("Paul", "STAFF", "J"))

    def test_If_Staff_be_accomodated(self):
        self.assertEqual(self.amity.add_person("Paul", "STAFF", "Y"),
                         "Staff cannot have accomodation!")

    def test_if_Fellow_Can_be_accomodated(self):
        self.assertEqual(self.amity.add_person("Paul", "FELLOW", "Y"),
                         "Living_Space successfully allocated")

    def test_if_fellow_doesnt_want_accomodation(self):
        self.assertEqual(self.amity.add_person("Paul", "FELLOW", "N"),
                         "Living_Space not allocated.")

    def test_ReallocationUID_had_Previous_Room(self):
        self.assertEqual(self.amity.rellocate_person("UID002", "Hogwarts"),
                         "This person was not allocated a room previously.")

    def test_Reallocation_Success(self):
        self.assertEqual(self.amity.rellocate_person("UID001", "Hogwarts"),
                         "Person successfully reallocated")
        pass

    def test_room_4ReallocationExists(self):
        self.assertEqual(self.amity.rellocate_person("UID001", "Narnia"),
                         "Oops sorry, this particular room name does not exist!")

    def test_PersonID_exists(self):
        self.assertEqual(self.amity.rellocate_person("XCDEE", "Narniaa"),
                         "Ooops, incorrect Person ID format or doesn't exist!")

    def test_allocation(self):
        self.assertEqual(self.amity.allocate_room("Paul", "FELLOW", "Y"),
                         "Office and Living_space successfuly allocated")

    def test_same_room_reallocation(self):
        self.assertEqual(self.amity.rellocate_person("UID001", "Hogwarts"),
                         "Ooops Upendo is already allocated to Hogwarts")

    """ Tests add_person function. """
# def test_Living_max_capacity_exceeded(self):
#     """ Check logic for this"""
#     pass
#
# def test_living_capacity_output(self):
#     """ Check logic for this"""
#     pass
#
# def test_Room_occupied(self):
#
#     pass
#
# def test_RoomSpace_Avalilable(self):
#     pass


if __name__ == "__main__":
    unittest.main()
