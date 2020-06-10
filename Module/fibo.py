def fibo(x):
    a = 0
    b = 1
    print(0)
    print(1)
    print(1)
    if x > 2:
        for i in range(2, x): #x-1
            c = a + b
            a = b
            b = c
            print(a+b)
    x = int(x)
    if x == 1:
        print(0)
    elif x == 2:
        print(0)
        print(1)
    elif x == 3:
        print(0)
        print(1)
        print(1)
def fibo_numbers(y):
    z = [0, 1, 1]
    a = 0
    b = 1
    for i in range(2, y):
        c = a + b
        a = b
        b = c
        z.append(a + b)
    print("The", y, "is", z[y - 1])


if __name__ == "__main__":
    print("It is a module for printing the fibonacci numbers made by 5hagat0")