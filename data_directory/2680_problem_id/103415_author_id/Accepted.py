a = [int(i) for i in input().split()]
size = a[0]
a = a[1:]
a = sorted(a)
b = sorted([i%8 for i in range(5000000)])
s = [str(x) for x in a]
print(" ".join(s))