

import constants.phase_constants
from phase.intro import intro_phase
from phase.name import name_phase

current_phase=constants.phase_constants.INTRO

continue_game=True

while continue_game:
    """call constants intro"""
    if current_phase==constants.phase_constants.INTRO:
        current_phase= intro_phase()

    """call constants Name"""

    if current_phase == constants.phase_constants.NAME:
        current_phase = name_phase()

    if current_phase==constants.phase_constants.END:
       continue_game=False

    if current_phase==constants.phase_constants.INTRO_ABILITIES:
        pass






