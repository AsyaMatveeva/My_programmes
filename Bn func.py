n = int(input())
b = []
for i in range(n):
    i = int(input())
    b.append(i)
print_scheme = 1
def B(n, print_scheme):
    for i in range(0, n // 2):
        if print_scheme == 1:
            com = 'connect %d with %d'
            print(com % (i, i + (n // 2)))
        if b[i] > b[i + (n // 2)]:
            c = b[i]
            b[i] = b[i + (n // 2)]
            b[i + (n // 2)] = c
B(n, print_scheme)
print(b)
