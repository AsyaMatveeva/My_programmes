import random
heap_length = int(input())
Heap = ["n"]
for i in range(heap_length):
    i = random.randint(0, 100)
    Heap.append(i)
print(Heap)
def swap(a, b):
    c = a
    a = b
    b = c
def comparison(n, m):
    if n < m:
        swap(n, m)
for k in range(2, heap_length + 1):
    h_value = Heap[k]
    print(k, h_value)
    while Heap.index(h_value) > 1 and h_value > Heap[(Heap.index(h_value))//2]:
        comparison(Heap[Heap.index(h_value)//2], h_value)
print("Heap =", Heap)
