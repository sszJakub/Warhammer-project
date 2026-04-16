print("Hello, new Warhammer RPG player!")
print("This is a simple character sheet generator for the Warhammer RPG.")
print("Please enter your character's name:")
character_name = input("> ")
print(f"Welcome, {character_name}! Let's create your character sheet.")
print("You have to choose your character's race. Please select from the following options:")
races = ["Human", "High Elf", "Wood Elf", "Dwarf", "Halfling"]
for i in range(len(races)):
    print(f"{i+1}. {races[i]}")


while True:
    race_choice = input("> ")
    if race_choice in races:
        print(f"You have chosen {race_choice} as your character's race.")
        break
    else:
        print("Invalid choice. Please select a valid race.")

print("Choose your character's class. Please select from the following options:")
classes = ["Academics", "Burghers", "Courtiers", "Peasants", "Rangers", "Riverfolk", "Rogues", "Warriors"]
for i in range(len(classes)):
    print(f"{i+1}. {classes[i]}")

while True:
    class_choice = input ("> ")
    if class_choice in classes:
        print(f"You have chosen {class_choice} as your character's class")
        break
    else:
        print("Invalid choice. Please select a valid class.")

classes_professions = {
    "Academics": ["Apothecary", "Engineer", "Lawyer", "Nun", "Physician", "Priest", "Scholar", "Wizard"],
    "Burghers": ["Agitator", "Artisan", "Beggar", "Investigator", "Merchant", "Rat Catcher", "Townsman", "Watchman"],
    "Courtiers": ["Advisor", "Artist", "Duellist", "Envoy", "Noble", "Servant", "Spy", "Warden"],
    "Peasants": ["Bailiff", "Hedge Witch", "Herbalist", "Hunter", "Miner", "Mystic", "Scout", "Villager"],
    "Rangers": ["Bounty Hunter", "Coachman", "Entertainer", "Flagellant", "Messenger", "Pedlar", "Road Warden", "Witch Hunter"],
    "Riverfolk": ["Boatman", "Huffer", "Riverwarden", "Riverwoman", "Seaman", "Smuggler", "Stevedore", "Wrecker"],
    "Rogues": ["Bawd", "Charlatan", "Fence", "Grave Robber", "Outlaw", "Racketeer", "Thief", "Witch"],
    "Warriors": ["Cavalryman", "Guard", "Knight", "Pit Fighter", "Protagonist", "Soldier", "Slayer", "Warrior Priest"]
}

print(f"Now, choose your character's profession. Please select from the following options for the {class_choice} class:")
professions = classes_professions[class_choice]
for i in range(len(professions)):
    print(f"{i+1}. {professions[i]}")

while True:
    profession_choice = input("> ")
    if profession_choice in professions:
        print(f"You have chosen {profession_choice} as your character's profession.")
        break
    else:
        print("Invalid choice. Please select a valid profession.")

