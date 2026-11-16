import random
secrets = random.randint(1,100)
def ranges ():
    if secrets <= 20:
        print('asnwer is under 0 - 20')
    elif secrets <= 40:
        print('asnwer is under 20 - 40')
    elif secrets <= 60:
        print('asnwer is under 40 - 60')
    elif secrets <= 80:
        print('asnwer is under 60 - 80')
    else:
        print('asnwer is under 80 - 100')
def main():
    att =3
    while att > 0:
        num = int(input("Enter a number: "))
        if num > 100 or num < 0:
            print("<<<"+"give valid answer"+">>>")
        if num != secrets:
            att -= 1
            if att > 0:
                print(f"you have {att} attempts")
                if secrets < num:
                    print("you guess \"TOO HIGH\"  ")
                else:
                    print("you guess \"TOO LOW\"  ")

            else:
                print("YOU LOST THE GAME ")
                print('-'*20)
                print('The final answer is ', secrets)
        else:
            print('you got it')
            break


ranges()
main()
