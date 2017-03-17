import unittest


class TestModel(unittest.TestCase):

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
