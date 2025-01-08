from idlelib.colorizer import prog_group_name_to_tag

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

def print_finish_game():
    """0 - Áno chcem ukončiť hru"
       1 - Chcem pokračovať
    """
    print("0 - Áno chcem ukončiť hru")
    print("1 - Chcem pokračovať")

def print_ready_for_next_fight():
    """Si pripravený na prvý súboj?"""
    print("Si pripravený na prvý súboj?")

def print_notification_about_abilities(name_of_hero):
    """{name_of_hero} tvoje schopnosti sú momentálne ne tom takto"""
    print(f"{name_of_hero} tvoje schopnosti sú momentálne ne tom takto")

def print_info_avalaible_points(avalaible_points):
    """Máš {avalaible_points} na pridelenie schopností """
    print(f"Máš {avalaible_points} na pridelenie schopností, musíš si upraviť body!!! ")

def print_info_about_no_points(info_point):
    """Nemáš žiadne body ktoré by so mohol pridať"""
    print(f"Nemáš žiadne body ktoré by so mohol {info_point} ")


def print_abilities_options(with_help_option=False):
    """
    1 -  Útočná sila
    2 -  Obrana
    3 -  Obratnosť
    4 -  Skill
    5 -  Život
    6 -  Šťastie
    """
    if  with_help_option:
        print("0 - Vysvetlivky - načo sú dobré jednotlivé schopnosti")
    for i, ability in enumerate(abilities.keys()):
       ability_option = str(i + 1) + ' - ' + ability
       if ability == "Život":
         ability_option += " " + "- jeden bod pridá 5 života"
       print(ability_option)

def print_abilities_options_descriprion():
    """
    Útočná sila - Sila je potrebna k útoku, do ktorého okrem sily vstupuje aj obratnosť a skill.
    Obrana - Celkový obrana sa ráta z bodov obrany + obratnosti.
    Obratnosť - Obratnosť je dôležitá aj pre obranu aj pre útok.
    Skill - SKill je dôležitý pri normálnom útoku ako aj kritickom útoku
    Život - Život je dôležitý pri bitke. Život sa dá doplniť po každom súboji.
    Šťastie - Šťastie je dôležité pre kritický útok
    """

    for i, ability in abilities.items():
       ability_option = f"{i} - {ability['description']}"
       print(ability_option)


def print_abilities_points():
    """Útočná sila - 1,Obrana - 1,Obratnosť - 1,Skill - 1,Život - 50,Šťastie - 1,"""
    for i,j in abilities.items():
        print(f"{i} - {str(j['points'])}", end=', ')


