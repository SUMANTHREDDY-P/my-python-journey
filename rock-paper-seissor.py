import random
computer=["rock","paper","scissors"]
while True:
    user = input("enter your choice : ").lower()
    if user not in computer:
        print("--Enter Valid Choice--")
        continue
    game = random.choice(computer)
    if user == "q":
        print('--Thanks for playing--')
        break

    print('The computer chose : ', game)
    if user == game:
        print("you Draw ")
    elif (user == "rock" and game == "scissors") or \
         (user == "paper" and game == "rock") or \
         (user == "scissors" and game == "paper"):
        print("You Win")
    else:
        print("-----YOU LOSS------")

    print("press 'q' to exit")