n = int(input())
def f(n):
    x = 1
    y = 1
    if n == 1:
        return(1)
    elif n == 2:
        return(1)
    else:
        for i in range(3, n + 1):
            a = x + y
            x = y
            print("x =", x)
            y = a
            print("y =", y)
        return(a)
print("result =", f(n))
