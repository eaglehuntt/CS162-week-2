import json

class Character:
    def __init__(
            self,
            new_playername = "none given",
            new_level = 5,
            new_vigor = 10,
            new_mind = 11,
            new_endurance = 10,
            new_strength = 9,
            new_dexterity = 13,
            new_intelligence = 9,
            new_faith = 8,
            new_arcane = 14,
            new_weapon_right = "Great Knife",
            new_weapon_left = "empty",
            new_helm = "none",
            new_chest_armor = "none"
            ):
        self.playername = new_playername
        self.level = new_level
        self.vigor = new_vigor
        self.mind = new_mind
        self.endurance = new_endurance
        self.strength = new_strength
        self.dexterity = new_dexterity
        self.intelligence = new_intelligence
        self.faith = new_faith
        self.arcane = new_arcane
        self.weapon_right = new_weapon_right
        self.weapon_left = new_weapon_left
        self.helm = new_helm
        self.chest_armor = new_chest_armor
    
    def __str__(self):
        result = f"playername: {self.playername}\n" \
        f"level: {self.level}\n" \
        f"stats-\nvigor: {self.vigor}\n" \
        f"mind: {self.mind}\n" \
        f"endurance: {self.endurance}\n" \
        f"strength: {self.strength}\n" \
        f"dexterity: {self.dexterity}\n" \
        f"intelligence: {self.intelligence}\n" \
        f"faith: {self.faith}\n" \
        f"arcane: {self.arcane}\n" \
        f"\nequipment-\nrighthand: {self.weapon_right}\n" \
        f"lefthand: {self.weapon_left}\n" \
        f"helm: {self.helm}\n" \
        f"chest_armor: {self.chest_armor}"
        return result
def save_character(character, filename):
    try:
        with open(filename, "w") as file:
            character_data = {
                "playername": character.playername,
                "level": character.level,
                "vigor": character.vigor,
                "mind": character.mind,
                "endurance": character.endurance,
                "strength": character.strength,
                "dexterity": character.dexterity,
                "intelligence": character.intelligence,
                "faith": character.faith,
                "arcane": character.arcane,
                "weapon_right": character.weapon_right,
                "weapon_left": character.weapon_left,
                "helm": character.helm,
                "chest_armor": character.chest_armor,
            }
            json.dump(character_data, file, indent=4)
        print(f"Character '{character.playername}' saved to {filename}")
    except Exception as e:
        print(f"Error saving character: {e}")

def load_character(filename):
    try:
        with open(filename, "r") as file:
            character_data = json.load(file)
            loaded_character = Character(
                new_playername=character_data["playername"],
                new_level=character_data["level"],
                new_vigor=character_data["vigor"],
                new_mind=character_data["mind"],
                new_endurance=character_data["endurance"],
                new_strength=character_data["strength"],
                new_dexterity=character_data["dexterity"],
                new_intelligence=character_data["intelligence"],
                new_faith=character_data["faith"],
                new_arcane=character_data["arcane"],
                new_weapon_right=character_data["weapon_right"],
                new_weapon_left=character_data["weapon_left"],
                new_helm=character_data["helm"],
                new_chest_armor=character_data["chest_armor"],
            )
            return loaded_character
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"Error loading character: {e}")
letmesoloher = Character(new_playername="Let Me Solo Her", new_level=179, new_weapon_right="uchigatana", new_weapon_left="Rivers of Blood", new_helm="Jar",new_vigor=40, new_mind=24, new_endurance=40, new_strength=38, new_dexterity=48, new_intelligence=28, new_faith=22, new_arcane=20 )
default = Character()


if __name__ == "__main__":
    print("##### Program Start #####")
    exit_program = False
    user_input = None
    

    while not exit_program:
        print("\nEnter one of the listed numbers to use that function:")
        print("\nEnter one of the listed numbers to use that function:")
        print("0 - Enter your own stats")
        print("1 - View default stats")
        print("2 - View preset")
        print("3 - Print your character stats")
        print("4 - Save character to file")
        print("5 - Load character from file")
        print("Type 'exit' to close the program")

        menu_input = input("Enter your choice: ")

        if menu_input == "0":
            user_input = Character(
                new_playername=input("Enter your Playername: ") or "none given",
                new_level=int(input("Level: ")),
                new_vigor=int(input("Vigor: ")),
                new_mind=int(input("Mind: ")),
                new_endurance=int(input("Endurance: ")),
                new_strength=int(input("Strength: ")),
                new_dexterity=int(input("Dexterity: ")),
                new_intelligence=int(input("Intelligence: ")),
                new_faith=int(input("Faith: ")),
                new_arcane=int(input("Arcane: ")),
            )
        elif menu_input == "1":
            print(default)
        elif menu_input == "2":
            print(letmesoloher)
        elif menu_input == "3":
            try:
                print(user_input)
            except:
                print("You must enter character stats first")
        elif menu_input == "4":
            if user_input:
                save_filename = input("Enter the filename to save your character: ")
                save_filename += ".txt"
                save_character(user_input, save_filename)
            else:
                print("You must create a character first.")
        elif menu_input == "5":
            load_filename = input("Enter the filename to load your character: ")
            load_filename += ".txt"
            user_input = load_character(load_filename)
            if user_input:
                print(f"Character '{user_input.playername}' loaded successfully.")
        elif menu_input.lower() == "exit":
            print("Goodbye!")
            exit_program = True

            