x1,x2,x3=map(int,input().split())
s=(x1+x2+x3)//3
z=0
if x1>=s:
    z+=x1-s
else:
    z+=s-x1
if x2>=s:
    z+=x2-s
else:
    z+=s-x2
if x3>=s:
    z+=x3-s
else:
    z+=s-x3
print(z)