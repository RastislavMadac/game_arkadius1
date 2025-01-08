
from print_all import print_info_about_no_points,print_info_avalaible_points,print_abilities_options,print_choice,status_information,print_abilities_points,empty_line,point_information,print_wrong_answer
from constants.game_constants import DIVIDER
from  abilities_folder.hero_data import abilities
import abilities_folder.hero_all_ponts




def hero_update():
    from phase.check import hero_check  # Lazy import, inside the function
    while True:
        print("0 - Späť")
        print(f"1 - Pridať body (Máš - {abilities_folder.hero_all_ponts.avalaible_points} bodov na pridanie)")
        print("2 - Odstránenie bodov zo schopností")

        choice = print_choice()

        if choice not in ["0", "1", "2"]:
            print_wrong_answer()
            continue

        if choice == "0":
            hero_check(skip_start=False)

        if choice == "1":
            empty_line()
            if abilities_folder.hero_all_ponts.avalaible_points == 0:
                print_info_avalaible_points(abilities_folder.hero_all_ponts.avalaible_points)
            else:
                hero_add_point()
        if choice == "2":
            empty_line()

            hero_substract_point()



def hero_add_point():

    print("0 - Už nechcem body (späť)")
    print_abilities_options()
    should_continue = True
    while should_continue:

        choice = print_choice()
        print(DIVIDER)
        if choice == "0":
            print(DIVIDER)
            hero_update()
            should_continue = False


        elif choice.isnumeric() and int(choice) in list(range(1, len(abilities) + 1)):

            # Name of abilyties
            chosen_ability_name = list(abilities.keys())[int(choice) - 1]

            # Index of abilyties
            chosen_ability = abilities[chosen_ability_name]

            if abilities_folder.hero_all_ponts.avalaible_points!=0:
                print(f"Vybral si si schopnosť {chosen_ability_name} pridávam ti bod")
                if chosen_ability_name == "Život":
                    chosen_ability["points"] += 5
                else:
                    chosen_ability["points"] += 1
                status_information()
                print_abilities_points()
                empty_line()
                abilities_folder.hero_all_ponts.avalaible_points -= 1
                point_information(point=abilities_folder.hero_all_ponts.avalaible_points)
            else:
                print_info_about_no_points("pridať")
                hero_update()

        else:
            print_wrong_answer()
            hero_substract_point()
def hero_substract_point():

    print("0 - Už nechcem body (späť)")
    print_abilities_options()
    should_continue = True
    while should_continue:

        choice = print_choice()
        print(DIVIDER)
        print("0 - Už nechcem body (späť)")
        print_abilities_options()
        if choice=="0":
            print(DIVIDER)
            hero_update()
            should_continue=False


        elif choice.isnumeric() and int(choice) in list(range(1, len(abilities) + 1)):

            # Name of abilyties
            chosen_ability_name = list(abilities.keys())[int(choice) - 1]

            # Index of abilyties
            chosen_ability = abilities[chosen_ability_name]

            if chosen_ability["points"] != 0:
                print(f"Vybral si si schopnosť {chosen_ability_name} odoberám ti bod")
                if chosen_ability_name == "Život":
                    chosen_ability["points"] -= 5
                else:
                    chosen_ability["points"] -= 1
                status_information()
                print_abilities_points()
                empty_line()
                abilities_folder.hero_all_ponts.avalaible_points += 1
                point_information(point=abilities_folder.hero_all_ponts.avalaible_points)
            else:
                print_info_about_no_points("odobrať")
                hero_update()

        else:
            print_wrong_answer()
            hero_substract_point()

