# Program to implement super()
# Name = Indrajeet Mondal; Date = 5th October 2023
# SourceCode

class User(object):
    def __init__(self, email):
        self.email = email

    @staticmethod
    def sign_in():
        return f'Logged In'


class Wizard(User):
    def __init__(self, name, type, email):
        super().__init__(email)
        self._name = name
        self._type = type
        self._email = email

    def tell_your_type(self):
        return (f'Hello !! I am {self._name}, and my magic '
                f'ability is {self._type}.')


# Creating instances of Wizard class
wizard1 = Wizard('Skullduggery', 'Adept',
                 'pleasant@gmail.com')
print(wizard1.sign_in())
print(wizard1.email)
print(wizard1.tell_your_type())
