# Demonstrating polymorphism
# Name = Indrajeet Mondal; Date = 5th October 2023
# SourceCode

# Creating the User class which is later on inherited by Wizard and Archer class
class User(object):
    @staticmethod
    def sign_in():
        print('Logged In')

    @property
    def attack(self):
        return print('Do nothing')


# Defining the Wizard class
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        return print(f'Attacking with power of {self.power} !!')


# Defining the Archer class
class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        return print(f'Attacking with {self.num_arrows} arrows !!')


# Instantiating the Wizard class
wizard1 = Wizard('Merlin', 60)
# Calling the Wizard class attack() method
print(wizard1.attack())

# Instantiating the Archer class
archer1 = Archer('Robin', 30)
# Calling the Archer class attack() method
print(archer1.attack())


# 1st way of calling the attack() method and showing polymorphism
def attack_char(char):
    char.attack()


# Wizard attack() method will be called
attack_char(wizard1)

# Archer attack() method will be called
attack_char(archer1)

# 2nd way of calling the attack() method and showing polymorphism
char_list = [wizard1, archer1]
for var in char_list:
    var.attack()
