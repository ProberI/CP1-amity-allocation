import unittest


class TestModel(unittest.TestCase):
    def setUp(self):
        amity = Amity()
        rooms = Rooms()
        staff = Staff()
        fellow = Fellow()
        staff = Staff()
        person = Person()

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


if __name__ == "__main__":
    unittest.main()
