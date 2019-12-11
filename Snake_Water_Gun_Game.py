# Scissor Paper Stone

import random

def random_choice_gen():

    print('Let\'s start the game "Snake Water Gun" ')
    count = 0
    win = 0
    draw = 0

    lst =["Snake", "Water", "Gun"]
    print("1-Snake, 2-Water, 3-Gun")
    print("You Got 10 chances")

    try:

        while count<10:
            cpu_choice = random.randint(0, 2)
            print("****** Turn-", count+1, " ******")
            user_choice = int(input("Please enter your choice : "))

            while user_choice>2 or user_choice<0:
                print("your input is invalid")
                user_choice = int(input("Please insert again : "))

            print("your choice : ", lst[user_choice])
            print("computer's choice : ", lst[cpu_choice])

            if user_choice == cpu_choice:
                print("Draw")
                draw += 1
            else:
                if user_choice ==0:
                    if cpu_choice == 1:
                        print("You win the Game")
                        win +=1
                    if cpu_choice == 2:
                        print("You lost the game")
                elif user_choice == 1:
                    if cpu_choice == 0:
                        print("You lost the Game")
                    if cpu_choice == 2:
                        print("You win the Game")
                        win += 1
                elif user_choice == 2:
                    if cpu_choice == 0:
                        print("You win the Game")
                        win += 1
                    if cpu_choice == 1:
                        print("You lost the Game")
            count += 1

        print("********Reaults********")
        print("Your Total Win : ", str(win))
        print("Computer Total Win : ", str(10-win-draw))
        print("Total No. of Draws : ", str(draw))



    except Exception as e:
        print("Something went wrong")


if __name__ == "__main__":
    random_choice_gen()
