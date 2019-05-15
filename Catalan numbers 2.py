import math
n = int(input())
if n > 1:
    def C(a, b):
        f = math.factorial(a) // (math.factorial(b) * math.factorial(a - b))
        return(f)
    def Cat(n):
        result = C(2 * n, n) // (n + 1)
        return(result)
    Cat(n)
    print(Cat(n))
else:
    print(1)
