'''A square is filled with random values.
Start point is in the upper left corner, finish point is in the bottom right corner.
The cursor can move only down or right.
Each cage (includung start and finish) reduces your score by the value that containes.
This program shows the way from start to finish cage with minimum loss of points.
'''
import random
n = int(input()) #Length of the 1 sequence
m = int(input()) #Length of the 2 sequence
b = {} #Empty table for values' summation
for i in range(n):
    b[i] = {}
a = {} #Filled start table
c = {} #Binary sequence of necessary steps
for i in range(n):
    c[i] = {}
answer_dict = {} #Sequence of necessary steps
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
x = 1 #lines
y = 1 #columns
for i in reversed(range(1, m + n)):
        answer_dict[i] = str((n - x, m - y))
        if c[n - x][m - y] == 0:
            x += 1
        else:
            y += 1
answer_list = [] #answer as a list
for value in answer_dict.values():
    answer_list.append(value)
for i in reversed(answer_list):
    print(i, end=' ')
print()

