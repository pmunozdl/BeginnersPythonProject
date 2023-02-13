#ask user if they want to generate a password or not
#if yes ask for password length
#generate password
#print password
import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("How long would you like your password to be?"))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

def main():
    option = input("Do you want to generate a password? (Y/N)" )

    if str(option).upper() == "Y":
        generate_password()
    elif str(option).upper() == "N":
        print("Program ended")
        exit()
    else:
        print("No valid option. Please, try again")
        main()
main()