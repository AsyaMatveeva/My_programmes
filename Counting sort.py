'''Counting sort is working in O(n). Conditions for work: all values are integers and non-negative, the maximum possible value is given. 
Program creates an array with quantity of element's repetitions at index, that corresponds to this element's value in the 1st array
(created at the beginning). 
Final output is a consistent record of 2nd array's indexex, repeting n times ('n' is a value at current index).'''
import random
n = int(input()) #Length of the sequence
m = int(input()) #Maximum possible value in the sequence
sort = [] #Data array
for i in range(0, n):
    i = random.randint(0, m)
    sort.append(i)
print(sort)
auxiliary = [0] * n #Array with quantities of repetitions
for i in sort:
    auxiliary[i] += 1
print(auxiliary)
for i in range(0, n):
    if auxiliary[i] > 0:
        for b in range(1, auxiliary[i] + 1):
            print(i,' ',end=' ')
