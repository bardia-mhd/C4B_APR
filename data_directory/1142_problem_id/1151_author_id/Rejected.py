n,a,b=map(int,input().split())
n-=a
if n>b+1:
    print(n-b)
else:
    print(n)