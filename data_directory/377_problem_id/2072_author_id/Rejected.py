a, b = [int(x) for x in input().split()]
mins = 0

while a > 0 and b > 0:
    mins += 1
    if a < b:
        a += 1
        b -= 2
    else:
        a -= 2
        b += 1
print(mins)