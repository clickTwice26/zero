#it will take list of some numbers and print the output of averge of these numbers

x = []
elements = input("Please enter the number of elements: ")
elements = int(elements)


while elements != len(x):

    y = input()
    if y != "":
        x.append(int(y))
        continue
    if y == "":
        print("input valid numbers")
        continue


print("The sum of Your Inputed Numbers:", sum(x))
print("the average of your inputed numbers is", sum(x)/ len(x))