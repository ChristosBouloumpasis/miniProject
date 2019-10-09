
class Person:
    #constructor
    def __init__(self, id=None ,firstName=None, lastName=None, email=None):
       self.id = id
       self.firstName = firstName
       self.lastName = lastName
       self.email = email

    def getID(self):
        return self.id

    def getpersonDict(self):

        personDict = {
            "fistName": self.firstName,
            "lastName": self.lastName,
            "email": self.email
        }
        return personDict
