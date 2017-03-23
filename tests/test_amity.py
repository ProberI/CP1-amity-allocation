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

    """ Tests if classes are correctly inheriting as expected """
# Test if room exists
# Test room capacity
# Test Room Allocation
# Test accomodation differences STAFF Y raise error

    def test_Office_Inheritance(self):
        self.assertTrue(issubclass(Office, Rooms))

    def test_Living_inheritance(self):
        self.assertTrue(issubclass(Living, Rooms))

    def test_FellowInherit(self):
        self.assertTrue(issubclass(Fellow, Person))

    def test_StaffInherit(self):
        self.assertTrue(issubclass(Staff, Person))

    """ Tests for the create_room function in class Amity.
    The tests validate input and output data and also see if
    specified constraints are met. """

    def test_Room_wrong_value_input(self):
        self.assertEqual("Wrong input",
                         self.amity.create_room("Narnia",
                                                "Toilet"), msg="Incorrect input")

    def test_Room_existance(self):
        self.assertIn('Hogwarts', self.amity.create_room("Hogwarts", "Office"))
        # check inside self.rooms if that room name exists

    def test_Office_type_creation(self):
        self.assertEqual([{"Office": 'Hogwarts'}],
                         self.amity.create_room("Hogwarts", "Office"))

    def test_living_space_creation(self):
        self.assertEqual([{"Living_Space": "Barmuda"}],
                         self.amity.create_room("Barmuda", "L"))

        # Test Multiple Room Insertion

    def test_Multiple_Room_Creation(self):
        self.assertEqual([{"Office": 'Hogwarts'}, {"Office": 'Mombasa'}],
                         self.amity.create_room("Hogwarts Mombasa", "Office"))

    def test_Living_max_capacity_exceeded(self):
        self.living = Living()
        self.assertEqual("You have exceeded maximum",
                         self.living.numTest("Paul Kagwe Enjoy Kagwe Mungai"))

    def test_living_capacity_output(self):
        self.living = Living()
        self.assertEqual(self.living.numTest("Paul Kagwe Enjoy Kagwe"),
                         ['Paul', 'Kagwe', 'Enjoy', 'Kagwe'])

    def test_Room_Type_assertion(self):
        self.assertNotEqual({False: 'Hogwarts'},
                            self.amity.create_room('Hogwarts', "O"))

    """ Tests add_person function. """

    def test_person_name_as_string(self):
        with self.assertRaises(TypeError):
            self.amity.add_person(2, "STAFF", "N")

    def test_role(self):
        with self.assertRaises(ValueError):
            self.amity.add_person("John", "Member", "Y")

    def test_accomodation(self):
        with self.assertRaises(ValueError):
            self.amity.add_person("Paul", "STAFF", "J")

    def test_staff_accomodation(self):
        self.assertEqual(self.amity.add_person("Paul", "STAFF", "Y"),
                         "Staff cannot have accomodation!")

    def test_fellow_accomodation(self):
        self.assertEqual(self.amity.add_person("Paul", "FELLOW", "Y"),
                         "Living_Space successfully allocated")

    def test_fellow_doesnt_want_accomodation(self):
        self.assertEqual(self.amity.add_person("Paul", "FELLOW", "N"),
                         "Living_Space not allocated.")


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

"""


if __name__ == "__main__":
    unittest.main()
