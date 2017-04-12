from app.cp.rooms import Rooms


class Living(Rooms):
    def __init__(self, room_name):
        super().__init__(room_name)
        self.room_capacity = 4
