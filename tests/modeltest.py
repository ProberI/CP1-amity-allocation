import unittest
import


class TestModel(unittest.TestCase):
    def setUp(self):
        self.amity = Amity()
        self.living = Living()

# Test Room Type

    def test_CorrectRtype(self):
        self.assertEqual("Wrong input",
                         self.amity.create_room("Narnia", "Beaureau"))
# Test Multiple Room Insertion

    def test_Room_Insertion(self):
        self.assertIs(self, {True: 'Hogwarts', True: 'Mombasa'},
                      self.amity.create_room("Hogwarts Mombasa", "Office"))

    def test_Room_max(self):
        self.assertEqual("You have exceeded maximum",
                         self.living.numTest("Paul Kagwe Enjoy Kagwe Mungai"))

    def test_Room_min(self):
        self.assertEqual(['Paul', 'Kagwe', 'Enjoy', 'Kagwe'],
                         self.living.numTest("Paul Kagwe Enjoy Kagwe"))
# Ensure O and L return appropriate Boo values

    def test_Room_Type(self):
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

    def test_OfficeInherit(self):
        issubclass(Rooms, Office)

    def test_LivingInherit(self):
        issubclass(Rooms, Living)
"""


if __name__ == "__main__":
    unittest.main()
