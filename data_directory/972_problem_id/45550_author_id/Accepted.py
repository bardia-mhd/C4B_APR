import math
import sys
a,b=input().split()
a=int(a)
b=int(b)
if a==0 and b==0:
    print('NO')
    sys.exit()
if a>=b:
    if a-b>1:
        print('NO')
    else:
        print('YES')
else:
    if b-a>1:
        print('NO')
    else:
        print('YES')