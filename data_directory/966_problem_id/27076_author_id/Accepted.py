n,m,k=map(int,input().split())
ans=1
m-=n
osn=0
while m>1:
    if osn==max(k-1,n-k):break
    ans+=1
    m-=1
    osnl,osnr=min(k-1,osn),min(n-k,osn)
    osn+=1
    m-=(osnl+osnr)
ans+=m//n
print(ans)