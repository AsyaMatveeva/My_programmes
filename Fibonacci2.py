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
            i = x + y
            x = y
            print("x =", x)
            y = i
            print("y =", y)
        return(i)
print("result =", f(n))
