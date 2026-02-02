print("1: Manually add elements in the array")
print("2: Choose array size and have all elements randomly generated(range - 0 to 100)")
option = int(input("Enter 1 or 2 to choose one of the options from above: "))

arr = []
num = ""

while option not in [1,2]:
    print("Please choose one of the options from above")
    option = int(input("Enter 1 or 2 to choose one of the options from above: "))

if option == 1:
    while True:
        element = input("Enter an element in the array or press ENTER to stop: ")
        if element == "":
            break
        arr.append(int(element))

    print(arr)
    num = int(input("Enter the number that needs to be found in the array: "))

elif option == 2:
    import random
    size = int(input("Enter the size of the array: "))
    for s in range(size):
        element = random.randint(0, 100)
        arr.append(element)

    print(arr)
    num = int(input("Enter the number that needs to be found in the array: "))

def linearSearch(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return print(i)
    return None

linearSearch(arr, num)