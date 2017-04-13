from app.cp.rooms import Rooms


class Living(Rooms):
    def __init__(self, room_name):
        super().__init__(room_name)
        self.room_capacity = 4
        self.occupants = []

    def add_occupants(self, occupant):

        if len(self.occupants) < self.room_capacity:
            self.occupants.append(occupant)
        else:
            return "Room Full"

    def get_occupants(self):
        return self.occupants
