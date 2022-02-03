def a(x):
    print("A start, x =", x)
    b(x+1)
    print("A end x=", x)


def b(x):
    print("B start, x =", x)
    c(x + 1)
    print("B end x=", x)


def c(x):
    print("C start and end, x =", x)


a(5)
