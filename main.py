from all_prints import choice, wrong_answer




should_continue=True
while should_continue:
    print("Práve si zapol hru Arkadius, v ktorej budeš bojovať proti príšerám a pro tom si zlepšovať svojho hrdinu. Si na to pripravený?")
    print("0 - Áno som")
    print("1 - Nie bojím sa")
    user_choice = choice()
    if  user_choice not in ["0", "1"]:
        wrong_answer()
        continue
