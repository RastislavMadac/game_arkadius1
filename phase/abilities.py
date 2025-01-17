

import abilities_folder.hero_data
from abilities_folder.hero_data import abilities
from print_all import print_abilities_options_descriprion,print_ready_for_fight, print_finish_add_abilities,status_information,print_wrong_answer,print_abilities_points,print_abilities_options,print_choice, point_information, empty_line,choice_better_abilities
import abilities_folder.hero_all_ponts
import constants.phase_constants

from constants.game_constants import DIVIDER

def abilities_update(avalaible_points):
    abilities_folder.hero_all_ponts.points_for_abilities+=avalaible_points

    print(f"{abilities_folder.hero_data.names_of_hero}, tvoje schopnosti sú montálne na tom takto:")
    print_abilities_points()
    empty_line()
    print(DIVIDER)
    point_information(point=abilities_folder.hero_all_ponts.points_for_abilities)


    should_continue =True
    while should_continue:
        print_abilities_options(with_help_option=True)
        choice_better_abilities()
        choice = print_choice()
        print(DIVIDER)

        if choice == "0":
            print_abilities_options_descriprion()
            print(DIVIDER)
            continue

        if choice.isnumeric() and int(choice) in list(range(0, len(abilities)+1)):

            #Name of abilyties
            chosen_ability_name=list(abilities.keys())[int(choice)-1]

            #Index of abilyties
            chosen_ability=abilities[chosen_ability_name]


            print(f"Vybral si si schopnosť {chosen_ability_name} pridávam ti bod")
            if chosen_ability_name == "Život":
                chosen_ability["points"]+=5
            else:
                chosen_ability["points"]+=1
            status_information()
            print_abilities_points()
            empty_line()
            abilities_folder.hero_all_ponts.points_for_abilities -= 1
            point_information(point=abilities_folder.hero_all_ponts.points_for_abilities)

        else:
            print_wrong_answer()
            continue
        abilities_folder.hero_all_ponts.ability_picked_count += 1

        if abilities_folder.hero_all_ponts.ability_picked_count==avalaible_points:
            should_continue=False

    print(DIVIDER)
    print_finish_add_abilities(abilities_folder.hero_data.names_of_hero)
    print_abilities_points()
    empty_line()
    print_ready_for_fight()
    return constants.phase_constants.CHECK








