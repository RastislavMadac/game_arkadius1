import constants.phase_constants
from print_all import hero_name, confirm_name,print_choice,print_welcome_in_game
from constants.game_constants import DIVIDER



def name_phase():

    continue_game= True
    while continue_game:

       print(DIVIDER)
       name_of_hero=hero_name()

       confirm_name(names_of_hero=name_of_hero)

       confirm_hero_name = print_choice()

       if confirm_hero_name=="0":
           continue
       if confirm_hero_name=="1":
           print(DIVIDER)
           print_welcome_in_game(names_of_hero=name_of_hero)
           constants.phase_constants.INTRO_ABILITIES











