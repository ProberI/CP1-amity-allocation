from app.cp.rooms import Rooms


class Office(Rooms):
    def __init__(self, room_name):
        super().__init__(room_name)
        self.room_capacity = 6

    def add_occupants(self, occupant):
        self.occupants = []
        if len(self.occupants) < self.room_capacity:
            self.occupants.append(occupant)
        else:
            return "Room Full"
