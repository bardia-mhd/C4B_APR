x, y = map(int, input().split())

c = min(x // 2, y // 24)
x -= 2 * c
y -= 24 * c

c = min(x // 3, y // 14)
x -= 3 * c
y -= 14 * c

c = min(x // 4, y // 4)
x -= 4 * c
y -= 4 * c

c = min(x, y // 34)
x -= 1 * c
y -= 34 * c

c = y // 44
y -= 44 * c

if 10 * x + y >= 22:
    print('Ciel')
else:
    print('Hanako')