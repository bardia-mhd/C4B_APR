n,k=map(int,input().split())
if k>n:print(-1)
else:
    s=("ab"*(n//2+1))[:n]
    print(s[:-(k-2)]+''.join([chr(97+i) for i in range(2,k)]) if k>2 else s)