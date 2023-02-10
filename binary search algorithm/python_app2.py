#without loops. For checking
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

list_length = input("Longitud lista: ")
my_list = [input("Valor: ") for x in range(int(list_length))]
target = input("target: ")
binary_search(my_list, target)