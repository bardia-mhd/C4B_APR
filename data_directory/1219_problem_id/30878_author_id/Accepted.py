a=input()
cnt=0
ans=0
t=a[0]
for i in range(len(a)):
  if a[i]==t:
    cnt+=1
  else:
    #print(i)
    ans+=1
    cnt=1
  if(cnt==5):
    if(i+1!=len(a)):
      if(a[i+1]!=t):
        i+=1
      ans+=1
      cnt=0
  t=a[i]
print(ans+1 if cnt!=0 else ans)