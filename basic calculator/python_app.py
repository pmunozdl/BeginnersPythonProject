#define the functions needed: add, sub, mul, div
#print options to the user
#ask for values
#call the functions
#while loop to continue the program until the user wants to exit



def add(a,b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer) + "\n")

def sub(a,b):
    answer = a - b
    print(str(a) + "-" + str(b) + "=" + str(answer) + "\n")

def mul(a,b):
    answer = a * b
    print(str(a) + "*" + str(b) + "=" + str(answer) + "\n")

def div(a,b):
    answer = a/b
    print(str(a) + "/" + str(b) + "=" + str(answer) + "\n")
def choose():
    print("A. add")
    print("B. Sub")
    print("C. Mul")
    print("D. Div")
    print("E. Exit")

    choice = input("input your choice:")

    if (choice.upper() == "A"):
        print("Addition")
        a = int(input("input first number:"))
        b = int(input("input second number: "))
        add(a,b)
    elif (choice.upper() == "B"):
        print("Substraction")
        a = int(input("input first number:"))
        b = int(input("input second number: "))
        sub(a,b)
    elif (choice.upper() == "C"):
        print("Multiplication")
        a = int(input("input first number:"))
        b = int(input("input second number: "))
        mul(a,b)
    elif (choice.upper() == "D"):
        print("Division")
        a = int(input("input first number:"))
        b = int(input("input second number: "))
        div(a,b)
    elif (choice.upper() == "E"):
        print("exit")
        quit()
    else:
        print("opción invalida, vuelve a elegir")
        choose()
choose()


    
