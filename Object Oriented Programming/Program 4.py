# Learning about __init__ constructor, @classmethod and @staticmethod
# Name = Indrajeet Mondal; Date = 4th October 2023
# SourceCode

# Creating PlayerCharacter class
class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        if age > 18:
            self.name = name
            self.age = age
        else:
            print("Age must be greater than 18")

    def shout(self):
        print(f'My name is {self.name}')

    @classmethod
    # cls is for class, cls is passed as the default argument instead of self
    # @classmethods can be used even without even instantiating an object
    def adding_things(cls, num1, num2):
        return num1 + num2

    @staticmethod
    # A static method is a method that belongs to a class rather than an instance of the class. It is a
    # method that is shared among all instances of a class.
    # A static method is bound to the class and not the object of the class. It can’t access or modify
    # class state. A static method does not receive an implicit first argument.
    def adding_things2(num1, num2):
        return num1 + num2


# Creating instances of PlayerCharacter
# player2 will have the default parameters assigned to it
player1 = PlayerCharacter('Benedict Hope', 53)
player2 = PlayerCharacter("Scott Mariani", 55)

# Calling class methods
player1.shout()
player2.shout()

# Calling a @classmethod
print(PlayerCharacter.adding_things(3, 5))

# Calling a @staticmethod
print(player1.adding_things(3, 5))
print(player2.adding_things(3, 5))
