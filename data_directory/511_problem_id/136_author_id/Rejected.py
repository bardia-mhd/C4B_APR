a,b,c=[int(i) for i in input().split()]
if c==0:
    if a==b:
        print('YES')
    else:
        print('NO')
elif c>0:
    if b%c==a and b>=a:        
        print('YES')
    else:
        print('NO')
else:
    if a>=b and b%-c==a:
        print('YES')
    else:
        print('NO')