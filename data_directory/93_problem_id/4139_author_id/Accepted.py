L = [int(s) for s in input().split()]
k,a,b = L[0],L[1],L[2]
if (b-a) % k == 0:
    if a % k == 0:
        print((b-a+k)//k)
    else:
        print((b-a)//k)
else:
    if a % k == 0:
        print(b//k-a//k+1)
    elif b % k == 0:
        print(b//k-a//k)
    else:
        print(b//k-a//k)