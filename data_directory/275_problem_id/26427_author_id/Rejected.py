from sys import stdin
txt = stdin.readline()
p = txt[0] + txt[2] + txt[4] + txt[3] + txt[1]
m = n = int(p)
n = (n*n) % 100000
n = (n*n) % 100000
n = (n*m) % 100000
print(n)