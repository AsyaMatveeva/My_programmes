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
    heap_value = Heap[k]
    print("Heap[",k,"] =", heap_value)
    while Heap.index(heap_value) > 1 and heap_value > Heap[(Heap.index(heap_value))//2]:
        comparison(Heap[Heap.index(heap_value)//2], heap_value)
print("Heap =", Heap)
def sort(x, y, Heap):
    while x < y:
        compasrison(Heap[x], max(Heap[x * 2], Heap[(x * 2)+1]))
for i in range(1, heap_length + 1):
    swap(Heap[1], Heap[heap_length - i + 1])
    sort(1, heap_length - i, Heap)
print("Final sequence =", Heap)
