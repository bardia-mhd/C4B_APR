n,a,b,M,I=int(input()),1,1,1000000007,1000000005
for i in range(1,n):
  a=a*i%M
a=pow(a,I,M)
for i in range(n+1,n*2):
  b=b*i%M
print(((2*a*b)%M-n)%M)