n,m,p=map(int,input().split(" "))
l=[]
l.append(n)
l.append(m)
def mcd(a,b):
    while(b!=0):
       aux=a%b
       a=b
       b=aux
    return a
ps=1
signo=1
while(p!=0):
    p-=mcd(l[ps],p)
    ps=ps+signo*-1
    signo=-1*signo
print(ps)