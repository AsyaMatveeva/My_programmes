n = int(input())
x = []
x = input().split()
for a in range(n):
    x[a] = int(x[a])
print("x =", x)
m = int(input())
y = []
y  = input().split()
for b in range(m):
    y[b] = int(y[b])
print("y =", y)
table = {}
for i in range(n + 1):
    table[i] = {}
    for j in range(m + 1):
        table[0][j] = 0
        table[i][0] = 0
print("table =", table)
LCS = {}
for i in range(n + 1):
    LCS[i] = {}
    for j in range(m + 1):
        LCS[0][j] = 0
        LCS[i][0] = 0
print("LCS =", LCS)
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if x[i - 1] == y[j - 1]:
            table[i][j] = table[i - 1][j - 1] + x[i - 1]
            if LCS[i - 1][j - 1] != 0:
                LCS[i][j] = LCS[i - 1][j - 1], x[i - 1]
            else:
                LCS[i][j] = x[i - 1]
            #print("lcs =", LCS[i][j])
        else:
            if table[i - 1][j] >= table[i][j - 1]:
                table[i][j] = table[i - 1][j]
                LCS[i][j] = LCS[i - 1][j]
                #print("lcs =", LCS[i][j])
            else:
                table[i][j] = table[i][j - 1]
                LCS[i][j] = LCS[i][j - 1]
                #print("lcs =", LCS[i][j])
print("LCS =", LCS[n][m])
