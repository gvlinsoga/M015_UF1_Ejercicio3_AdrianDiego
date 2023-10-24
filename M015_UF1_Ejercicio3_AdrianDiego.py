import json
from character import Character
from character_films import CharacterFilms

def functionList() -> list:
        json_file = open("StarWars.json", "r")
        data = json.load(json_file)
        infoch: []
        for character in data:
                infoch.append(Character)
        return infoch

def read_json():
    characters = []

    with open("starwars.json", "r") as json_file:
        data = json.load(json_file)

        for item in data:
            fields = item["fields"]
            character = Character(
                fields["edited"],
                fields["name"],
                fields["gender"],
                fields["skin_color"],
                fields["hair_color"],
                fields["height"],
                fields["eye_color"],
                fields["mass"],
                fields["homeworld"],
                fields["birth_year"]
            )
            characters.append(character)

    return characters

def load_character_films(characters):
    charactersFilms = []
    for character in characters:
        match character.name:
            case "Luke Skywalker":
                infoLuke = ["4", "Star Wars: Episode IV - A New Hope (1977)", "dead"]
                luke = CharacterFilms(
                    character.edited,
                    character.name,
                    character.gender,
                    character.skin_color,
                    character.hair_color,
                    character.height,
                    character.eye_color,
                    character.mass,
                    character.homeworld,
                    character.birth_year,
                    infoLuke[0],
                    infoLuke[1],
                    infoLuke[2]
                )
                charactersFilms.append(luke)

            case "Chewbacca":
                infoChewbacca = ["6", "Star Wars: Episode IV - A New Hope (1977)", "alive"]
                chewbacca = CharacterFilms(
                    character.edited,
                    character.name,
                    character.gender,
                    character.skin_color,
                    character.hair_color,
                    character.height,
                    character.eye_color,
                    character.mass,
                    character.homeworld,
                    character.birth_year,
                    infoChewbacca[0],
                    infoChewbacca[1],
                    infoChewbacca[2]
                )
                charactersFilms.append(chewbacca)

            case "Anakin Skywalker":
                infoAnakin = ["4", "Star Wars: Episode VI - Return of the Jedi (1983)", "dead"]
                anakin = CharacterFilms(
                    character.edited,
                    character.name,
                    character.gender,
                    character.skin_color,
                    character.hair_color,
                    character.height,
                    character.eye_color,
                    character.mass,
                    character.homeworld,
                    character.birth_year,
                    infoAnakin[0],
                    infoAnakin[1],
                    infoAnakin[2]
                )
                charactersFilms.append(anakin)

            case _:
                charact = CharacterFilms(
                    character.edited,
                    character.name,
                    character.gender,
                    character.skin_color,
                    character.hair_color,
                    character.height,
                    character.eye_color,
                    character.mass,
                    character.homeworld,
                    character.birth_year,
                    "Null",
                    "Null",
                    "Null"
                )
                charactersFilms.append(charact)

    return charactersFilms
