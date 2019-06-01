S = []
S1 = input().split()
for i in range(len(S1)):
    S1[i] = int(S1[i])

S2 = input().split()
for i in range(len(S2)):
    S2[i] = int(S2[i])

m = len(S2)
n = len(S1)
print(S1)
print(S2)
k = max(n, m)
if k == n:
    b = S1
    l = S2
else:
    b = S2
    l = S1
#print("k =", k)
#print("b =", b)
#print("l =", l)
def GCD(k):
    global S
    for i in range(0, k):
        if b[i] in l:
            S.append(b[i])
            print("S =", S)
    return(S)
print("GCD =", GCD(k))
