a, b = map(int, input().split())

i = 1
while True:
    a = a - i
    if a < 0:
        ans = "Vladik"
        break
    i += 1
    b = b - i
    if b < 0:
        ans = "Valera"
        break
    i += 1

print(ans)