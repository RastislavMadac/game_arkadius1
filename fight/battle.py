import time
import random

from abilities_folder.hero_data import abilities,names_of_hero
from abilities_folder.enemy_data import enemies
from print_all import print_enemy_missed_it,print_lost_fight,print_hero_status_life,print_winner,print_enemy_status_life,print_missed_it,print_power_attack, print_critical_fight, print_enemy_ready_stats, \
    print_hero_ready_stats, empty_line, print_start_fight_info
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


#kriticky utok nastane iba ak random vyberia menšie císlo ako ke vypočet kritického útoku
def is_critical_hit(chance):
    return random.randint(0,100)<chance


#(boolean, number) cize (win, health_remaining) -win, 50
def simulate_battle(hero, enemy):
    print_name_stats(hero, with_print=True)
    empty_line()
    time.sleep(1)
    print_name_stats(enemy, with_print=False)

    print(DIVIDER)
    print_start_fight_info()

    hero_turn=True
    while True:
        if hero_turn:
            min_attack, max_attack=hero['attack']
            attack=random.randint(min_attack,max_attack)
            if is_critical_hit(hero['critical_hit']):
                attack*=3
                print_critical_fight("útočíš")

            min_defence, max_defence= enemy['defence']
            defence= random.randint(min_defence,max_defence)

            # znamena ak je defence väčšie číslo ako attack bude vysledol vzdi 0
            final_attack = max(attack -defence,0)
            if final_attack>0:
                print_power_attack(names_of_hero,final_attack)
                enemy["health"]-=final_attack

                if enemy['health']>0:
                    print_enemy_status_life(enemy['name'], enemy['health'])
                else:
                    time.sleep(1)
                    print_winner()
                    print(DIVIDER)
                    return True, hero['health']


            else:
                print_missed_it()

        else:
            min_attack, max_attack = enemy['attack']
            attack = random.randint(min_attack, max_attack)
            if is_critical_hit(enemy['critical_hit']):
                attack *= 3
                print_critical_fight("Súper")

            min_defence, max_defence = hero['defence']
            defence = random.randint(min_defence, max_defence)

            # znamena ak je defence väčšie číslo ako attack bude vysledol vzdi 0
            final_attack = max(attack - defence, 0)
            if final_attack > 0:
                print_power_attack(names_of_hero, final_attack)
                hero["health"] -= final_attack

                if hero['health'] > 0:
                    print_hero_status_life(hero['health'])
                else:
                    time.sleep(1)
                    print_lost_fight()
                    print(DIVIDER)
                    return False, 0


            else:
                print_enemy_missed_it()

        empty_line()
        hero_turn = not hero_turn
        time.sleep(1)


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
