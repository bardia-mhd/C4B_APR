# n, m e k

s = input().split()

n = int(s[0])
m = int(s[1])
k = int(s[2])

j = int((k - 1) / (2 * m))
col = int(((k - 1) % (2 * m)))
i = int(col / 2)
print(str(j + 1) + " " + str(i + 1), end = " ")
if col % 2 == 1:
    print('R')
else:
    print('L')