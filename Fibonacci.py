def fibo(x):
    a = 0
    b = 1
    print(0)
    print(1)
    print(1)
    for i in range(2, x): #x-1
        c = a + b
        a = b
        b = c
        print(a+b)

x = input("Please input(How many numbers you want to print?):")
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
elif x > 2:
    fibo(x)