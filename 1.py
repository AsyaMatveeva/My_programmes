seq = list(map(int, input().split()))
pos = 0
neg = 0
ans = 0
for i in range(1, len(seq)):
    if seq[i] > 0:
        ans += pos + (seq[i - 1] > 0)
        pos, neg = 2 * pos + (seq[i - 1] > 0), 2 * neg + (seq[i - 1] < 0)
    else:
        ans += neg + (seq[i - 1] < 0)
        pos, neg = neg + (seq[i - 1] < 0), pos + (seq[i - 1] >  0)
print(ans)