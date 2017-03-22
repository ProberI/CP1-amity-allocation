import sys
sys.path.insert(0, '/Users/Upendo/Documents/CP1/CP1-amity-allocation')
import unittest
from cp.Amity import Amity
from cp.Living import Living
from cp.Rooms import Rooms
from cp.Office import Office


class TestModel(unittest.TestCase):

    def setUp(self):
        self.amity = Amity()

    """ Tests if classes are correctly inheriting as expected """

    def test_Office_Inheritance(self):
        self.assertTrue(issubclass(Office, Rooms))

    def test_Living_inheritance(self):
        issubclass(Rooms, Living)

    """ Tests for the create_room function in class Amity.
    The tests validate input and output data and also see if
    specified constraints are met. """

    def test_Room_wrong_value_input(self):
        self.assertEqual("Wrong input",
                         self.amity.create_room("Narnia", "Toilet"))

    def test_Room_existance(self):
        self.assertIn('Hogwarts', self.amity.create_room("Hogwarts", "Office"))
        # check inside self.rooms if that room name exists

    def test_Room_correct_input(self):
        self.assertEqual([{True: 'Hogwarts'}],
                         self.amity.create_room("Hogwarts", "Office"))

        # Test Multiple Room Insertion

    def test_Multiple_Room_Creation(self):
        self.assertEqual([{True: 'Hogwarts'}, {True: 'Mombasa'}],
                         self.amity.create_room("Hogwarts Mombasa", "Office"))

    def test_Living_max_capacity_exceeded(self):
        self.living = Living()
        self.assertEqual("You have exceeded maximum",
                         self.living.numTest("Paul Kagwe Enjoy Kagwe Mungai"))

    def test_living_capacity_output(self):
        self.living = Living()
        self.assertEqual(['Paul', 'Kagwe', 'Enjoy', 'Kagwe'],
                         self.living.numTest("Paul Kagwe Enjoy Kagwe"))

# Ensure O and L return appropriate Bool values

    def test_Room_Type_assertion(self):
        self.assertNotEqual({False: 'Hogwarts'},
                            self.amity.create_room('Hogwarts', "O"))


# Test if room exists
# Test room capacity
# Test Room Allocation
# Test accomodation differences STAFF Y raise error


"""
    # Test for appropriate class names

    def test_Amity(self):
        self.assertEqual('Amity', amity.getName())

    def test_Person(self):
        self.assertEqual('Person', person.getName())

    def test_Rooms(self):
        self.assertEqual('Rooms', rooms.getName())

    def test_Staff(self):
        self.assertEqual('Staff', rooms.getName())

    # Tests to check if classes correctly inherit
    def test_FellowInherit(self):
        issubclass(Person, Fellow)

    def test_StaffInherit(self):
        issubclass(Person, Staff)
"""


if __name__ == "__main__":
    unittest.main()
