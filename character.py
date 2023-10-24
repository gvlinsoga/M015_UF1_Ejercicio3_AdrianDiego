### Definición de la clase Character
class Character:
    def __init__(self, edited, name, gender, skin_color, hair_color, height, eye_color, mass, homeworld, birth_year):
        self.edited = edited
        self.name = name
        self.gender = gender
        self.skin_color = skin_color
        self.hair_color = hair_color
        self.height = height
        self.eye_color = eye_color
        self.mass = mass
        self.homeworld = homeworld
        self.birth_year = birth_year

    def printCharacter(self):
        print(f"Edited: {self.edited}")
        print(f"Name: {self.name}")
        print(f"Gender: {self.gender}")
        print(f"skin_color: {self.skin_color}")
        print(f"hair_color: {self.hair_color}")
        print(f"height: {self.height}")
        print(f"eye_color: {self.eye_color}")
        print(f"mass: {self.mass}")
        print(f"homeworld: {self.homeworld}")
        print(f"birth_year: {self.birth_year}")

from character import Character