n = int(input())
n2 = int(input())
m = int(input())
m2 = int(input())
a = [n]
for i in range(n + 1, n2 + 1):
    a.append(i)
print(a)
b = [m]
for i in range(m + 1, m2 + 1):
    b.append(i)
print(b)
c1 = 0
c2 = 0
merge = []
while c1 < n2 - n + 1  and c2 < m2 - m + 1:
    if a[c1] < b[c2]:
        merge.append(a[c1])
        print(merge)
        c1 += 1
    else:
        merge.append(b[c2])
        print(merge)
        c2 += 1
while c1 < n2 - n + 1:
     merge.append(a[c1])
     c1 += 1
while c2 < m2 - m + 1:
        merge.append(b[c2])
        c2 += 1
for i in merge:
    print(i, ' ', end=' ')
print()
