import random
n = int(input())
num = [1]
for i in range(2, n + 1):
    num.append(i)
random.shuffle(num)
print (num)
b = 0
c = 1
while b != n - 1:
    if c <= n - 1 - b:
        if num[b] > num[b + c]:
            x = num[b]
            num[b] = num[b + c]
            num[b + c] = x
            for i in (num):
                print(i,' ', end='')
            print()
            c += 1
        else:
            c += 1
    else:
        b += 1
        c = 1
