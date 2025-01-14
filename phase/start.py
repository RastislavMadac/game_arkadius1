

from constants.game_constants import DIVIDER
import constants.phase_constants
from print_all import (print_start_menu,
                       print_saved_menu_game,
                       print_loading_game,
                       print_loaded_game,
                       print_choice,
                       print_wrong_answer,
                       empty_line)
from save_load import load_game
import abilities_folder.hero_data
from phase.check import phase_check

def start_phase():

    while True:
        print_start_menu()
        choice=print_choice()
        print(DIVIDER)

        if choice not in ["0", "1"]:
            print_wrong_answer()
            continue
        if choice == "0":
            return constants.phase_constants.INTRO

        if choice=="1":
            jano, next_phase=load_game()
            if jano:
                print_loaded_game(abilities_folder.hero_data.names_of_hero)
            return phase_check(next_phase)
        else:
            """pítame sa znova pretože namal uloženú žiadnu hru alebo dal späť"""
            continue




