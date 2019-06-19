n = int(input()) "Number of the element in Fibonacci sequence
def f(n):
    x = 1 #previous Fibonacci number
    y = 1 #previous for x Fibonacci number
    if n == 1:
        return(1)
    elif n == 2:
        return(1)
    else:
        for i in range(3, n + 1):
            a = x + y "Element of Fibonacci sequence with number "i"
            x = y
            print("x =", x)
            y = a
            print("y =", y)
        return(a)
print("result =", f(n))
