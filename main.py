import random

def roll_dice(num_dice, sides):
    return sum([random.randint(1, sides) for _ in range(num_dice)])

def generate_rolls_for_attributes():
    return [roll_dice(2, 10) for _ in range(10)]



    



base_attibutes = {
    "Human": {
        "Weapon Skill": 20,
        "Ballistic Skill": 20,
        "Strength": 20,
        "Toughness": 20,
        "Initiative": 20,
        "Agility": 20,
        "Dexterity": 20,
        "Intelligence": 20,
        "Willpower": 20,
        "Fellowship": 20
    },
    "High Elf": {
        "Weapon Skill": 30,
        "Ballistic Skill": 30,
        "Strength": 20,
        "Toughness": 20,
        "Initiative": 40,
        "Agility": 30,
        "Dexterity": 30,
        "Intelligence": 30,
        "Willpower": 30,
        "Fellowship": 20
    },
    "Wood Elf": {
        "Weapon Skill": 30,
        "Ballistic Skill": 30,
        "Strength": 20,
        "Toughness": 20,
        "Initiative": 30,
        "Agility": 40,
        "Dexterity": 30,
        "Intelligence": 30,
        "Willpower": 30,
        "Fellowship": 20
    }, 
    "Dwarf": {
        "Weapon Skill": 30,
        "Ballistic Skill": 20,
        "Strength": 20,
        "Toughness": 30,
        "Initiative": 20,
        "Agility": 10,
        "Dexterity": 30,
        "Intelligence": 20,
        "Willpower": 40,
        "Fellowship": 10
    },
    "Halfling": {
        "Weapon Skill": 10,
        "Ballistic Skill": 30,
        "Strength": 10,
        "Toughness": 20,
        "Initiative": 20,
        "Agility": 20,
        "Dexterity": 30,
        "Intelligence": 20,
        "Willpower": 30,
        "Fellowship": 30
    }
    
}

def assign_stats(base_attributes, chosen_race):
    rolls = generate_rolls_for_attributes()
    assigned_stats = {}
    
    print ("\nYour rolls:")
    for i, roll in enumerate(rolls, start=1):
        print(f"{i}: {roll}")
    
    for stat, base in base_attibutes[chosen_race].items():
        while True:
            print(f"\nAssign a roll to (choose list index): {stat} (base {base})")
            print(f"Available rolls: {rolls}")
            choice = input("> ")
            
            if choice.isdigit():
                value = int(choice)

                if value in rolls:
                    index = rolls.index(value)
                    selected_roll = rolls.pop(index)
                    assigned_stats[stat] = base + selected_roll
                    print(f"{stat} = {base} + {selected_roll}")
                    break
            print("Invalid choice. Please select a valid roll number.")
    return assigned_stats



print("Hello, new Warhammer RPG player!")
print("This is a simple character sheet generator for the Warhammer RPG.")
print("Please enter your character's name:")
character_name = input("> ")
print(f"Welcome, {character_name}! Let's create your character sheet.")
print("You have to choose your character's race. Please select from the following options (Enter a number 1-5):")
races = ["Human", "High Elf", "Wood Elf", "Dwarf", "Halfling"]
for i in range(len(races)):
    print(f"{i+1}. {races[i]}")


while True:
    race_input = input("> ")
    if race_input.isdigit():
        race_choice = int(race_input)
        if 1 <= race_choice <= len(races):
            print(f"You have chosen {races[race_choice - 1]} as your character's race.")
            break
        else:
            print("Invalid choice. Please select a valid race.")
    print("Invalid input. Please enter a number corresponding to your choice.")

chosen_race = races[race_choice - 1]

print("Choose your character's class. Please select from the following options:")
classes = ["Academics", "Burghers", "Courtiers", "Peasants", "Rangers", "Riverfolk", "Rogues", "Warriors"]
for i in range(len(classes)):
    print(f"{i+1}. {classes[i]}")

while True:
    class_input = input("> ")
    if class_input.isdigit():
        class_choice = int(class_input)
        if 1 <= class_choice <= len(classes):
            print(f"You have chosen {classes[class_choice - 1]} as your character's class")
            break
    print("Invalid choice. Please select a valid class.")

chosen_class = classes[class_choice - 1]


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

print(f"Now, choose your character's profession. Please select from the following options for the {chosen_class} class:")
professions = classes_professions[chosen_class]
for i in range(len(professions)):
    print(f"{i+1}. {professions[i]}")

while True:
    profession_input = input("> ")
    if profession_input.isdigit():
        profession_choice = int(profession_input)
        if 1 <= profession_choice <= len(professions):
            print(f"You have chosen {professions[profession_choice - 1]} as your character's profession.")
            break
    else:
        print("Invalid choice. Please select a valid profession.")
chosen_profession = professions[profession_choice - 1]


print(f"Congratulations! You have created basics for your character:")
print(f"Name: {character_name}")
print(f"Race: {chosen_race}")
print(f"Class: {chosen_class}")
print(f"Profession: {chosen_profession}")
      
print("You can now proceed to fill in the rest of your character sheet with attributes, skills, and equipment.")
for stat, value in base_attibutes[chosen_race].items():
    print(f"{stat}: {value}")

print("Now, let's roll for your character's attributes. You will roll 2d10 for each attribute and add the base value")
final_stats = assign_stats(base_attibutes, chosen_race)


print("\nYour final attributes are:")
for stat, value in final_stats.items():
    print(f"{stat}: {value}")

