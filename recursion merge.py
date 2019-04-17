import random
n = int(input())
a = [1]
for i in range(2, n + 1):
    a.append(i)
random.shuffle(a)
print(a)
b = 0
e = n - 1
b1 = 0
e1 = 0
mid1 = 0
def merge(a, b1, mid1, e1):
    result = []
    c1 = 0
    c2 = 0
    k1 = [a[b1]]
    for i in range(b1 + 1, mid1 + 1):
        k1.append(a[i])
    k2 = [a[mid1 + 1]]
    for i in range(mid1 + 2, e1 + 1):
        k2.append(a[i])
    while c1 < mid1 - b1 + 1 and c2 < e1 - mid1:
        if k1[c1] < k2[c2]:
            result.append(k1[c1])
            c1 += 1
        else:
            result.append(k2[c2])
            c2 += 1
    while c1 < mid1 - b1 + 1:
        result.append(k1[c1])
        c1 += 1
    while c2 < e1 - mid1:
        result.append(k2[c2])
        c2 += 1
    c3 = 0
    for i in range(b1, e1 + 1):
        a[i] = result[c3]
        c3 += 1

def veg(a, b, e):
    if e - b > 0:
        mid = (e + b) // 2
        veg(a, b, mid)
        veg(a, mid + 1, e)
        merge(a, b, mid, e)
        print(a)
veg(a, b, e)
