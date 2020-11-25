import random

def Game():

    print(" s = Snake \n w = Water \n g = Gun \n")

    Chances = 9
    no_of_chnaces = 0
    Computer_win = 0
    User_win = 0

    while no_of_chnaces < Chances:
        no_of_chnaces += 1

        list1 = ["s", "w", "g"]

        User = str(input("Enter s, w, g:"))
        Computer = random.choice(list1)

        if User == Computer:
            print("The match is tie, 0 point to each")

        elif User == "s" and Computer == "w":
            User_win = User_win + 1
            print("Ohh! Shit, You win \n")

        elif User == "w" and Computer == "g":
            User_win = User_win + 1
            print("Ohh! Shit, You win \n")

        elif User == "g" and Computer == "s":
            User_win = User_win + 1
            print("Ohh! Shit, You win \n")

        elif User == "w" and Computer == "s":
            Computer_win = Computer_win + 1
            print("Yeahh!, I win \n")

        elif User == "g" and Computer == "w":
            Computer_win = Computer_win + 1
            print("Yeahh!, I win \n")

        elif User == "s" and Computer == "g":
            Computer_win = Computer_win + 1
            print("Yeahh!, I win \n")

        else:
            print("Wrong input")

        print(f"Computer points = {Computer_win} \nUser points = {User_win}")
        print(f"{Chances - no_of_chnaces} are the chances remaining out of {Chances} \n")

    if User_win > Computer_win:
        print(" You are the winner \n")
    elif User_win == Computer_win:
        print("The match is tie \n")
    else:
        print("Computer is the winner \n")

    while True:
        user = str(input("Do you want to play again:\nYes = Y and No = N : "))

        if user == "Y":
            Game()
        elif user == "N":
            print("Game is over")
            break
        else:
            print("Wrong input\n")
            continue

Game()










