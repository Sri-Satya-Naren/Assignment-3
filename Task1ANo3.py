from functools import reduce
def factorial(a):
    lst = []
    for i in range(1, a + 1):
        lst.append(i)
    fac = reduce(lambda x, y: x * y, lst)
    print("Factorial:", fac)
num = int(input("Enter a number: "))
factorial(num)