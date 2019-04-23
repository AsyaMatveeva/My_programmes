import random
n = int(input())
b = []
x = random.randrange(0, n)
print(x)
y = random.randrange(x, n)
print(y)
s = [0, 1]
random.shuffle(s)
print(s[0])
for i in range(0, x):
    i = s[0]
    b.append(i)
random.shuffle(s)
print(s[0])
for i in range(x, y):
    i = s[0]
    b.append(i)
random.shuffle(s)
print(s[0])
for i in range(y, n):
    i = s[0]
    b.append(i)
print(b)
for i in range(0, n // 2):
    if b[i] > b[i + (n // 2)]:
        c = b[i]
        b[i] = b[i + (n // 2)]
        b[i + (n // 2)] = c
print(b)

