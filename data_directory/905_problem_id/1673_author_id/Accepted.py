n,m,k = map(int,input().split())
if k %2  == 0:
    l = 'R'
if k % 2 != 0:
    l = 'L'
if k % (2 * m) != 0:
    p = k // (2 * m) + 1
if k % (2 * m) == 0:
    p = k // (2 * m)
t = (k - (p - 1) * (2*m)) // 2 + (k - (p - 1) * (2*m)) % 2
print(str(p)+' '+str(t)+' '+l)