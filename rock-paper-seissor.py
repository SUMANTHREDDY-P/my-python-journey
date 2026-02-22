import random
computer=["rock","paper","scissors"]
while True:
    game = random.choice(computer)
    user = input("enter your choice : ").lower()
    if user == "q":
        print('--Thanks for playing--')
        break

    print('The computer chose : ', game)
    if user == game:
        print("you Draw ")
    elif user == "rock":
        if game == "scissors":
            print("you win")
        elif game == "paper":
            print("you lose")
    elif user == "scissors":
        if game == "rock":
            print("you lose")
        elif game == "paper":
            print("you win")
    elif user == "paper":
        if game == "scissors":
            print("you lose")
        elif game == "rock":
            print("you win")
    else:
        print("-----Plese Enter Valide Choice------")

    print("press 'q' to exit")