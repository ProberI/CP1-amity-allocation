import unittest
from app.cp.amity import Amity


class Test_Amity_Class(unittest.TestCase):

    def setUp(self):
        self.amity = Amity()

    def tearDown(self):
        del self.amity

    """
    Tests for the create_room function in class Amity.
    The tests validate input and output data and also see if
    specified constraints are met and EdgeCases are handled. create_room
    function takes the room_name and Room_Type as arguments.
    """

    def test_CreatingRoom_with_wrong_RoomType(self):
        self.assertEqual(self.amity.create_room("Narnia", "Quiet_Room"),
                         "Room_Type can only be OFFICE or LIVING_SPACE",
                         msg="Room_Type can only be OFFICE or LIVING_SPACE")

    def test_Created_Rooms_persisted(self):
        self.amity.create_room("Hogwarts", "Office")
        self.assertListEqual([{'OFFICE': 'Hogwarts'}], self.amity.all_rooms)

    def test_Successful_Office_Creation(self):
        self.assertEqual(self.amity.create_room("Hogwarts", "Office"),
                         "OFFICE successfully created!")

    def test_Successful_Living_Space_Creation(self):
        self.assertTrue(self.amity.create_room("Barmuda", "L") ==
                        "LIVING_SPACE successfully created!")

    def test_Creation_of_MultipleRooms_at_once(self):
        self.amity.create_room("Hogwarts Mombasa", "Office")
        self.assertListEqual(self.amity.offices, ['Hogwarts', 'Mombasa'])

    def test_Living_Space_isnt_created_when_office_is_specified(self):
        self.assertNotEqual("LIVING_SPACE successfully created!",
                            self.amity.create_room('Hogwarts', "O"))

    def test_OFFICE_isnt_created_when_office_is_specified(self):
        self.assertNotEqual("OFFICE successfully created!",
                            self.amity.create_room('Hogwarts', "L"))

    def test_creation_of_exiting_room(self):
        self.amity.rooms.append("Hogwarts")
        self.assertTrue(self.amity.create_room("Hogwarts", "O") ==
                        "Room Hogwarts already exists!")

    """
    Test Cases for add_person function.
    The add person function takes PersonName,
    Role plus Accomodation options.
    """

    def test_AddingPerson_with_integers_as_name(self):
        self.assertEqual(self.amity.add_person("Paul2", "Upendo", "STAFF", "N"),
                         "Ooops! Name cannot contain a digit!",
                         msg="Name can only be String")

    def test_adding_existing_person(self):
        self.amity.all_people.append("Paul Upendo")
        self.assertTrue(self.amity.add_person("Paul", "Upendo", "FELLOW", "N") ==
                        "Ooops! Paul Upendo already exists in the system.")

    def test_person_ID_format(self):
        self.assertTrue(self.amity.add_person("John", "Waria", "FELLOW", "Y") ==
                        [{'John WariaUID0': 'John Waria'}])

    def test_addind_person_with_number_as_name(self):
        self.assertTrue(self.amity.add_person(2, "Upendo", "STAFF", "N")
                        == "Name cannot be a number!")

    def test_AddingPeople_with_unrecognized_roles(self):
        self.assertTrue(self.amity.add_person("John", "Maasai", "Member", "Y")
                        == "Role can only be STAFF or FELLOW")

    def test_Worong_accomodation_option(self):
        self.assertEqual(self.amity.add_person("Paul", "Upendo", "STAFF", "J"),
                         "Accomodation options are only 'Y' or 'N'")

    def test_If_Staff_be_accomodated(self):
        self.assertEqual(self.amity.add_person("Paul", "Upendo", "STAFF", "Y"),
                         "Staff cannot have accomodation!")

    """ Allocation and Reallocation"""

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
        self.amity.allocate_room()
        self.assertEqual(self.amity.print_room("VALHALLA"),
                         ['Paul Upendo', 'John Chang'])


if __name__ == '__main__':
    unittest.main()
