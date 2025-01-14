

from print_all import (empty_line,
                       print_info_avalaible_points,
                       print_abilities_points,
                       print_notification_about_abilities,
                       print_choice,print_wrong_answer,
                       print_good_by,
                       print_finish_game)
import constants.phase_constants
import abilities_folder.hero_data
import abilities_folder.hero_all_ponts
from save_load import save_game


from abilities_folder.hero_update import  hero_add_point, hero_substract_point



def hero_add_points():
    while True:
        print("0 - Späť")
        print(f"1 - Pridať body (Máš - {abilities_folder.hero_all_ponts.avalaible_points} bodov na pridanie)")
        print("2 - Odstránenie bodov zo schopností")

        choice = print_choice()

        if choice not in ["0", "1", "2"]:
            print_wrong_answer()
            continue

        if choice == "0":
           hero_check(skip_start=True)

        if choice == "1":
            empty_line()
            if abilities_folder.hero_all_ponts.avalaible_points == 0:
                print_info_avalaible_points(abilities_folder.hero_all_ponts.avalaible_points)
            else:
                hero_add_point()
        if choice == "2":
            empty_line()
            hero_substract_point()

def phase_check(next_phase):


    should_continue=True
    while should_continue:
        print("0 - Pokračovať na ", next_phase)
        print("1 - Upraviť hrdinu")
        print("2 - Uložiť hru")
        print("3 - Ukončiť hru")

        choice = print_choice()

        if choice not in ["0","1","2","3"]:
            print_wrong_answer()
            continue

        if choice =="0":
            return next_phase

        if choice == "1":
            print_abilities_points()
            hero_check()
            empty_line()
        if choice == "2":
            save_game(next_phase)

        if choice =="3":
           while True:
                print_finish_game()
                choice1 = print_choice()
                if choice1 not in ["0","1"]:
                    print_wrong_answer()
                    continue
                if choice1=="1":
                    break
                if choice1 == "0":
                 print_good_by()
                 return constants.phase_constants.END
                break



def hero_check(skip_start=False):
    if  skip_start:
        print_notification_about_abilities(abilities_folder.hero_data.names_of_hero)
        print_abilities_points()
        empty_line()
        empty_line()
        print_info_avalaible_points(abilities_folder.hero_all_ponts.avalaible_points)

    should_continue=True
    while should_continue:
        empty_line()
        print("0 - Späť")
        print("1 - Upraviť schopnosti hrdinu")
        choice = print_choice()

        if choice not in ["0","1"]:
            print_wrong_answer()
            continue

        if choice =="0":
            empty_line()
            phase_check(constants.phase_constants.FIGHT)


        if choice == "1":
            empty_line()
            hero_add_points()






