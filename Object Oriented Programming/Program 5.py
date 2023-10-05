# Private and Public variables
# Name = Indrajeet Mondal; Date = 5th September 2023
# SourceCode

class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        print(f'Hello !! {self._name} is running')
        return

    def speak(self):
        print(f'My name is {self._name}, and I am {self._age} years '
              f'old')
        return

    # Instantiating the PlayerCharacter class


player1 = PlayerCharacter('Andrei', 100)
print(player1.run())
print(player1.speak())
