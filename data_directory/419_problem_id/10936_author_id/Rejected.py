import sys
n,a,b = map(int,input().split())

if(b == 0):
    res = a
elif(b < 0):
    b = abs(b)
    if (a < b):
        b -= (a-1)
        for i in range(n,0,-1):
            b -= 1
            if (b == 0):
                res = i
                break
    elif (a >= b):
        res = n


elif(b > 0):
    if( n - a < b):
        b -= n - a
        while(b > 0):
            for i in range(1,n+1):
                b -= 1
                if(b == 0):
                    res = i
                    break
    else:
        res = a + b
print(res)