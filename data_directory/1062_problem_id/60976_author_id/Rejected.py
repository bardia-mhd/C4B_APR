z = input()
t = 1
summ = 0
k = 0
for e in str(z):
    print(e)
    if e == '4' or e == '7':
        k += 1
for e in str(k):
    if e != '4' and e != '7':
        print('NO')
        t = 0
        break
if t:
    print('YES')