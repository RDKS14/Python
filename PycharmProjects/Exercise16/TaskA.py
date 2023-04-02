class Person:

    def __init__(self, name, gender, location):
        self._name = name
        self._gender = gender.upper()
        self._location = location

    def __str__(self):
        return "Name: " + self._name + " Gender: " + self._gender + " location:" + self._location
