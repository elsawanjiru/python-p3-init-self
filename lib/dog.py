# dog.py

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

    def sit(self):
        print(f"{self.name} is sitting.")
