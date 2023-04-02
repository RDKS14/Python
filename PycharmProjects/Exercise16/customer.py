from TaskA import Person


class Customer(Person):
    def __init__(self, name, gender, location, account):
        super().__init__(name, gender, location)
        self.account = account

    def __str__(self):
        return super().__str__() + " Account number: " + self.account