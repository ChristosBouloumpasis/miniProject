class preference:
    #constructor
    def __init__(self,id=None, person=None, drink=None):
       self.id = id
       self.person = person
       self.drink = drink

    def getID(self):
        return self.id

    def getPerson(self):
        return self.person

    def getDrink(self):
        return self.drink

