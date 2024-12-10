from constants.game_constants import DIVIDER

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
    print(f"Vitaj v hre {names_of_hero} ideme na to!!")
