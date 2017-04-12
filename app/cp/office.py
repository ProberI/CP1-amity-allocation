from app.cp.rooms import Rooms


class Office(Rooms):
    def __init__(self, room_name):
        super().__init__(room_name)
        self.room_name = room_name
        self.room_capacity = 6
