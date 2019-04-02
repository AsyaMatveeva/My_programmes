import random
n = int(input())
alf = [1]
for i in range(2, n + 1):
    alf.append(i)
random.shuffle(alf)
print(alf)
for i in range(n):
    buf = alf[i]
    #cursor
    c = i
    while c > 0 and buf < alf[c - 1]:
        alf[c] = alf[c - 1]
        c -= 1
        for i in (alf):
            print(i, ' ', end='')
        print()
    alf[c] = buf
    for i in (alf):
        print(i, ' ', end='')
    print()
 
