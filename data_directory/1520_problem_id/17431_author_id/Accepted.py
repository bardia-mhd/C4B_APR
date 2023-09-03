#! /bin/python

n, a, b, c = list(map(int, input().split()))

tab = [0] * (n + a + b + c)
tab[a] = 1
tab[b] = 1
tab[c] = 1
for i in range(n + 1):
    if tab[i] == 0:
        continue
    tab[i + a] = max(tab[i] + 1, tab[i + a])
    tab[i + b] = max(tab[i] + 1, tab[i + b])
    tab[i + c] = max(tab[i] + 1, tab[i + c])
#  print(tab)
print(tab[n])