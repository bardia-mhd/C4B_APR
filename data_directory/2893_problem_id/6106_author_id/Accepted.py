s=input()
l=s.split()
n=int(l[0])
k=int(l[1])
a=n//2
p1=a//(k+1)
p2=k*p1
p3=n-p2-p1
if p3>=n/2 :
    print(int(p1),int(p2),int(p3))
else :
    print(0,0,n)