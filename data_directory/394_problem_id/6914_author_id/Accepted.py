from sys import stdin
def input():
    return stdin.readline()


n,k=map(int,input().split())


ans=0
i=0
if k>=n//2:
    ans=n*(n-1)//2
else:
    ans=k*(2*n-2*k-1)

print(ans)