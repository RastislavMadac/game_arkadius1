
import random

from abilities_folder.hero_data import abilities
from abilities_folder.enemy_data import enemies

def test(enemy):
    min_defence, max_defence = enemy['defence']
    defence = random.randint(min_defence, max_defence)


def battle(fight_level):
    enemy_data = enemies[fight_level]
    enemy = {
    "defence": (enemy_data["Obrana"], enemy_data["Obrana"]+enemy_data["Obratnosť"])
         }