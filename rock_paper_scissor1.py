print("...rock...\n...paper...\n...scissors...\n")
print("HEY! LET'S BEGIN ;)\nEnter your choice :\n")
player1 = input("PLAYER 1: ")
print("\n### HEY ! NO CHEATING !!! ###\n" * 20)
player2 = input("PLAYER 2: ")

if player1 =="" or player2 == "":
    print("Choosing one is mandatory")
else:
    print("\n\tKABOOM!!\n")
    if player1 == player2:
        print("oooh!!, That's a tie.")
    elif player1 == "rock":
        if player2 == "paper":
            print("yoohoo! PLAYER2 wins")
        elif player2 == "scissors":
            print("yoohoo! PLAYER1 wins")
    elif player1 == "paper":
        if player2 == "scissors":
            print("yoohoo! PLAYER2 wins")
        elif player2 == "rock":
            print("yoohoo! PLAYER1 wins")
    elif player1 == "scissors":
        if player2 == "rock":
            print("yoohoo! PLAYER2 wins")
        elif player2 == "paper":
            print("yoohoo! PLAYER1 wins")
    else:
        print("Ohkay, someone made a wrong selection !!")
print("\n\n")