n = int(input())
Fib = {}
Fib = {1:1, 2:1}
def f(n):
    if n == 1:
        return(1)
    elif n == 2:
        return(1)
    else:
        for i in range(3, n + 1):
            Fib[i] = Fib[i - 1] + Fib[i - 2]
            a = Fib[i - 1]
            print("a =", a)
            b = Fib[i]
            print("b =", b)
            Fib[i] = Fib.pop(i - 1)
            Fib[i] = b
            print("Fib1 =", Fib)
            Fib[i - 1] = Fib.pop(i - 2)
            Fib[i - 1] = a
            print("Fib2 =", Fib)
        return(Fib[n])
print("result =", f(n))
