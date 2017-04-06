from person import Person


class Fellow(Person):
    def __init__(self, Fellow_names="Paul"):
        self.Fellow_names = Fellow_names

    def get_attr(self):
        return self.Fellow_names
