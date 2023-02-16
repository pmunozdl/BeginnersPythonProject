import random
import sys


user = 0
computer = 0
def game():
        global user
        global computer
        options = ["rock", "paper", "scissors"]
        user_input = input("Choose rock, paper, scissors or exit: ")
        computer_input = random.choice(options)
        if user == 3:
                    print("has ganado")
                    sys.exit()
        elif computer == 3:
                    print("gana el ordenador")
                    sys.exit()
        else:
             while True:
                if user_input == "exit":
                    print("Game ended")
                    sys.exit()

                elif user_input == "rock":
                    if computer_input =="rock":
                        print("Your input is: ", user_input)
                        print("computer input is: ", computer_input)
                        print("choose again")
                        game()
                    elif computer_input == "scissors":
                        print("Your input is: ", user_input)
                        print("computer input is: ", computer_input)
                        print("you wins")
                        user = user + 1
                        print("the score is: \n", "you:", user, "computer: ", computer)
                        game()
                    elif computer_input == "paper":
                        print("Your input is: ", user_input)
                        print("computer input is: ", computer_input)
                        print("computer wins")
                        computer = computer + 1
                        print("the score is: \n", "you:", user, "computer: ", computer)
                        game()
                elif user_input == "scissors":
                    if computer_input =="scissors":
                        print("Your input is: ", user_input)
                        print("computer input is: ", computer_input)
                        print("choose again")
                        game()
                    elif computer_input == "paper":
                        print("Your input is: ", user_input)
                        print("computer input is: ", computer_input)
                        print("you wins")
                        user = user + 1
                        print("the score is: \n", "you:", user, "computer: ", computer)
                        game()
                    elif computer_input == "rock":
                        print("Your input is: ", user_input)
                        print("computer input is: ", computer_input)
                        print("computer wins")
                        computer = computer + 1
                        print("the score is: \n", "you:", user, "computer: ", computer)
                        game()
                elif user_input == "paper":
                    if computer_input =="paper":
                        print("Your input is: ", user_input)
                        print("computer input is: ", computer_input)
                        print("choose again")
                        game()
                    elif computer_input == "rock":
                        print("Your input is: ", user_input)
                        print("computer input is: ", computer_input)
                        print("you wins")
                        user = user + 1
                        print("the score is: \n", "you:", user, "computer: ", computer)
                        game()
                    elif computer_input == "scissors":
                        print("Your input is: ", user_input)
                        print("computer input is: ", computer_input)
                        print("computer wins")
                        computer = computer + 1
                        print("the score is: \n", "you:", user, "computer: ", computer)
                        game()
                elif user_input != " rock" or user_input != "paper" or user_input != "scissors":
                        print("Invalid Input, choose again")
                        game()
        

game()

