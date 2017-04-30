from cp.rooms import Rooms

from termcolor import colored


class Office(Rooms):
    def __init__(self, room_name):
        super().__init__(room_name)
        self.room_capacity = 6
        self.Rm_type = "OFFICE"
        self.occupants = []

    def add_occupants(self, occupant):

        if len(self.occupants) < self.room_capacity:
            self.occupants.append(occupant)
        else:
            return colored("Room Full", 'red', attrs=['bold'])

    def get_occupants(self):
        return self.occupants
