

from all_prints import choice, wrong_answer

abilities = {
    "Útočná sila": {
        "points": 1,
        "description": "Sila je potrebna k útoku, do ktorého okrem sily vstupuje aj obratnosť a skill."
    },
    "Obrana": {
        "points": 1,
        "description": "Celkový obrana sa ráta z bodov obrany + obratnosti."
    },
    "Obratnosť": {
        "points": 1,
        "description": "Obratnosť je dôležitá aj pre obranu aj pre útok."
    },
    "Skill": {
        "points": 1,
        "description": "SKill je dôležitý pri normálnom útoku ako aj kritickom útoku"
    },
    "Život": {
        "points": 50,
        "description": "Život je dôležitý pri bitke. Život sa dá doplniť po každom súboji."
    },
    "Šťastie": {
        "points": 1,
        "description": "Šťastie je dôležité pre kritický útok"
    }
}

#body pomocou ktorých sa vylepšujú abilities
start_points = 7


def print_ability_options():
    for i, ability in enumerate(abilities.keys()):
        ability_option = f"{str(i + 1)}- {ability}"
        if ability == "Život":
            ability_option += "- jeden bod ti pridá 5 života"
        print(ability_option)


def print_ability_points():
    for k, v in abilities.items():
        print(f"{k}-{str(v['points'])}", end=", ")



should_continue = True
while should_continue:
    print(
        "Práve si zapol hru Arkadius, v ktorej budeš bojovať proti príšerám a pro tom si zlepšovať svojho hrdinu. Si na to pripravený?")
    print("0 - Áno som")
    print("1 - Nie bojím sa")
    user_choice = choice()
    if user_choice not in ["0", "1"]:
        wrong_answer()
        continue

    elif user_choice == "1":
        print("To ma mrzí. Dúfam že prídeš neskôr")
        break

    print("Výborne máš odvahu. To sa mi páči")

    hero_name = ""
    while should_continue:
        name_choice = input("Ako sa bude volať tvoj hrdina? ")
        print(f"Si si istý, že tvoj hrdina sa bude volať {name_choice}?")
        print("0 - Nie chcem zmenit meno")
        print("1 - Áno som")
        choice_name=choice()

        if choice_name not in ["0", "1"]:
            wrong_answer()
            continue

        elif choice_name == "0":
            continue

        else:
            hero_name = name_choice
            break

    print()
    print(f"Ahoj, {hero_name}")
    print(f"{hero_name}, Tvoje schopnosti sú momentálne takto:")
    print_ability_points()
    print()
    print(f"Máš {start_points} bodov, ktoré si rozdel naprieč schopnostiam podľa svojich preferencií.")



    abilities_picked=False
    abilities_picked_count=0

    while not abilities_picked:
        print_ability_options()

        option= input(f"Máš {start_points} na zlepšenie. Ktorú schopnosť chceš vylepšiť? ")

        #   čisla si v stringu     prekonvetuje string na integer  dlzka abilities +1 aby zahrnala aj poslednu hodnotu
        if option.isnumeric() and int(option) in list(range(1,len(abilities)+1)):
            # vylistuj index abilities  [int(option)-1] pretoze index zacina od 0 a option id 1
            chosen_ability_name= list(abilities.keys())[int(option)-1]
            if chosen_ability_name =="Život":

                #Musí byť jasne ze je to v dictionary preto je tam abilities
                abilities[chosen_ability_name]["points"] += 5
                print(f"\n Vybral si so schopnosť {chosen_ability_name}. Pridávam ti 5 bodov")

            else:
                abilities[chosen_ability_name]["points"] += 1
                print(f"\n Vybral si so schopnosť {chosen_ability_name}. Pridávam ti bod")

        else:
            wrong_answer()
            continue

        start_points -= 1
        abilities_picked_count+=1
        if abilities_picked_count == 7:
           abilities_picked=True
           print(f"Výborne {hero_name}. Dokončil si pridávanie schopností. Pre rekapituláciu, teraz vyzerajú tvoje schopnosti takto.")
           print_ability_points()
           print("Si pripravený na prvý súboj?")




