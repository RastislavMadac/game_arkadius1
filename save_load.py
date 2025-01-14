

import abilities_folder.hero_data
import abilities_folder.hero_all_ponts

from abilities_folder.hero_data import abilities
from constants.game_constants import DIVIDER

from os import listdir
from os.path import isfile, join
from print_all import (print_saved_name,
                       print_info_saved_game,
                       print_choice,
                       print_wrong_answer,
                       print_no_saved_game,
                       print_back,
                       print_load_file,
                       print_loading_game,
                       print_game_position_loaded, empty_line
                       )

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
                # load condition game
            file_handler.write(next_phase)
            file_handler.write("\n")
            file_handler.write(str(abilities_folder.hero_all_ponts.avalaible_points))
            file_handler.write("\n")
            file_handler.close()
            print(print_info_saved_game())
            print(DIVIDER)
            break

        else:
            print_wrong_answer()
def load(file):
    print_loading_game(file.replace(".txt", ""))
    file_handler = open("saved/" + file, "r",encoding="utf-8")

    """ukáže nán ktoré operácia boli urobené"""
    name_loaded= False
    abilities_loaded=False
    abilities_loaded_counter=0
    next_phase_loaded=False
    next_phase = ""
    abilities_points_loaded=False

    for line in file_handler:
        """odstrani biele miesta pred a za slovom viac variable ako rstrip"""
        line=line.strip()
        if not name_loaded:
            hero_name= line
            abilities_folder.hero_data.names_of_hero=hero_name
            name_loaded=True
            print_game_position_loaded("name_loaded")
        elif not abilities_loaded:
            """ulozené values su takto Útočná sila - 3 preto si to splitneme pomlčkou """
            ability_key,points = line.split(" - ")
            """jednotlive císelne hodnoty prideli podľa poradia ability_key a pridá points"""
            abilities_folder.hero_data.abilities[ability_key]["points"] = int(points)
            abilities_loaded_counter+=1
            """keď counter dosiahne to koˇko je abilities v dictionary zmeni abilities loaded na True a bude pokračovať dalej vo for cikle"""
            if abilities_loaded_counter == len(abilities_folder.hero_data.abilities):
                abilities_loaded = True
                print_game_position_loaded("abilities_loaded")
        elif not next_phase_loaded:
                """do next_phase zapiše dalsie fazi a to je fight"""
                next_phase = line
                next_phase_loaded=True
                print_game_position_loaded("next_phase_loaded")
        elif not abilities_points_loaded:
           """zapiseme uložené body potrbne zmenit na integer"""
           abilities_folder.hero_all_ponts.avalaible_points= int(line)
           abilities_points_loaded=True
           print_game_position_loaded("abilities_points_loaded")

    """indikuje ze hra bola nacina spravne a posiela hraca do boja to je next phase"""
    return True, next_phase





def load_game():
    saved_files = []
    """return Tuple (boolean, string) - či sa podarilo načítať hru true a false a string je názov fázy, v ktorej pokračuje hra
        kedy nám vráti false  keď stlačíme späť alebo nemáme uložené žiadne hry"""
    """skenuje obsah foldra"""
    for file in listdir("saved"):
        """pridava obsah foldra do listu"""
        saved_files.append(file)

    """ak je ulozene niečo vo foldri """
    if len(saved_files)>0:
        print_back()
        for i, save in enumerate(saved_files):
            """Index začína 0 preto musime pripočítať +1 a premeniť na strig  vymažeme .txt aby názov bol bez koncovky"""
            print(f"{str(i+1)} - {save.replace('.txt', '')}")

        while True:
            print_load_file()
            choice=print_choice()
            if choice == "0":
                return False, ""

            """ak choice nieje ziadne čislo, alebo choice nieje integer v zozneme  ktorý je ulozený v premennej saved file a je v rozmedzí od 1 po pocet ulozený hodnôt v premenej"""
            if not choice.isdigit() or int(choice) not in list(range(0, len(saved_files)+1)):
                print(print_wrong_answer)
                continue

            else:
                game_to_load=saved_files[int(choice) - 1]
                return load(game_to_load)
    else:
        """ak je folder prázdny"""
        print_no_saved_game()
        return False





