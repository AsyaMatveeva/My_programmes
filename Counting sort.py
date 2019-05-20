import random
n = int(input())
m = int(input())
sort = []
for i in range(0, n):
    i = random.randint(0, m)
    sort.append(i)
print(sort)
auxiliary = [0] * n
for i in sort:
    auxiliary[i] += 1
print(auxiliary)
for i in range(0, n):
    if auxiliary[i] > 0:
        for b in range(1, auxiliary[i] + 1):
            print(i,' ',end=' ')
