import random
n = int(input())
mas = []
for i in range(1, n + 1):
    mas.append(i)
random.shuffle(mas)
print(mas)
low = 0
high = n - 1
result = []
def partition(mas, low, high):
    print("sorting mas = ", mas, "low = ", low, "high = ", high)
    global result
    pivot = mas[(high + low) // 2]
    print("pivot = ", pivot)
    i = low
    j = high
    print("i = ",i ," mas[i] = ", mas[i])
    while i < j:
        while mas[i] < pivot:
            i += 1
            print("i+=1: i = ",i," mas[i] = ", mas[i])
        print("j = ",j," mas[j] = ", mas[j])
        while mas[j] > pivot:
            j -= 1
            print("j -=1: j = ", j , "mas[j] = ", mas[j])
        c = mas[j]
        mas[j] = mas[i]
        mas[i] = c
        print("swap", mas[i], "and", mas[j])
        print(mas)
    print("return ",j)
    print("mas = ",mas)
    result = mas
    return(j)
def quick_sort(mas, low, high):
    if low < high:
        p = partition(mas, low, high)
        quick_sort(mas, low, p - 1)
        quick_sort(mas, p + 1, high)
quick_sort(mas, low, high)
print("final result = ",result)
