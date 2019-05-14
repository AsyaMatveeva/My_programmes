n = int(input()) 
def Cat(n):
    Sum = 0
    if n == 0 or n == 1:
        Sum = 1
    else:
        for i in range(0, n):
            Sum += Cat(i) * Cat(n - i - 1)
    return(Sum)
Cat(n)
print(Cat(n))
