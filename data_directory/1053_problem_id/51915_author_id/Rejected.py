n = int(input())
test = 0
i = 0
j = 0
x = True
y = True

while y:
    while x:
        i += 1
        test = i*4 + j*7
        if test == n:
            x = False
            y = False
        elif test > n:
            i = 0
            break

    test = i*4 + j*7
    if test == n:
        x = True
        y = True
        break
    elif test > n:
        x = False
        y = False
    j += 1

if not x and not y:
    print(-1)
else:
    print(str(4)*i+str(7)*j)