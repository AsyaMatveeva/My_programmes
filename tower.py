''' Circles are situated in descending order of their size (the biggest is the lowest) on one tower (sourse tower) of three possible. 
Putting bigger circle on the lesser is forbidded. 
The task is to put all the circles to the destination tower (different froom sourse) in the descending order. 
Number of neccesary operations is 2^n (for n circles). 
Recursion way of solving the problem (if it''s necessary to put circles from 1st to 3rd tower): put n-1 circules from 1 tower to 2. 
Put the biggest circle from 1 tower to 3. Put n-1 circles from 2 to 3.''' 
n = int(input()) #number of circules
j = int(input()) #sourse tower
i = int(input()) #destination tower
k = 6 - j - i  #auxilliary tower
def move_tower(n, j, i, k):
    if n == 1:
        com = 'Remove 1 circule from %d tower to %d tower'
        print(com % (j, i))
    else:
        move_tower(n - 1, j, k, i)
        move_tower(1, j, i, k)
        move_tower(n - 1, k, i, j)
move_tower(n, j, i, k)
