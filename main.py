from print_all import print_choice,print_wrong_answer,print_good_by,continue_game


print("Práve si zapol hru Arkádius, v ktorej budeš bojovať proti príšerám a pro tom so zlepšovať svojho hrdinu. Si na to pripravený?")

while True:
    print("0 - Nie, bojím sa")
    print("1 - Áno, poďme na to")

    all_choice = print_choice()

    if all_choice not in ["0", "1"]:
        print_wrong_answer()
        continue

    if all_choice =="0":
        print_good_by()
        break

    if all_choice=="1":
        continue_game()
        continue












