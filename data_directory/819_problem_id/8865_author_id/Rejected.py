s=input()
s1=[i for i in range(len(s)) if s[i]=="A" or s[i]=="E" or s[i]=="I" or s[i]=="O" or s[i]=="U" or s[i]=="Y"]
d=0
for i in range(len(s1)-1):
    if s1[i+1]-s1[i]>d:
        d=s1[i+1]-s1[i]

if d==0 and len(s1)!=0:
    print(max(s1[0]+1,len(s)-s1[-1]))
elif len(s1)==0:
    print(len(s)+1)
else:
    d=max(d,len(s)-s1[-1])
    print (d )