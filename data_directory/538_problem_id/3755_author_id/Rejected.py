lst = list(map(int, input().split()))
data = [0] * 101
s = 0
for i in lst:
    data[i] += 1
    s += i
max_change = 0
for i in range(101):
    if data[i] > 2:
        max_change = max(max_change, i * 3)
    if data[i] > 1:
        max_change = max(max_change, i * 2)
    elif data[i] > 0:
        max_change = max(max_change, i)
print(s - max_change)