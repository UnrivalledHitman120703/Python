# Learning about multiple inheritance
# Name = Indrajeet Mondal; Date = 5th October 2023
# SourceCode

class User:
    @staticmethod
    def sign_in():
        return 'Logged In'


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        return f'Attacking with power of {self.power}'


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        return f'{self.arrows} are now left !!'

    @staticmethod
    def run():
        return 'Running really fast !!'


class Grotesquery(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)
        self.power = power


gtry1 = Grotesquery('Faceless Ones', 100, 100)
print(gtry1.run())
print(gtry1.check_arrows())
print(gtry1.attack())
print(gtry1.sign_in())
