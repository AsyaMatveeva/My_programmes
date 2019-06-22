'''Basic sort working in O(n^2). 
Compares each element of the given sequence with elements with bigger indexes and sorts the pair in acsending order (swap or pass).'''
import random
n = int(input()) #length of the sequence
num = [1] #unsorted seqence
for i in range(2, n + 1):
    num.append(i)
random.shuffle(num)
print (num)
b = 0 #Index of the element that is comparing with others at the moment
c = 1 #Index of the element that is comparing with num[b]
def swap(i, j):
    k = i
    i = j
    j = k
    return(i, j)
while b != n - 1:
    if c <= n - 1 - b:
        if num[b] > num[b + c]:
            num[b], num[b + c] = swap(num[b], num[b + c])
            for i in (num):
                print(i,' ', end='')
            print()
            c += 1
        else:
            c += 1
    else:
        b += 1
        c = 1
