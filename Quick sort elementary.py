import random
n = int(input())
mas = []
for i in range(1, n + 1):
    mas.append(i)
random.shuffle(mas)
print(mas)
def quick_sort(mas):
    left = []
    middle = []
    right = []
    result = []
    if len(mas) > 1:
        x = len(mas) // 2
        middle.append(mas[x])
        if x > 0:
            for i in range(0, x):
                if mas[i] > mas[x]:
                    right.append(mas[i])
                elif mas[i] == mas[x]:
                    middle.append(mas[i])
                elif mas[i] < mas[x]:
                    left.append(mas[i])
        if len(mas) - x > 1:
            for i in range(x + 1, len(mas)):
                if mas[i] > mas[x]:
                    right.append(mas[i])
                elif mas[i] == mas[x]:
                    middle.append(mas[i])
                elif mas[i] < mas[x]:
                    left.append(mas[i])
    else:
        return mas
    result = result + (quick_sort(left))
    result = result + middle
    result = result + (quick_sort(right))
    return result
quick_sort(mas)
res = quick_sort(mas)
print("Result after sort = ", res)
