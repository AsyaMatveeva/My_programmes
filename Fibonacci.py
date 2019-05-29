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
        return(Fib[n])
print(f(n))
