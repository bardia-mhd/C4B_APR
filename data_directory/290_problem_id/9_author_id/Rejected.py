def d():
    a, b, c = map(int,input().split())
    if c < b and c < a:
        return "No"
    if c % b == 0 or c % a == 0:
        return "Yes"
    q = max(a,b)
    k = a + b - q
    v = c
    while c > 0:
        c -= q
        if c % k == 0:
            return "Yes"
    c = v
    while c > 0:
        c -= k
        if c % q == 0:
            return "Yes"
    return "No"
print(d())