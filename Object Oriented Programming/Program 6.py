# Learning about Inheritance
# Name = Indrajeet Mondal; Date = 5th October 2023
# SourceCode

class User:
    @staticmethod
    def sign_in():
        return 'Logged In'


class Wizard(User):
    def __init__(self, name, power):
        self._name = name
        self._power = power

    def attack(self):
        return f'Attacking with a power of {self._power}'


class Archer(User):
    def __init__(self, name, num_arrows):
        self._name = name
        self.num_arrows = num_arrows

    def attack(self):
        return f'Attacking with arrows: {self.num_arrows}'


# Instantiating an object of the wizard class
wizard1 = Wizard("Harry Potter", 1000)
print((wizard1.sign_in()))
print(wizard1.attack())

# Instantiating an object of the archer class
archer1 = Archer("Hawkeye", 100)
print(archer1.attack())

# Using isinstance
print(isinstance(wizard1, User))
print(isinstance(wizard1, Wizard))
print(isinstance(archer1, User))
print(isinstance(archer1, Archer))
print(isinstance(wizard1, Archer))
print(isinstance(archer1, Wizard))
