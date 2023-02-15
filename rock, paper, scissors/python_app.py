# import random

# user = 0
# computer = 0
# def points():
    
#     while user < 3 and computer < 3:
#         game()
#         if(user == 3):
#             print("you wins")
#         elif(computer == 3):
#             print("computers wins")
# def game():
#             options = ["rock", "paper", "scissors"]
#             user_input = input("Choose rock, paper, scissors or exit: ")
#             computer_input = random.choice(options)

#             if user_input == "exit":
#                 print("Game ended")
#                 exit()

#             elif user_input == "rock":
#                 if computer_input =="rock":
#                     print("Your input is: ", user_input)
#                     print("computer input is: ", computer_input)
#                     print("choose again")
#                     game()
#                 elif computer_input == "scissors":
#                     print("Your input is: ", user_input)
#                     print("computer input is: ", computer_input)
#                     print("you wins")
#                     user+=1
#                     print("the score is: \n", "you:", user, "computer: ", computer)
#                     game()
#                 elif computer_input == "paper":
#                     print("Your input is: ", user_input)
#                     print("computer input is: ", computer_input)
#                     print("computer wins wins")
#                     computer+=1
#                     print("the score is: \n", "you:", user, "computer: ", computer)
#                     game()
#             elif user_input == "scissors":
#                 if computer_input =="scissors":
#                     print("Your input is: ", user_input)
#                     print("computer input is: ", computer_input)
#                     print("choose again")
#                     game()
#                 elif computer_input == "paper":
#                     print("Your input is: ", user_input)
#                     print("computer input is: ", computer_input)
#                     print("you wins")
#                     user+=1
#                     print("the score is: \n", "you:", user, "computer: ", computer)
#                     game()
#                 elif computer_input == "rock":
#                     print("Your input is: ", user_input)
#                     print("computer input is: ", computer_input)
#                     print("computer wins wins")
#                     computer+=1
#                     print("the score is: \n", "you:", user, "computer: ", computer)
#                     game()
#             elif user_input == "paper":
#                 if computer_input =="paper":
#                     print("Your input is: ", user_input)
#                     print("computer input is: ", computer_input)
#                     print("choose again")
#                     game()
#                 elif computer_input == "rock":
#                     print("Your input is: ", user_input)
#                     print("computer input is: ", computer_input)
#                     print("you wins")
#                     user+=1
#                     print("the score is: \n", "you:", user, "computer: ", computer)
#                     game()
#                 elif computer_input == "scissors":
#                     print("Your input is: ", user_input)
#                     print("computer input is: ", computer_input)
#                     print("computer wins wins")
#                     computer+=1
#                     print("the score is: \n", "you:", user, "computer: ", computer)
#                     game()

# points()

import random

exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ["rock", "paper" , "scissors"]
    user_input = input("Choose rock, paper, scissors or exit: ")
    computer_input = random.choice(options)
    
    if user_input == "exit" :
        print("Game ended")
        print("You won a total score of "+str(user_points)+" and the computer total score is " +str(computer_points))
        exit = True

    if user_input == "rock":
        if computer_input == "rock":
            print("Your input is rock")
            print("computer input is rock")
            print("It is a tie!")
        elif computer_input == "paper":
            print("Your input is rock")
            print("computer input is paper")
            print(" computer wins")
            computer_points += 1
        elif computer_input == "scissors":
            print("Your input is rock")
            print("computer input is scissors")
            print("you win")
            user_points += 1

    elif user_input == "paper":
        if computer_input == "rock":
            print("Your input is paper")
            print("computer input is rock")
            print("you win!")
            user_points += 1
        elif computer_input == "paper":
            print("Your input is paper")
            print("computer input is paper")
            print("it's a tie!")
        elif computer_input == "scissors":
            print("Your input is paper")
            print("computer input is scissors")
            print("computer wins")
            computer_points += 1

    elif user_input == "scissors":
        if computer_input == "rock":
            print("Your input is scissors")
            print("computer input is rock")
            print("computer win!")
            computer_points += 1
        elif computer_input == "paper":
            print("Your input is scissors")
            print("computer input is paper")
            print("you win")
            user_points += 1
        elif computer_input == "scissors":
            print("Your input is scissors")
            print("computer input is scissors")
            print("its a tie")

    elif user_input != " rock" or user_input != "paper" or user_input != "scissors":
        print("Invalid Input")