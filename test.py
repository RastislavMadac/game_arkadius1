

from abilities_folder.hero_data import abilities

from print_all import print_hero_ready_stats,empty_line



def calculate_hero_attack():
    """výpočet útok na nepriatela"""
    return abilities["Útočná sila"]["points"],abilities["Útočná sila"]["points"] + abilities["Obratnosť"]["points"]+abilities["Skill"]["points"]

def print_hero_stats(hero):
    print_hero_ready_stats()
    print(f"Útok: minimum - {str(hero['attack'][0])} maximum- {str(hero['attack'][1])}" )
    print(f"Šanca na kritický útok - minimum - {str(hero['critical_hit'])} %" )
    print(f"Obrana: minimum - {str(hero['defence'][0])} maximum- {str(hero['defence'][1])}")
    print(f"Život - {str(hero['health'])}")

def simulate_battle(hero):

    print_hero_stats(hero)
    empty_line()



def battle(hero):
    hero={
            "attack":calculate_hero_attack(),
             """zober minimum 100 alebo druhy argument pokial je menšie číslo ako 100"""
            "critical_hit": min(100, (abilities["Skill"]["points"] * abilities["Šťastie"]["points"]) // 2),
            "defence":(abilities["Obrana"]["points"], abilities["Obrana"]["points"]+abilities["Obratnosť"]["points"]),
            "health":abilities["Život"]["points"]
        }

    print_hero_stats(hero)