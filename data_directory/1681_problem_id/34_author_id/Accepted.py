n,m=map(int, input().split())
res=0
for i in range(int(n**0.5)+2):
    for j in range(n+1):
        if i**2+j==n and i+j**2==m:
            res+=1
print(res)