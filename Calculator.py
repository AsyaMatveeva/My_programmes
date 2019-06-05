def argmin(mas):
    n = len(mas)
    #print('cur mas for argmin: ',mas)
    cur_min = mas[0]
    cur_index = 0
    for i in range(1,n):
        if mas[i] < cur_min:
            cur_min, cur_index = mas[i], i
    return cur_index
n = int(input())
bk = {}
bk = {1:[0, '']}
def ways(n):
    x = 0
    if n == 1:
        print('Operations sequence: ',bk[1][1])
        return(bk[1][0])
    else:
        for i in range(2, n + 1):
            bk[i]=['','']
            indexes = [i-1, i/2, i/3]
            if i % 6 == 0:
                x = min(bk[i - 1][0], bk[i / 2][0], bk[i/3][0])
                index_x = argmin([bk[i - 1][0], bk[i / 2][0], bk[i/3][0]])
                #print ("x =", x, ' index_x = ', index_x, 'i = ', i)
                bk[i][0] = x + 1
                bk[i][1] = bk[indexes[index_x]][1] + str(index_x+1)
                #print("sequence =", bk[i][1])
                continue
            elif i % 3 == 0:
                x = min(bk[i / 3][0], bk[i - 1][0])
                index_x = argmin([bk[i - 1][0], float('inf'), bk[i/3][0]])
                #print ("x =", x, ' index_x = ', index_x, 'i = ', i)
                bk[i][0] = x + 1
                bk[i][1] = bk[indexes[index_x]][1] + str(index_x+1)
                #print("sequence =", bk[i][1])
                continue
            elif i % 2 == 0:
                x = min(float('inf'), bk[i / 2][0], bk[i - 1][0])
                index_x = argmin([bk[i - 1][0], bk[i / 2][0], float('inf')])
                #print ("x =", x, ' index_x = ', index_x, 'i = ',i)
                bk[i][0] = x + 1
                bk[i][1] = bk[indexes[index_x]][1] + str(index_x+1)
                #print("sequence =", bk[i][1])
                continue
            else:
                bk[i][0] = bk[i - 1][0] + 1
                bk[i][1] = bk[i - 1][1] + str(1)
                #print("bk =", bk[i][1])
        return(bk[n][0],bk[n][1])
w,s = ways(n)
print('Min number of operations: ',w, ' sequence: ', s)
print()
