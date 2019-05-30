n = int(input())
c = 'way'
def ball(n):
    global c
    x = 0
    y = 0
    x = 1
    a = 1
    if n == 1:
        return(1)
    else:
        for i in range(2, n + 1):
            z = y
            #print("z =", z)
            y = x
            #print("y =", y)
            x = a
            #print("x =", x)
            a = x + y + z
            print("a =", a)
        c = 'ways'
        return(a)
print(ball(n), c)
