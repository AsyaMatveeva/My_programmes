    #number of circules
n = int(input())
    #sourse tower
j = int(input())
    #destination tower
i = int(input())
    #auxilliary tower
k = 6 - j - i
def move_tower(n, j, i, k):
    if n == 1:
        com = 'Remove 1 circule from %d tower to %d tower'
        print(com % (j, i))
    else:
        move_tower(n - 1, j, k, i)
        move_tower(1, j, i, k)
        move_tower(n - 1, k, i, j)
        
move_tower(n, j, i, k)
