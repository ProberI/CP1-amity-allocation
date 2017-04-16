from person import Person


class Fellow(Person):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.role = "FELLOW"
