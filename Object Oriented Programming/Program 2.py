# Creating my own classes and objects
# Name = Indrajeet Mondal; Date = 4th October 2023
# SourceCode

# Creating a PlayerCharacter class
class PlayerCharacter:
    # __init__ is a constructor, it is called everytime an object of the class is created
    def __init__(self, name, age):
        # self.name and self.age are attributes
        self.name = name
        self.age = age

    def run(self):
        print(f'{self.name} is running !!')
        return 'done'


# Instantiating the PlayerCharacter class/ Creating an object of the PlayerCharacter class
player1 = PlayerCharacter('Skullduggery', 250)
player2 = PlayerCharacter('Lord Vile', 100)

# Displaying class attributes
print(player1.name, player1.age)
print(player2.name, player2.age)

# Calling class methods
print(player1.run())
print(player2.run())

# Both the objects are at different memory locations
print(player1)
print(player2)

# Adding an attribute to the object player2
player2.attack = 1000
print(f"Attack power of {player2.name} is:- {player2.attack}")
