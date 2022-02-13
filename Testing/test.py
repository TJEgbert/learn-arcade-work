done = False
while not done:
    quit = input("Do you want to quit")
    if quit == "y":
        break

    if not done:
        attack = input("does your elf attack the dragon? ")
        if attack == "y":
            print("bad choice, you died.")
            break

    if not done:
        attack = input("Does your elf attempt to steal the gold? ")
        if attack == "y":
            print("bad choice, you died. ")
            break


