import random
n = int(input())
m = int(input())
b = {}
for i in range(n):
    b[i] = {}
a = {}
c = {}
for i in range(n):
    c[i] = {}
answer = {}
for i in range(n):
    a[i] = {}
    for j in range(m):
        a[i][j] = random.randint(0, 10)
print("a =", a)
for i in range(n):
    for j in range(m):
        b[0][0] = a[0][0]
        if i == 0 and j == 0:
            b[0][0] = a[0][0]
            c[0][0] = -1
            continue
        if i == 0 and j > 0:
            if j == 1:
                b[i][j] = a[i][j - 1] + a[i][j]
                c[i][j] = 1
            else:
                b[i][j] = b[i][j - 1] + a[i][j]
                c[i][j] = 1
            continue
        if j == 0 and i > 0:
            if i == 1:
                b[i][j] = a[i - 1][j] + a[i][j]
                c[i][j] = 0
            else:
                b[i][j] = b[i - 1][j] + a[i][j]
                c[i][j] = 0
            continue
        if i > 0 and j > 0:
            if a[i - 1][j] <= a[i][j - 1]:
                b[i][j] = a[i][j] + b[i - 1][j]
                c[i][j] = 0
            else:
                b[i][j] = a[i][j] + b[i][j - 1]
                c[i][j] = 1
print("b =", b)
print("min value =", b[n - 1][m - 1])
#print("c =", c)
x = 1
y = 1
for i in reversed(range(1, m + n)):
        answer[i] = str((n - x, m - y))
        if c[n - x][m - y] == 0:
            x += 1
        else:
            y += 1
answer1 = []
for value in answer.values():
    ans = value
    answer1.append(ans)
for i in reversed(answer1):
    print(i, end=' ')
print()

