from math import *
def from10(a, n):
    if(a==0):
        return 0
    if(a==1):
        return 1
    k = log(a,n)
    b = ceil(k)
    if(b-k ==0):
        b+=1
    c = a//(n**(b-1))
    #print(b)
    return int(c)+from10(a-c*n**(b-1),n)
#print(from10(4,2))
a = int(input())
slog = 0
summ = 0
for i in range(2,a):
    summ+=from10(a,i)
    #print(summ)
print(summ//gcd(a-2,summ),(a-2)//(gcd(summ,a-2)),sep='/')