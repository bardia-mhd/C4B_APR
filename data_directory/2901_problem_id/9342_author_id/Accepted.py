c, v0, v1, a, l = map(int, input().split())
d, p = 0, 0
while p < c:
    p += min(v0 + a * d, v1)
    if d >= 1:
        p -= l
    d += 1
print(d)