from TaskA import Person

class Employee(Person):
    def __init__(self, name, gender, location, dept, id):
        super().__init__(name, gender, location)
        self._dept = dept
        self._id = id
    def __str__(self):
        return super().__str__() + " Department: " + self._dept +" Staff ID:" + self._id