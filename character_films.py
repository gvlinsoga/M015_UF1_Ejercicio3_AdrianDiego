from character import Character

class CharacterFilms:
    def __init__(self, edited, name, gender, skin_color, hair_color, height, eye_color, mass, homeworld, birth_year, num_films, first_film, alive_at_the_end):
        self.character = Character(edited, name, gender, skin_color, hair_color, height, eye_color, mass, homeworld, birth_year)
        self.num_films = num_films
        self.first_film = first_film
        self.alive_at_the_end = alive_at_the_end

    def get_num_films(self):
        return self.num_films

    def get_first_film(self):
        return self.first_film

    def get_alive_at_the_end(self):
        return self.alive_at_the_end    

    def get_info(self):
        self.character.printCharacter()
        print(f"Number films:", self.get_num_films())
        print(f"First film:", self.get_first_film())
        print(f"Alive at the end:", self.get_alive_at_the_end())
        print("\n")
