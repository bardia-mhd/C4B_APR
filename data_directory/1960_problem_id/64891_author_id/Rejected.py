from math import fabs
a = [[int(j) for j in input().split()] for i in range(5)]
for i in range(5):
    for j in range(5):
        if a[i][j] == 1:
            rem_i = i + 1
            rem_j = j + 1
            break
print(fabs(3 - rem_i) + fabs(3 - rem_j))