
from print_all import print_saved_name,print_info_saved_game, print_choice,print_wrong_answer
import abilities_folder.hero_data
from constants.game_constants import DIVIDER


def save_game(next_phase):
    print(DIVIDER)
    print_saved_name(abilities_folder.hero_data.names_of_hero)
    while True:
        choice=print_choice()
        if choice.isalpha():
            #MAKE NAME OF FILE
            file_path= "saved/" + choice + ".txt"
            # NAME OF HERO (PLAYER)
            file_handler = open(file_path, "w", encoding="utf-8")
            file_handler.write(abilities_folder.hero_data.names_of_hero)
            file_handler.write("\n")
            # SEVED VALUES OF ABILITIES
            for n, p in  abilities_folder.hero_data.abilities.items():
                file_handler.write(str(n) + ' - ' + str(p['points']))
                file_handler.write("\n")
            file_handler.write(next_phase)
            file_handler.write("\n")
            file_handler.close()
            print(print_info_saved_game())
            print(DIVIDER)
            break

        else:
            print_wrong_answer()


