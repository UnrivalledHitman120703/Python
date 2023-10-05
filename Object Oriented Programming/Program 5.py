# Private and Public variables
# Name = Indrajeet Mondal; Date = 5th September 2023
# SourceCode

class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        return f'Hello !! {self._name} is running'

    def speak(self):
        return f'My name is {self._name}, and I am {self._age} years old'


# Instantiating the PlayerCharacter class


player1 = PlayerCharacter('Andrei', 100)
print(player1.run())
print(player1.speak())
