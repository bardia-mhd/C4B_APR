def f(c):
    return c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U' or c == 'Y'
s = input().split()[0]
a = [0]*len(s)
for i in range (len(s)):
    a[i] = (s[i], i+1)
a = [elem for (letter, elem) in a if f(letter)]
b = [0]*(len(a))
if (len(a) != 0):
    b[0] = a[0]
    for i in range (1, len(a)):
        b[i] = a[i] - a[i-1]
    b.append (len(s) + 1 - a[len(a)-1])
    print (max (b))
else:
    print (len(s) + 1)