n = int(input())
xpos, ypos = [], []
for x in range(n):
    string = input()
    numbers = string.split()
    xpos.append(int(numbers[0]))
    ypos.append(int(numbers[1]))
a = -1
if n > 1:
    x = xpos[0]
    b = 1
    while xpos[b] == x:
        b += 1
        if b == n:
            break
    if b != n:
        m = abs(x - xpos[b])
        y = ypos[0]
        b = 1
        while ypos[b] == y:
            b += 1
            if b == n:
                break
        if b != n:
            n = abs(y - ypos[b])
            a = m * n
print(a)