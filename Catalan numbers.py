'''Reccurent way to count the given number of Catalan sequence.
Catalan numbers - quantity of right arrangement of n pairs of brackets for n from 0 to infinity (C0 = 1, C1 = 1).'''
n = int(input()) #Number of Catalan sequence's element to count
def C_num(n):
    Sum = 0
    if n == 0 or n == 1:
        Sum = 1
    else:
        for i in range(0, n):
            Sum += C_num(i) * C_num(n - i - 1)
    return(Sum)
C_num(n)
print(C_num(n))
