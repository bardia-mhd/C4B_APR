from math import sqrt
p, n = [], int(input())
def f(x, y): return (x + 2) * (y + 2) + (2 * (x + y + 2) * n) // (x * y)
for x in range(2, int(sqrt(n)) + 1):
    if n % x == 0: p.append(x)
p += [n // x for x in reversed(p)]
p = [1] + p + [n]
u = v = f(1, 1)
for m in p:
    for x in range(1, int(sqrt(m)) + 1): u = min(u, f(x, m // x))
print(u, v)