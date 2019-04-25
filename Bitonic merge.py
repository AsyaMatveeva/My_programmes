n = int(input())
b = []
x = 0
y = n
for i in range(n):
    i = int(input())
    b.append(i)
print_scheme = 1
def B(x, y, print_scheme):
    for i in range(x, (x + y) // 2):
        if print_scheme == 1:
            com = 'connect %d with %d'
            print(com % (i, i + ((y - x) // 2)))
        if b[i] > b[i + ((y - x) // 2)]:
            c = b[i]
            b[i] = b[i + ((y - x) // 2)]
            b[i + ((y - x) // 2)] = c
def bitonic_merge(x, y, print_scheme):
    if y - x > 1:
        B(x, y, print_scheme)
        bitonic_merge(x, (x + y) // 2, print_scheme)
        bitonic_merge((x + y) // 2, y, print_scheme)
bitonic_merge(x, y, print_scheme)
print(b)             
