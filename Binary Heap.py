import random
heap_length = int(input())
Heap = ["n"]
for i in range(heap_length):
    i = random.randint(0, 100)
    Heap.append(i)
print(Heap)
def sort(x, y, i):
    if Heap[2] >= Heap[3] or heap_length - i < 3:
        pos_max = 2
    else:
        pos_max = 3
    print("pos_max =", pos_max)
    while x <= y//2 and Heap[x] < Heap[pos_max]:
        Heap[x], Heap[pos_max] = Heap[pos_max], Heap[x]
        if heap_length >= x*2 + 1 and x*2 + 1 <= y:
            if Heap[x * 2] >= Heap[(x * 2) + 1]:
                pos_max = x*2
            else:
                pos_max = (x*2)+ 1
            print("pos_max_s =", pos_max)
    print("Heap =", Heap)
    return(Heap)
for k in range(2, heap_length + 1):
    heap_value = Heap[k]
    b = k
    while b > 1 and heap_value > Heap[b//2]:
        Heap[b//2], heap_value = heap_value, Heap[b//2]
        Heap[b] = heap_value
        b = b//2
print("Heap after conversion=", Heap)                                                
for i in range(1, heap_length):
    print("i =", i)
    Heap[1], Heap[heap_length - i + 1] = Heap[heap_length - i + 1], Heap[1]
    print("Heap =", Heap)
    if heap_length - i > 1:
        Heap = sort(1, heap_length - i, i)
print("Final sequence =", end=' ')
for i in range(1, heap_length + 1):
    print(Heap[i], end=' ')
    
