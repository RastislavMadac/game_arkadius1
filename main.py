
import abilities_folder.hero_data
import constants.phase_constants
from abilities_folder.hero_data import fight_level
from phase.start import start_phase
from phase.intro import intro_phase
from phase.name import name_phase
from phase.abilities import abilities_update
from phase.check import phase_check
from constants.game_constants import DIVIDER
from print_all import print_ready_for_next_fight
from fight.battle import battle

current_phase=constants.phase_constants.START

continue_game=True

while continue_game:
    """call constants Start"""
    if current_phase==constants.phase_constants.START:
        current_phase= start_phase()

    """call constants intro"""
    if current_phase==constants.phase_constants.INTRO:
        current_phase= intro_phase()

    """call constants Name"""

    if current_phase == constants.phase_constants.NAME:
        current_phase = name_phase()

    """call constants end"""
    if current_phase==constants.phase_constants.END:
       continue_game=False

    """call constants Abilities"""
    if current_phase==constants.phase_constants.INTRO_ABILITIES:
        current_phase=abilities_update()
        print(DIVIDER)

    """call constants Fight"""
    if current_phase== constants.phase_constants.FIGHT:
        print(DIVIDER)
        battle(abilities_folder.hero_data.fight_level)
        print_ready_for_next_fight()
        break






