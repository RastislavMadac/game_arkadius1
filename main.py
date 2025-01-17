
import abilities_folder.hero_data
import abilities_folder.hero_all_ponts
import constants.phase_constants
from abilities_folder.hero_data import fight_level,abilities
from phase.start import start_phase
from phase.intro import intro_phase
from phase.name import name_phase
from phase.abilities import abilities_update
from phase.check import phase_check
from constants.game_constants import DIVIDER
from print_all import print_get_relax,print_after_win,print_status_of_life,print_ready_for_next_fight
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
        current_phase=abilities_update(abilities_folder.hero_all_ponts.INTRO_ABILITIES_COUNT)
        print(DIVIDER)

    """call constants check"""
    if current_phase == constants.phase_constants.CHECK:
        current_phase = phase_check(constants.phase_constants.FIGHT)
        print(DIVIDER)

    """call constants Fight"""
    if current_phase== constants.phase_constants.FIGHT:
        print(DIVIDER)
        win, health_remaining = battle(abilities_folder.hero_data.fight_level)

        if win:
            #Bojovní vyhral
            print_status_of_life(str(health_remaining),abilities_folder.hero_data.abilities["Život"]["points"] )
            print_after_win(abilities_folder.hero_data.fight_level, abilities_folder.hero_data.fight_level )
            abilities_update(abilities_folder.hero_data.fight_level)
            abilities_folder.hero_data.fight_level+=1
            print(DIVIDER)
        else:
                #Bojovník prehral
            print_get_relax()
            print(DIVIDER)


        abilities_folder.hero_data.abilities["Život"]["points"]=health_remaining






