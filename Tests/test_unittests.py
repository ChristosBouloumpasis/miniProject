import unittest
import sys
sys.path.append("..")
from rounds import * #TODO change that to something else


class Test_Methods(unittest.TestCase):


    #Testing adding a preference Happy path
    def test_whenDrinkNameValid_ShouldReturnTheSameName(self):
        # Arrange
        newRound = Round("Christos")
        newDrink = "Corona"
        usersName = "Jack"

        # Act
        newRound.inputChoice(newDrink,usersName)
        completedRound = newRound.returnRound()
        actualDrink = completedRound[usersName]

        # Assert
        self.assertEqual(actualDrink,newDrink)


    #Testing adding a preference with an empty string as a persons name
    def test_whenUserNameEmpty_ShouldThrowException(self):
        # Arrange
        newRound = Round("Christos")
        newDrink = "Corona"
        usersName = ""
        # Act

        # Assert

        pass




    #Testing add a new person correctly Happy path
    def test_something(self):
        # Arrange
        newRound = Round("Christos")
        usersName = "Henry"

        # Act
        newRound.createNewperson(usersName)
        completedRound = newRound.returnRound()
        names = completedRound.keys()
        # Assert
        self.assertTrue(usersName in names)



    #Testing add preference

if __name__ == "__main__":
    unittest.main()