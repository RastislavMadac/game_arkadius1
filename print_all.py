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