c, v0, v1, a, l = list(map(int, input().split()))
pages = v0 
s = 1
while pages < c:
    if v0 + s * a > v1:
        pages += v1 - l
    else:
        pages += v0 + s*a - l
    s += 1
print(s)