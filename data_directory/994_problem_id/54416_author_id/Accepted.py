from math import *
#l=int(input())
#m=int(input())
#a=int(input())
#l, m,a = input(),input(),input()
#l=int(l)
#m=int(m)
#a=int(a)
l,m,a=input().split()
l=int(l)
m=int(m)
a=int(a)
r=ceil(l/a)
k=ceil(m/a)
print(k*r)