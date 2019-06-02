n = int(input())
bk = {}
bk = {1:[0, 0]}
def ways(n):
    x = 0
    if n == 1:
        return(bk[1][1])
    else:
        for i in range(2, n + 1):
            if i % 6 == 0:
                print("6i")
                x = min(bk[i / 3][0], bk[i / 2][0], bk[i - 1][0])
                print ("x =", x)
                bk[i][0] = x + 1
                bk[i][1] = list(bk.keys())[list(bk.values()).index(x)] * 10 + (bk[i][0] // list(bk.keys())[list(bk.values()).index(x)])
                print("bk =", bk[i][1])
                continue
            elif i % 3 == 0:
                print("3i")
                x = min(bk[i / 3][0], bk[i - 1][0])
                print ("x =", x)
                bk[i] = x + 1
                bk[i] = list(bk.keys())[list(bk.values()).index(x)] * 10 + (bk[i][0] // list(bk.keys())[list(bk.values()).index(x)])
                print("bk =", bk[i][1])
                continue
            elif i % 2 == 0:
                print("2i")
                x = min(bk[i / 2][0], bk[i - 1][0])
                print ("x =", x)
                bk[i] = x + 1
                bk[i] = list(bk.keys())[list(bk.values()).index(x)] * 10 + (bk[i][0] // list(bk.keys())[list(bk.values()).index(x)])
                print("bk =", bk[i][1])
                continue
            else:
                print("1i")
                bk[i] = bk[i - 1][0] + 1
                bk[i][1] = bk[i - 1][1] * 10 + 1
                print("bk =", bk[i][1])
        return(k[n])
print(ways(n))
