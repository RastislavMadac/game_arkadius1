

import constants.phase_constants
from phase.intro import intro_phase
from phase.name import name_phase
from phase.abilities import abilities_update
from phase.check import phase_check
from constants.game_constants import DIVIDER
from print_all import print_ready_for_next_fight

current_phase=constants.phase_constants.INTRO

continue_game=True

while continue_game:
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
        current_phase=phase_check(constants.phase_constants.FIGHT)
        print_ready_for_next_fight()
        break






