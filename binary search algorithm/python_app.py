# a function that takes a list and target parameter
#multiples variables: middle, start, end, steps
#recursion or while loop
#increase the steps each time a split is done
#conditions to track target position

def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start<=end):
        print("Step", steps, ":", str(list[start:end+1]))

        steps = steps + 1
        middle = (start+end) // 2

        if element == list[middle]:
            return middle
        elif element < list[middle]:
            end = middle - 1
        else: #element > list[middle]
            start = middle + 1
    return -1

def validation(): #anidar condiciones en la misma línea (ahorrar if else)
    list_length = input("Longitud lista: ") #me  devuelve la longitud de la lista
    if list_length.isdigit() == True:
        my_list = [input("Valor: ") for x in range(int(list_length))]
        my_list2 = ''.join(my_list) #list to str
        if my_list2.isdigit(): 
            my_list3 = list(my_list2)
            target = input("target: ")
            if target.isdigit() == True:
                binary_search(my_list3, target)
            else:
                print ("only numbers allowed")
                validation()
        else:
                print ("only numbers allowed")
                validation()
    else:
        print ("only numbers allowed")
        validation()
    
    
validation()