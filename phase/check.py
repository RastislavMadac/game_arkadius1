from print_all import print_choice,print_wrong_answer, print_good_by,print_finish_game
import constants.phase_constants


def phase_check(next_phase):


    should_continue=True
    while should_continue:
        print("0 - Pokračovať na ", next_phase)
        print("1 - Upraviť hrdinu")
        print("2 - Uložiť hru")
        print("3 - Ukončiť hru")

        choice = print_choice()

        if choice not in ["0","1","2","3"]:
            print_wrong_answer()
            continue

        if choice =="0":
            return constants.phase_constants.FIGHT

        if choice == "1":
            # TODO hero check
            continue
        if choice == "2":
            # TODO save_game
            continue
        if choice =="3":
           while True:
                print_finish_game()
                choice1 = print_choice()
                if choice1 not in ["0","1"]:
                    print_wrong_answer()
                    continue
                if choice1=="1":
                    break
                if choice1 == "0":
                 print_good_by()
                 return constants.phase_constants.END


