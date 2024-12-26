from constants.game_constants import DIVIDER
from abilities_folder.hero_data import abilities

def print_choice():
    """ aká je tvoja voľba: input"""
    return input("Aká je tvoja voťba? ")

def print_wrong_answer():
    """Netrafil si sa, musím sa ťa spýtať ešte raz"""
    print("Netrafil si sa, musím sa ťa spýtať ešte raz")

def print_good_by():
    """To ma mrzí, dúfam, že prídeš neskôr
    DIVIDER
    "Dovidenia"
    """
    print("To ma mrzí, dúfam, že prídeš neskôr")
    print(DIVIDER)
    print("Dovidenia")

def continue_game():
    """Výbore, máš odvahu to sa mi páči"""
    print("Výbore, máš odvahu to sa mi páči")

def hero_name():
    """Ako sa má volať tvoj hrdina"""
    return input("Ako sa má volať tvoj hrdina")

def confirm_name(names_of_hero):
    """0 - Chcem zmeniť meno
       1 - Áno chcem sa volať {hero_name()}
    """
    print("0 - Chcem zmeniť meno" )
    print(f"1 - Áno chcem sa volať {names_of_hero}")

def print_welcome_in_game(names_of_hero):
    """Vitaj v hre {names_of_hero} ideme na to!!"""
    print(f"Vitaj v hre {names_of_hero} ideme na to!!")

def point_information(point):
   """Máš {point} bodov, ktoré si rozdeľ naprieč schopnostiam podľa svojích preferencií."""
   print(f"Máš {point} bodov, ktoré si rozdeľ naprieč schopnostiam podľa svojích preferencií.")

def choice_better_abilities():
    """Ktorú schopnosť chceš vylepšiť?"""
    print("Ktorú schopnosť chceš vylepšiť?")

def empty_line():
    """Empty line print()"""
    print()

def status_information():
    """Teraz tvoje body vyzerajú takto"""
    print("Teraz tvoje body vyzerajú takto")

def print_finish_add_abilities(name_of_hero):
    """Výborne {name_of_hero}. Dokončil si pridávanie schopností. Pre rekapituláciu, teraz vyzerajú tvoje schopnosti takto."""
    print(f"Výborne {name_of_hero}. Dokončil si pridávanie schopností. Pre rekapituláciu, teraz vyzerajú tvoje schopnosti takto.")

def print_ready_for_fight():
    """Si pripravený na prvý súboj?"""
    print("Si pripravený na prvý súboj?")


def print_abilities_options( ):
    """
   1 -  Útočná sila
    2 -  Obrana
    3 -  Obratnosť
    4 -  Skill
    5 -  Život
    6 -  Šťastie
    """
    for i, ability in enumerate(abilities.keys()):
       ability_option = str(i + 1) + ' - ' + ability
       if ability == "Život":
         ability_option += " " + "- jeden bod pridá 5 života"
       print(ability_option)


def print_abilities_points():
    """Útočná sila - 1,Obrana - 1,Obratnosť - 1,Skill - 1,Život - 50,Šťastie - 1,"""
    for i,j in abilities.items():
        print(f"{i} - {str(j['points'])}", end=', ')


