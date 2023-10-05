# Learning about attributes and methods
# Name = Indrajeet Mondal; Date = 4th October 2023
# SourceCode

# Creating a PlayerCharacter class
class PlayerCharacter:
    # Class Object Attribute: value does not change across instances
    membership = True

    # __init__ is a constructor, it is called everytime an object of the class is created
    def __init__(self, name, age):
        # self.name and self.age are class attributes: value changes with instance change
        self.name = name
        self.age = age

    def run(self):
        print(f'{self.name} is running !!')
        return 'done'


# Creating instances of PlayerCharacter
player1 = PlayerCharacter("Percy", 21)
player2 = PlayerCharacter("Jason", 21)

# Displaying their class object attribute
print(f'Membership of {player1.name} is {player1.membership}')
print(f'Membership of {player2.name} is {player2.membership}')
