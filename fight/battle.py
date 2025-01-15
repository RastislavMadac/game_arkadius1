import time

from abilities_folder.hero_data import abilities
from abilities_folder.enemy_data import enemies
from print_all import print_enemy_ready_stats,print_hero_ready_stats,empty_line,print_start_fight_info
from constants.game_constants import DIVIDER

# výpočet útok na nepriatela
def calculate_hero_attack():
    """výpočet útok na nepriatela"""
    return abilities["Útočná sila"]["points"],abilities["Útočná sila"]["points"] + abilities["Obratnosť"]["points"]+abilities["Skill"]["points"]

#preto parameter enimy_data pretoze máme viac nepriateľov
def calculate_enemy_attack(enemy_data):
    return enemy_data["Útočná sila"],enemy_data["Útočná sila"] + enemy_data["Obratnosť"]+enemy_data["Skill"]

def print_name_stats(name, with_print=False):
    if with_print:
        print_hero_ready_stats()
    else:
        print_enemy_ready_stats(name)
    print(f"Útok: minimum - {str(name['attack'][0])} maximum- {str(name['attack'][1])}" )
    print(f"Šanca na kritický útok - minimum - {str(name['critical_hit'])} %" )
    print(f"Obrana: minimum - {str(name['defence'][0])} maximum- {str(name['defence'][1])}")
    print(f"Život - {str(name['health'])}")


def print_hero_stats(hero):
    print_hero_ready_stats()
    print(f"Útok: minimum - {str(hero['attack'][0])} maximum- {str(hero['attack'][1])}" )
    print(f"Šanca na kritický útok - minimum - {str(hero['critical_hit'])} %" )
    print(f"Obrana: minimum - {str(hero['defence'][0])} maximum- {str(hero['defence'][1])}")
    print(f"Život - {str(hero['health'])}")

def print_enemy_stats(enemy):
    print_enemy_ready_stats(enemy)
    print(f"Útok: minimum - {str(enemy['attack'][0])} maximum- {str(enemy['attack'][1])}")
    print(f"Šanca na kritický útok - minimum - {str(enemy['critical_hit'])} %")
    print(f"Obrana: minimum - {str(enemy['defence'][0])} maximum- {str(enemy['defence'][1])}")
    print(f"Život - {str(enemy['health'])}")

def simulate_battle(hero, enemy):
    print_name_stats(hero, with_print=True)
    empty_line()
    time.sleep(1)
    print_name_stats(enemy, with_print=False)

    print(DIVIDER)
    print_start_fight_info()

def battle(fight_level):
    """podľa toho aka prísera utoci bude dane kolo"""
    enemy_data=enemies[fight_level]


    hero={
        "attack":calculate_hero_attack(),
     #zober minimum 100 alebo druhy argument pokial je menšie číslo ako 100
        "critical_hit": min(100, (abilities["Skill"]["points"] * abilities["Šťastie"]["points"]) // 2),
        "defence":(abilities["Obrana"]["points"], abilities["Obrana"]["points"]+abilities["Obratnosť"]["points"]),
        "health":abilities["Život"]["points"]
    }

    enemy = {
        "name":enemy_data["name"],
        "attack": calculate_enemy_attack(enemy_data),
        "critical_hit":min(100,(enemy_data["Skill"]*enemy_data["Šťastie"])//2),
        "defence": (enemy_data["Obrana"], enemy_data["Obrana"]+enemy_data["Obratnosť"]),
        "health": enemy_data["Život"]
    }
    return simulate_battle(hero, enemy)
